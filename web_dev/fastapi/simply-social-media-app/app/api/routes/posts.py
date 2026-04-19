from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlalchemy import func, select

from app.api.deps import CurrentUser, SessionDep
from app.db.models import Post, Vote
from app.schemas import PostCreate, PostOut, PostRead, PostUpdate

router = APIRouter(prefix="/posts", tags=["Posts"])


def build_post_out(post: Post, votes: int) -> PostOut:
    return PostOut(Post=PostRead.model_validate(post), votes=votes)


@router.get("/", response_model=list[PostOut])
def get_posts(
    db: SessionDep,
    current_user: CurrentUser,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    skip: Annotated[int, Query(ge=0)] = 0,
    search: str = "",
) -> list[PostOut]:
    del current_user
    stmt = (
        select(Post, func.count(Vote.post_id).label("votes"))
        .join(Vote, Vote.post_id == Post.id, isouter=True)
        .where(Post.title.contains(search))
        .group_by(Post.id)
        .limit(limit)
        .offset(skip)
    )
    rows = db.execute(stmt).all()
    return [build_post_out(post, votes) for post, votes in rows]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostRead)
def create_post(
    post_in: PostCreate,
    db: SessionDep,
    current_user: CurrentUser,
) -> Post:
    post = Post(owner_id=current_user.id, **post_in.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: SessionDep, current_user: CurrentUser) -> PostOut:
    del current_user
    stmt = (
        select(Post, func.count(Vote.post_id).label("votes"))
        .join(Vote, Vote.post_id == Post.id, isouter=True)
        .where(Post.id == post_id)
        .group_by(Post.id)
    )
    row = db.execute(stmt).first()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {post_id} was not found",
        )
    post, votes = row
    return build_post_out(post, votes)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: SessionDep, current_user: CurrentUser) -> Response:
    post = db.get(Post, post_id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {post_id} does not exist",
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{post_id}", response_model=PostRead)
def update_post(
    post_id: int,
    post_in: PostUpdate,
    db: SessionDep,
    current_user: CurrentUser,
) -> Post:
    post = db.get(Post, post_id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {post_id} does not exist",
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    for field, value in post_in.model_dump().items():
        setattr(post, field, value)

    db.commit()
    db.refresh(post)
    return post

