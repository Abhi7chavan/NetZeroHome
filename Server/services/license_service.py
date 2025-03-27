from sqlalchemy.orm import Session
from models.license import License
from models.users import Users,UserSchema
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
            new_users = await self.user_service.create_user(new_license,db)
            return new_users

        except Exception as e:
            db.rollback()
            return {'message':str(e),'status_code':400}
        
        
    async def Update(self,licensedata,license_id,db):
        try:
            existing_license = db.query(License).filter(License.license_id ==license_id).first()
            if not existing_license:
                return {'staus_code':404,'message':'record not found'}
            
            update_license = licensedata.dict(exclude_unset=True)
            if update_license:
                for key,value in update_license.items():
                    setattr(existing_license,key,value)
                db.commit()
                
            #update user of that license
            get_user = db.query(Users).filter(Users.license_id == license_id).first()
         
            if get_user:
                for key,value in update_license.items():
                    setattr(get_user,key,value)
                    
            db.commit()
                
                
            return update_license 
                    
        except Exception as e:
            db.rollback()
            return {'message':e}