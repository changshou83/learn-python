from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import PyJWTError, decode_access_token, oauth2_scheme
from app.db.models import User
from app.db.session import get_db
from app.schemas import TokenPayload

SessionDep = Annotated[Session, Depends(get_db)]


def get_current_user(
    db: SessionDep,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenPayload(user_id=int(user_id))
    except (PyJWTError, ValueError):
        raise credentials_exception

    user = db.scalar(select(User).where(User.id == token_data.user_id))
    if user is None:
        raise credentials_exception
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]

