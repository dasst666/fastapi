from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from apis.version1.route_login import get_current_user_from_token

from db.session import get_db
from db.models.waybills import Waybill
from schemas.waybills import WaybillCreate,ShowWaybill
from db.repository.waybills import create_new_waybill
from db.models.users import User

router = APIRouter()


@router.post("/create-waybill/",response_model=ShowWaybill)
def create_waybill(
    waybill: WaybillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    waybill = create_new_waybill(waybill=waybill,db=db,user_id=current_user.id)
    return waybill