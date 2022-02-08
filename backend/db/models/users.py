from db.base_class import Base
from sqlalchemy import Boolean, ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner")

    waybills = relationship("Waybill", back_populates="user")
    
    # waybill_id = Column(Integer, ForeignKey("waybill_id"))
    # waybill = relationship("Waybill", back_populates="users")

