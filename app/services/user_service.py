from typing import Optional, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload
from app.models.user_model import User
from app.utils.security import hash_password
from uuid import UUID
import logging

logger = logging.getLogger(__name__)

class UserService:
    @classmethod
    async def _execute_query(cls, session: AsyncSession, query):
        """Helper method to execute query with error handling."""
        try:
            result = await session.execute(query)
            return result
        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            await session.rollback()
            return None

    @classmethod
    async def _fetch_one(cls, session: AsyncSession, model, **filters) -> Optional[User]:
        """Generic method to fetch a single record based on filters."""
        query = select(model).filter_by(**filters)
        result = await cls._execute_query(session, query)
        return result.scalars().first() if result else None

    @classmethod
    async def get_by_id(cls, session: AsyncSession, user_id: UUID) -> Optional[User]:
        """Fetch a user by ID without relationships."""
        return await cls._fetch_one(session, User, id=user_id)

    @classmethod
    async def get_by_username(cls, session: AsyncSession, username: str) -> Optional[User]:
        return await cls._fetch_one(session, User, username=username)

    @classmethod
    async def get_by_email(cls, session: AsyncSession, email: str) -> Optional[User]:
        return await cls._fetch_one(session, User, email=email)

    @classmethod
    async def create(cls, session: AsyncSession, user_data: Dict) -> Optional[User]:
        """Create a new user with the given data."""
        try:
            if 'password' in user_data:
                user_data['hashed_password'] = hash_password(user_data.pop('password'))
            user = User(**user_data)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
        except SQLAlchemyError as e:
            logger.error(f"Failed to create user {user_data.get('username', '')}: {e}")
            await session.rollback()
            return None

    @classmethod
    async def update(cls, session: AsyncSession, user_id: UUID, update_data: Dict[str, str]) -> Optional[User]:
        """Update an existing user's information."""
        try:
            user = await cls.get_by_id(session, user_id)
            if user:
                for key, value in update_data.items():
                    setattr(user, key, value)
                await session.commit()
                await session.refresh(user)
                return user
            return None
        except SQLAlchemyError as e:
            logger.error(f"Failed to update user {user_id}: {e}")
            await session.rollback()
            return None

    @classmethod
    async def delete(cls, session: AsyncSession, user_id: UUID) -> bool:
        """Delete a user by ID."""
        try:
            user = await cls.get_by_id(session, user_id)
            if user:
                await session.delete(user)
                await session.commit()
                return True
            else:
                logger.info(f"User {user_id} not found for deletion.")
                return False
        except SQLAlchemyError as e:
            logger.error(f"Failed to delete user {user_id}: {e}")
            await session.rollback()
            return False
