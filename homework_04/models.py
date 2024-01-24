"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost:5432/postgres"
engine = create_async_engine(PG_CONN_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="", server_default="")
    username = Column(String, nullable=False, default="", server_default="")
    email = Column(String, nullable=False, default="", server_default="")
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")
    user = relationship("User", back_populates="posts")


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def fill_users_table(users_data):
    async with Session() as session:
        session: AsyncSession
        async with session.begin():
            for user_ in users_data:
                user_added = User(name=user_['name'], username=user_['username'], email=user_['email'])
                session.add(user_added)

                
async def fill_posts_table(posts_data):
    async with Session() as session:
        session: AsyncSession
        async with session.begin():
            for post_ in posts_data:
                post_added = Post(user_id=post_['userId'], title=post_['title'], body=post_['body'])
                session.add(post_added)

