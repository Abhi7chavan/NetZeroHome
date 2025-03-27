from models.users import Users
from services.role_service import Roleservice
class UserService:
    def __init__(self):
        self.roleservice = Roleservice()
    async def create_user(self,userdata,db):
        if userdata:
            try:
                get_roles = self.roleservice.get_role(db)
                admin_user = Users(license_id=userdata.license_id,username=userdata.username,email=userdata.email,password=userdata.password,location=userdata.location,features=userdata.features,HouseholdItems=userdata.HouseholdItems,SensorCount=userdata.SensorCount,role_id=get_roles[0]['role_id'])

                
                db.add(admin_user)
                db.commit()
                db.refresh(admin_user)
                
                return admin_user
            except Exception as e:
                db.rollback()
                return {'message':str(e),'status_code':400}
            
            
            
        