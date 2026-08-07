from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request



class pincode_not_found_error(Exception):
    def __inif__(self,pincode:str):
        self.pincode=pincode





class invalid_pincde_error(Exception):
    def __inif__(self,pincode:str,reason:str):
        self.pincode=pincode
        self.reason=reason





def pincode_not_found_exception_handler(request:Request,exc:pincode_not_found_error):
    return JSONResponse(
        status_code=404,
        content={"message":f"Pincode {exc.pincode} not found."}
    )

def invalid_pincode_exception_handler(request:Request,exc:invalid_pincde_error):
    return JSONResponse(
        status_code=400,
        content={"message":f"Invalid pincode {exc.pincode}: {exc.reason}"}
    )