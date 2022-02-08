from datetime import date
from datetime import datetime
from optparse import Option
from typing import Optional

from pydantic import BaseModel

class WaybillBase(BaseModel):
    number: Optional[int] = None
    date_posted: Optional[date] = datetime.now().date()
    comment: Optional[str] = None
    status: Optional[str] = None

#this will be used to validate data while creating a Waybill
class WaybillCreate(WaybillBase):
    number : int
    status : str 
    type : str
    comment : str 
    
#this will be used to format the response to not to have id,owner_id etc
class ShowWaybill(WaybillBase):
    number : str 
    status: str 
    date_posted : date
    comment : Optional[str]

    class Config():  #to convert non dict obj to json
        orm_mode = True