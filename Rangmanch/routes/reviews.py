from fastapi import APIRouter, Depends,HTTPException
from sqlmodel import Session,select,func
from model import Feedback,FeedbackCreate,FeedbackUpdate,FeedbackRead,FeedbackDelete,Response_delete
from database import get_session




route=APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)
@route.get("/")
def get_reviews():
    return {"message":"This is the reviews endpoint"}


#creat reviews in database and return the created review
@route.post("/create", response_model=FeedbackRead)
def create_review(*, session: Session = Depends(get_session), feedback: FeedbackCreate):
#here we convert the FeedbackCreate model to Feedback model(for to sotre the database easily and based one schema) and then add it to the database 
    db_feedback = Feedback(**feedback.model_dump())
    session.add(db_feedback)
    session.commit()
    session.refresh(db_feedback)
    return db_feedback

#here we write the code about pagiantion and sorting of the reviews based on the name and email and message and id
@route.get("/allreviews", response_model=list[FeedbackRead])
def get_all_reviews(*, session: Session = Depends(get_session)):
    try:
        reviews = session.exec(select(Feedback)).all()
        return reviews
    except Exception as e:
        return {"message": "Error occurred while fetching reviews"}


@route.get("/review/{review_id}", response_model=FeedbackRead)
def get_review(*, session: Session = Depends(get_session), review_id: int):
    try:
        review = session.get(Feedback, review_id)
        if not review:
            return {"message": "Review not found"}
        return review
    except Exception as e:
        return {"message": "Error occurred while fetching review"}


#update some message from emailid 
@route.patch("/review/update",response_model=FeedbackUpdate)
def update_review(*,session:Session =Depends(get_session),update_review:FeedbackUpdate):
    statement = select(Feedback).where(Feedback.email == update_review.email)
    db_feedback = session.exec(statement).first()
    
    # 2. If the email doesn't exist, raise a clean HTTP 404 error
    if not db_feedback:
        return FeedbackUpdate (
            email= update_review.email,
            message="Not update the review because we not found the specific email"
        )
    
    # 3. Update only the message field
    db_feedback.message = update_review.message
    
    # 4. Save the changes to your database
    session.add(db_feedback)
    session.commit()
    session.refresh(db_feedback)
    return FeedbackUpdate(
        email=db_feedback.email,
        message=db_feedback.message
        
    )



#delete some review dased on id 
@route.delete("/review/delete",response_model=Response_delete)
def review_delete(*,session:Session=Depends(get_session),delete_review:FeedbackDelete):
    statement = select(Feedback).where(Feedback.id == delete_review.id)
    db_feedback=session.exec(statement).first()

    if not db_feedback:
        return Response_delete(
                message="404 error show because we notfound the thid id "

            )
    try:
        # 3. Actually delete the record from the database session
        session.delete(db_feedback)
        session.commit()
        
    except Exception as e:
        # 4. Handle unexpected database connection issues safely
        session.rollback()
        raise HTTPException(
            status_code=404,
            detail="Database error occurred while deleting the review."
        )
    return Response_delete(
                    message="Your message was parmaent delete from our side  "
    
                )

    

    

            

    