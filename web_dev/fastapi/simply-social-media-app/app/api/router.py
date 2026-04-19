from fastapi import APIRouter

from app.api.routes import auth, posts, users, votes


api_router = APIRouter()
api_router.include_router(posts.router)
api_router.include_router(users.router)
api_router.include_router(auth.router)
api_router.include_router(votes.router)

