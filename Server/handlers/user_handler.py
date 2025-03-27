from fastapi import APIRouter
from models.users import Users

user_router = APIRouter(prefix='/users',tags=['/users'])


@user_router.get('/create')
def get_user():
    try:
        result =10/0
        return result
    
    except Exception as e:
        raise e
        
   