from sqlalchemy import Column, Integer, String, LargeBinary, BigInteger

from db import Base


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    addr = Column(String(length=750), nullable=False, unique=True, index=True)
    name = Column(String(length=750), nullable=False)
    symbol = Column(String(length=750), nullable=False)
    decimals = Column(Integer())
    age = Column(BigInteger(), index=True)
    logo = Column(LargeBinary())
