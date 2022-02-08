from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from db.models.users import User

class Waybill(Base):
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    date_posted = Column(Date)
    status = Column(String)
    type = Column(String)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="waybills")

    # person_id = Column(Integer, ForeignKey(User.id))

    # users = relationship("User", back_populates="waybill")