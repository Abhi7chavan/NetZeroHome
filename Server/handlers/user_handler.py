from fastapi import APIRouter


user_router = APIRouter(prefix='/users',tags=['/users'])


@user_router.get('')
def get_user():
    try:
        result =10/0
        return result
    
    except Exception as e:
        raise e
        
   