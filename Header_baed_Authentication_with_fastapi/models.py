from sqlmodel import SQLModel,Field
from typing  import Optional
from datetime import datetime
from pydantic import EmailStr

#store user data for libary management system 
class User(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True)  # Prevents duplicate registrations
    college_name:str =Field(index=True)
    phone_number: Optional[str] = Field(default=None)
    role: str = Field(default="member")  # member, librarian, admin
    joined_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)
    max_borrow_limit: int = Field(default=5)


#create tabel for book
class Book(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    book_name: str = Field(index=True)  # Added index for faster search
    author: str = Field(index=True)
    isbn: str = Field(
        unique=True, index=True
    )  # Prevents duplicate book records
    total_copies: int = Field(default=1)
    available_copies: int = Field(default=1)

class Respons_data(SQLModel):
    name:Optional[str] =Field(default="pritam")
    message: Optional[str] =Field(default="Hey good morening")

class Usercreated(SQLModel):
    name: str
    email: EmailStr  # Ensures format is valid name@domain.com
    college_name: str
    phone_number: str | None = None  # Optional field