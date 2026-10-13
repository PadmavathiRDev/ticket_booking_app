from fastapi import APIRouter
from app.schemas.user import UserCreate

router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/register")
def create_user(user: UserCreate):
    return{
        "message":"User Registered successfully",
        "name":user.name,
        "email":user.email
    }
             
             