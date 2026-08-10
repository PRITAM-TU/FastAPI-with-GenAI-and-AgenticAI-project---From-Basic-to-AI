from fastapi import Header,HTTPException


API_KEY="pritam@2005"

def varify_api_key(x_api_key: str = Header()):
    if API_KEY != x_api_key:
        raise HTTPException(
            status_code=401, 
            detail="No match with api key"
        )
    return x_api_key