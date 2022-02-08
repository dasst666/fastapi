from db.models.waybills import Waybill
from schemas.waybills import WaybillCreate
from sqlalchemy.orm import Session



def create_new_waybill(waybill: WaybillCreate,db: Session,user_id:int):
    waybill_object = Waybill(**waybill.dict(),user_id=user_id)
    db.add(waybill_object)
    db.commit()
    db.refresh(waybill_object)
    return waybill_object