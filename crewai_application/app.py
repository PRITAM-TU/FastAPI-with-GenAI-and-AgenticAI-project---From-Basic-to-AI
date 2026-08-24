from crewai import Crew ,LLM,Agent,Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
#tool_2 for one agent2 whcih is writiing the research 
llm=LLM(
   model="gemini/gemini-2.5-flash",
    api_key=api_key,
    max_output_tokens=8192,
    stop_sequences=["END", "STOP"],
    stream=True,  # Enable streaming
    safety_settings={
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE"
    }
)

#tool1 for for  researcher 
googel_search_tool=SerperDevTool(n=2)


#Agent_1
Resercher__analyst_agent=Agent(
    role= "Senior Research Analyst",
    goal= "Conduct deep, accurate, and comprehensive research on given {topic}, verify facts from reliable sources, and synthesize complex data into clear, actionable insights from web source .",
    backstory= "You are an expert investigative researcher with years of experience gathering market data, academic insights, and technical details. You have a sharp eye for detail, never rely on unverified assumptions, and always present information in a structured, logical manner.",
    verbose=True,
    memory= True,
    tools=[googel_search_tool],
    allow_delegation=False   ,
    llm=llm
)

#agent 2 for content writter
content_writter=Agent(
    role="Senior Medical and Technical Content Writer",
    goal="Transform complex research data, medical case studies, and healthcare insights into clear, engaging, and scientifically accurate written content.",
    backstory="""You are an elite medical writer and healthtech journalist with a knack for translating dense technical jargon into accessible, compelling narratives. 
    You ensure all content maintains strict clinical accuracy, adheres to regulatory tones, and formats beautifully for executive audiences.""",
    verbose=True,
    memory=True,
    allow_delegation=False,
    llm=llm


) 

 # Task 1: Detailed Research based on the Medical Topic
research_task = Task(
    description="""
        Conduct exhaustive, factual market intelligence research on the specified topic: {topic}.
        Focus specifically on medical developments, deployments, and clinical applications leading up to and including the current operational year of 2026. 
        
        Your investigation must identify and extract:
        1. Architectural and clinical breakthroughs (e.g., specialized medical LLMs, EHR integrations, synthetic patient data models).
        2. Dominant production use cases across healthcare institutions (e.g., autonomous charting, radiology co-pilots, drug discovery pipelines).
        3. Measurable ROI metrics, clinical efficiency gains, and hospital deployment benchmarks.
        4. Technical, ethical, and regulatory bottlenecks (e.g., HIPAA compliance, FDA approvals, medical hallucinations, data privacy).
        5. Industry-shifting platform releases or medical-grade AI announcements leading into 2026.
        
        Strict Guardrails: Avoid high-level marketing buzzwords. Ensure every point is anchored in concrete technical, medical, or market facts.
    """,
    expected_output="""
        A structured Markdown document containing exactly 10 comprehensive, high-density bullet points. 
        Each bullet point must be a substantial paragraph (3-4 sentences) that pairs a specific medical Generative AI trend or breakthrough with concrete evidence, clinical context, or real-world enterprise examples.
    """,
    agent=Resercher__analyst_agent
)

# Task 2: Formatted Medical Report Generation
reporting_task = Task(
    description="""
        Review the raw 10-point research synthesis provided in the context from the previous task regarding {topic}. 
        Expand each of those 10 points into its own dedicated, deep-dive section for a comprehensive Medical Market Intelligence Report.
        
        For each section, you must:
        - Construct an explicit, highly professional medical-tech headline.
        - Deconstruct the underlying AI technology, clinical operational impact, and strategic healthcare business implications.
        - Ensure smooth narrative transitions while maintaining absolute factual alignment with the analyst's data.
        
        Strict Guardrails: Do not summarize or combine points. The final report must contain 10 distinct, exhaustive sections matching the research input. Maintain a highly professional, clinical, and executive-ready tone.
    """,
    expected_output="""
        A production-grade, fully fledged Markdown report ('report.md') featuring a Title, Executive Summary, 
        10 distinct, deeply detailed technical sections (each at least 3-4 paragraphs long with sub-headers), and a clinical Future Outlook conclusion.
    """,
    agent=content_writter,  # Fixed: Matched your variable name
    context=[research_task],
    output_file="report.md"
)

# Crew Definition and Orchestration
medical_crew = Crew(
    agents=[Resercher__analyst_agent, content_writter],
    tasks=[research_task, reporting_task],
    verbose=True
)