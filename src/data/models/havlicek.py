from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Ukol(CRUDModel):
    __tablename__ = 'ukol'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    jmeno = Column(String(64), nullable=False, unique=True, index=True, doc="Jmeno.")
    prijmeni = Column(String(64), nullable=False, unique=True, index=True, doc="Prijmeni.")
    datum = Column(String(64), nullable=False, unique=True, index=True, doc="Datum narozeni(dd(d)mm(m)yyyy(y).")

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

