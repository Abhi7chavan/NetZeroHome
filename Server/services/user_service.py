from models.users import Users

class UserService:
    async def create_user(self,userdata,db):
        
        if userdata:
            try:
                new_user = Users(license_id=userdata.license_id,username=userdata.username,email=userdata.email,password=userdata.password,location=userdata.location,features=userdata.features,HouseholdItems=userdata.HouseholdItems,SensorCount=userdata.SensorCount)
                
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
                
                return new_user
            except Exception as e:
                db.rollback()
                return {'message':str(e),'status_code':400}
            
        