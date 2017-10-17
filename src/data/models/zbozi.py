from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Zbozi(CRUDModel):
    __tablename__ = 'zbozi'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    nazev = Column(String(64), nullable=False, unique=True, index=True, doc="Nazev zbozi.")
    cena = Column(Float, nullable=True, default=0)
    vyrazeno = Column(Boolean(name="Vyrazen"), default=False)
    kusu = Column(Integer, nullable=False, index=False)


    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

