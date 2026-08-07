from pydantic import BaseModel,field_validator

class PinCodeRequest(BaseModel):
    pincode:str
    @field_validator("pincode")
    @classmethod
    def validation_pincode(cls,value:str):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be a 6-digit number.")
        return value
    




class PincodeResponse(BaseModel):
    message:str
    pincode:int
    state:str
    district:str


class Bulk_pincodeRequest(BaseModel):
    pincodes:list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_bulk_pincodes(cls, values: list[str]):
        if not values:
            raise ValueError("Pincodes list cannot be empty.Altest Enter at least one pincode.")
        for value in values:
            if len(value) != 6 or not value.isdigit():
                raise ValueError(f"Pincode {value} must be a 6-digit number.")
        return values



class ResponseBulkPincode(BaseModel):
    message:str
    results:list[PincodeResponse]
    found_count:int
    not_found_count:list[str]
