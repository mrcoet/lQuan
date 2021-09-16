from typing import List

from sqlalchemy import update, delete
from sqlalchemy.future import select

from db.models.PairModel import Pair

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from keys import db_username, db_password, db_name


DATABASE_URL = f"postgresql+asyncpg://{db_username}:{db_password}@localhost:5432/{db_name}"

from db import Base


class PairDAL:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL)  # future=True
        self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def add_pair(self, quote: str, pair: str, mcap: int, height: int):
        """
        Add New pair to Pair Table in lQuan Database
        """
        async with self.async_session() as session:
            async with session.begin():  # Don't need to commit
                new_token = Pair(quote=quote, pair=pair, mcap=mcap, height=height)
                session.add(new_token)

    async def show_Pair(self, page: int = 0, many: int = 40) -> List[Pair]:
        """
        Show Tokens in Token Table in lQuan Database
        """

        async with self.async_session() as session:
            async with session.begin():
                q = await session.execute(select(Pair).order_by(Pair.mcap.desc()).limit(many).offset(int(page * many)))
                return q.scalars().all()

    async def one_pair(self, pair: str):
        """
        Show One Tokens in Token Table in lQuan Database
        """

        async with self.async_session() as session:
            async with session.begin():
                q = await session.execute(select(Pair).filter_by(pair=pair))
                return q.scalars().first()

    async def delete_pair(self, pair: str):
        """
        Delete One Token in Token Table in lQuan Database
        """

        async with self.async_session() as session:
            async with session.begin():
                q = delete(Pair).where(Pair.pair == pair)
                await session.execute(q)

    async def build_table(self):

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
