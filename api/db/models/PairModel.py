from sqlalchemy import Column, Integer, String


from db import Base


class Pair(Base):
    __tablename__ = "pairs"
    id = Column(Integer, primary_key=True)
    quote = Column(String(length=750), nullable=False, index=True)
    pair = Column(String(length=750), nullable=False, unique=True)
    mcap = Column(Integer(), nullable=False, index=True)
    height = Column(Integer(), nullable=False, index=True)
