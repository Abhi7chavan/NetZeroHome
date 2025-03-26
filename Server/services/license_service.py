from sqlalchemy.orm import Session
from models.license import License
from models.users import Users
from services.user_service import UserService 

class LicenseService:
    def __init__(self):
        self.user_service = UserService()
    async def Create(self, userdata: dict, db: Session):
        try:
            new_license = License(**userdata.dict())
            db.add(new_license)
            db.commit()
            #add user
            new_user = await self.user_service.create_user(new_license,db)
            return new_user

        except Exception as e:
            db.rollback()
            return {'message':str(e),'status_code':400}