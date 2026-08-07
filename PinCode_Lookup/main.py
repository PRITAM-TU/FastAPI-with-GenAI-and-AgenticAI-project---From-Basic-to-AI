from fastapi import FastAPI
import uvicorn
from exceptaion import pincode_not_found_exception_handler,invalid_pincode_exception_handler,pincode_not_found_error,invalid_pincde_error
from data import pincode_db
from model import PinCodeRequest,PincodeResponse,Bulk_pincodeRequest,ResponseBulkPincode




app=FastAPI(
    title="Pincode Lookup",
    description="This API allows you to look up information based on Indian pincodes.",
    version="1.0.0",
    
)
#register the coustom exception handlers
app.add_exception_handler(pincode_not_found_error,pincode_not_found_exception_handler)
app.add_exception_handler(invalid_pincde_error,invalid_pincode_exception_handler)

#creat the root endpoint 
@app.get("/")
def root( ):
    return {"message":"Welcome to the Pincode Lookup API."}


@app.get("/pincode/{code}", response_model=PincodeResponse)
def lookup_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise invalid_pincde_error(code,"Pincode must be a 6-digit number.")
    return PincodeResponse(
        message="Pincode lookup successful.",
        pincode=pincode_db[code]["pincode"],
        state=pincode_db[code]["state"],
        district=pincode_db[code]["district"]
    )



@app.post("/pincode/bulk_pincode", response_model=ResponseBulkPincode)
def bulk_lookup_pincode(request:Bulk_pincodeRequest):
    nums=request.pincodes
    print(nums)
    found_results=[]
    not_found_count=[]
    for code in nums:
        if len(code) != 6 or not code.isdigit():
            raise invalid_pincde_error(code,"Pincode must be a 6-digit number.")
        result=pincode_db.get(code)
        if result:
            found_results.append(PincodeResponse(
                message="Pincode lookup successful.",
                pincode=result["pincode"],
                state=result["state"],
                district=result["district"]
            ))
        else:
            not_found_count.append(code)
    return ResponseBulkPincode(
        message="Bulk pincode lookup completed.",
        results=found_results,
        found_count=len(found_results),
        not_found_count=not_found_count
    )






if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8001,reload=True)
