from fastapi import APIRouter,Depends,HTTPException,Query
from sqlmodel import Session,select
from database import get_session
from models import Respons_data,User,Book,Usercreated
from auth import varify_api_key,API_KEY



route_user=APIRouter(prefix="/user",tags=["all end point with auth "])
route_book=APIRouter(prefix="/book",tags=["all end point with auth "])
#route for  user write diffrent approch for head authntication 
@route_user.get("/",response_model=Respons_data,dependencies=[Depends(varify_api_key)])
def user(
):
    return {
        "message":"This is user endpoint",
    }


#post request for user data store  here we write the auth in diffrent way
@route_user.post("/",tags=["collect data from user"],response_model=User,dependencies=[Depends(varify_api_key)])
def user_data(*,session:Session =Depends(get_session),user_data:Usercreated):
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=404,
            detail="Email is already registered.",
        )
    user_db = User(**user_data.model_dump())
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db


@route_user.get("/alluser",response_model=list[User],dependencies=[Depends(varify_api_key)])
def All_user_data(*,session:Session =Depends(get_session)):
    try:
        user_db=session.exec(select(User)).all()
        return user_db
    except Exception as e:
        raise HTTPException(
         status_code=505,
            detail=f"Database error: {str(e)}",
        )

@route_user.get("/search",response_model=list[User],dependencies=[Depends(varify_api_key)])
def multi_parameter_filter(*,
    session: Session = Depends(get_session),
    # 1. Query parameters are optional (default=None)
    name: str | None = Query(default=None, description="Filter by user name"),
    email: str | None = Query(default=None, description="Filter by user email"),):
    statement=select(User)
    if name and email:
        # Matches BOTH name AND email
        statement = statement.where(User.name == name, User.email == email)
    elif name:
        # Matches name only
        statement = statement.where(User.name == name)
    elif email:
        # Matches email only
        statement = statement.where(User.email == email)
    users=session.exec(statement).all()
    return users

""" Enter all the book details into database and alos create tabel for that   """
#route for books
@route_book.get("/",dependencies=[Depends(varify_api_key)])
def book( dependencies=[Depends(varify_api_key)]):
    return{
        "message":"This is book  endpoint"
    }


@route_book.post("/upload",tags=["Enter all the book details with the help of this point "],response_model=Book,dependencies=[Depends(varify_api_key)])
def upload_book(*,session:Session =Depends(get_session),upload_book:Book):
    existing_book = session.exec(
            select(Book).where(Book.book_name==upload_book.book_name)
        ).first()
    if existing_book:
        raise HTTPException(
                    status_code=404,
                    detail="Book is already registered.",
                )
    book_db=Book(**upload_book.model_dump())
    session.add(book_db)
    session.commit()
    session.refresh(book_db)
    return book_db
#get all books details 
@route_book.get("/get_All",tags=["get all the book details with the help of this point "],response_model=list[Book],dependencies=[Depends(varify_api_key)])
def get_all_book(*,session:Session=Depends(get_session)):
    statement=select(Book)
    try:
            book_db=session.exec(statement).all()
            return book_db
    except Exception as e:
            raise HTTPException(
             status_code=505,
                detail=f"Database error: {str(e)}",
            )
    
    



