from fastapi import FastAPI,Query,HTTPException
import uvicorn
from data import data
from fastapi import Request
from model import MenuResponse,MenuItem

app=FastAPI(
    title="Chai_point all menu",
    description="In bengaluru city one chai point present that serve the all menu that they have but they want to buid some api that send all the request related to that chai point",
    version='1.0.0',
    docs_url="/docs"

)

@app.get("/")
def Root():
    return {
        "message": "Welcome to chai point project",
        "Our all menu are available in /menu": data,
        "status": "success",
        "version": "1.0.0"
    }
@app.get("/about")
def about():
    return {
        "message": "This is a chai point project",
        "status": "success",
        "version": "1.0.0"
    }
# @app.get("/menu")
# def menu():
#     return {
#         "message": "All menu are available in this endpoint",
#         "menu": data
#     }

# @app.get("/menu/")
# def menu_by_id(request: Request):
#     id = request.query_params.get("id")
#     for item in data:
#         if item["id"]==int(id):
#             return {
#                 "message": "Menu item found",
#                 "menu": item
#             }
#     return {
#         "message": "Menu item not found",
#         "status": "error"
#     }
# @app.get("/menu/category/")
# def menu_by_category(request: Request):
#     category = request.query_params.get("category")
#     list1=[]
#     for item in data:
#         if item["category"]==category:
#             list1.append(item)
#     if len(list1)>0:
#         return {
#             "message": "Menu items found",
#             "menu": list1
#         }


#     return {
#         "message": "Menu item not found",
#         "status": "error"
#     }
#based on prices 
@app.get("/menu/price")
def based_on_price(request: Request):
    price = request.query_params.get("price")
    if price is None:
        return {
            "message": "Price query parameter is required",
            "status": "error"
        }
    try:
        price = int(price)
    except ValueError:
        return {
            "message": "Price must be a number",
            "status": "error"
        }

    items = []
    for item in data:
        item_price = int(item.get("price", 0))
        if price <= 100 and item_price <= 100:
            items.append(item)
        elif 100 < price < 200 and 100 < item_price < 200:
            items.append(item)
        elif price >= 200 and item_price >= 200:
            items.append(item)

    if items:
        return {
            "message": "Menu items found",
            "status": "success",
            "items": items
        }
    return {
        "message": "No menu items found for the given price range",
        "status": "error"
    }


@app.get("/menu",response_model=MenuResponse,response_model_exclude_none=True)
def menu_baed_on_categori(category:str | None =Query(default=None, description="Category of the menu item")):
    if category is None:
        raise HTTPException(status_code=400, detail="Category query parameter is required")
    items = [item for item in data if item["category"].lower() == category.lower()]
    if items:
        return MenuResponse(
            message="Menu items found",
            status="success",
            count=len(items),
            menu=[MenuItem(**item) for item in items]
        )
    return MenuResponse(
        message="No menu items found for the given category",
        status="error",
        count=0,
        menu=[]
    )
@app.get("/menu/{item_id}",response_model=MenuResponse)
def menu_by_id(item_id:int):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return MenuResponse(
            message="Menu item found",
            status="success",
            count=1,
            menu=[MenuItem(**item)]
        )
    raise HTTPException(status_code=400,detail="Menu item not found for the given id")
    
    



if __name__=="__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)

