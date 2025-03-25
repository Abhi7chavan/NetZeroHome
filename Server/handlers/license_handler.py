from fastapi import APIRouter,Depends
from sqlalchemy.orm import  Session
from configuration.database import get_db
from models.license import licenseschema
from services.license_service import LicenseService

license_router = APIRouter(prefix='/license',tags=['/license'])
license_service = LicenseService()


@license_router.post('/create')
async def create_license(userdata:licenseschema,db:Session=Depends(get_db)):
    if userdata:
        return await license_service.Create(userdata,db)
    l