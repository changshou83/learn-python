from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from app.api.deps import SessionDep
from app.core.security import create_access_token, verify_password
from app.db.models import User
from app.schemas import Token

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    db: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = db.scalar(select(User).where(User.email == form_data.username))
    if user is None or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials",
        )

    access_token = create_access_token({"user_id": user.id})
    return Token(access_token=access_token, token_type="bearer")

