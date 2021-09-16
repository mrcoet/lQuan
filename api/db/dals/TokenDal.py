from typing import List, Optional, ByteString


from sqlalchemy import update, delete
from sqlalchemy.future import select


from db.models.TokenModel import Token


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


from keys import db_username, db_password, db_name

DATABASE_URL = f"postgresql+asyncpg://{db_username}:{db_password}@localhost:5432/{db_name}"

from db import Base


class TokenDAL:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL)  # future=True
        self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def add_token(self, addr: str, name: str, symbol: str, decimals: Optional[int], age: Optional[int], logo: Optional[ByteString]):
        """
        Add New toekn to Token Table in lQuan Database
        """
        async with self.async_session() as session:
            async with session.begin():  # Don't need to commit
                new_token = Token(addr=addr, name=name, symbol=symbol, decimals=decimals, age=age, logo=logo)
                session.add(new_token)

    async def show_Token(self, page: Optional[int] = 0, many: Optional[int] = 100) -> List[Token]:
        """
        Show Token in Token Table in lQuan Database
        """

        async with self.async_session() as session:
            async with session.begin():
                q = await session.execute(select(Token).order_by(Token.age).limit(many).offset(int(page * many)))
                return q.scalars().all()

    async def one_token(self, addr: str):
        """
        Show One Token in Token Table in lQuan Database
        """

        async with self.async_session() as session:
            async with session.begin():
                q = await session.execute(select(Token).filter_by(addr=addr))
                return q.scalars().first()

    async def delete_token(self, addr: str):
        """
        Delete One Token in Token Table in lQuan Database
        """

        async with self.async_session() as session:
            async with session.begin():
                q = delete(Token).where(Token.addr == addr)
                await session.execute(q)

    async def build_table(self):

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
