from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
import uvicorn

# google-genai expects safety_settings to be a list, while some CrewAI
# integrations still provide the older dictionary form.
try:
    from google.genai import types as genai_types

    _original_config_init = genai_types.GenerateContentConfig.__init__

    def _generate_content_config_init(self, *args, **kwargs):
        settings = kwargs.get("safety_settings")
        if isinstance(settings, dict):
            kwargs["safety_settings"] = [
                {"category": category, "threshold": threshold}
                for category, threshold in settings.items()
            ]
        _original_config_init(self, *args, **kwargs)

    genai_types.GenerateContentConfig.__init__ = _generate_content_config_init
except (ImportError, AttributeError):
    pass

from app import medical_crew

class ReportRequest(BaseModel):
    topic: str = Field(
        ..., 
        description="The medical sector or AI topic to research.",
        example="The Impact & Application of Generative AI in the Medical Sector"
    )


app=FastAPI(
    title="Medical resercherand content writter tools",
    description="It all about the crewai platfrom"

    )
@app.get("/")
async def root():
    return{
        "message":"This is root endpoint"
    }


#for post request 
@app.post("/generate-report",status_code=status.HTTP_200_OK,
    summary="Generate Medical AI Market Intelligence Report")
async def report_genereate(request_data: ReportRequest):
    """
    Triggers the multi-agent crew asynchronously to research the provided topic
    and compile a professional markdown report.
    """
    # Validate that the topic is not empty or just whitespace
    if not request_data.topic or not request_data.topic.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The 'topic' field cannot be empty. Please provide a valid research topic."
        )
    
    try:
        # Inject the validated topic string into the crew input dictionary
        crew_inputs = {"topic": request_data.topic.strip()}
        
        # CrewAI supports kickoff_async to prevent blocking the FastAPI event loop
        crew_output = await medical_crew.kickoff_async(inputs=crew_inputs)
        
        # Return a structured production response
        return {
            "status": "success",
            "message": "Report generated successfully.",
            "saved_file": "report.md",
            "data": str(crew_output)
        }
        
    except Exception as e:
        # Safeguard against background agent or LLM failure
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during crew execution: {str(e)}"
        )

    



if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
