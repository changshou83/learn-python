from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.api.deps import CurrentUser, SessionDep
from app.db.models import Post, Vote
from app.schemas import Message, VoteAction

router = APIRouter(prefix="/vote", tags=["Vote"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Message)
def vote(
    vote_in: VoteAction,
    db: SessionDep,
    current_user: CurrentUser,
) -> Message:
    post = db.get(Post, vote_in.post_id)
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {vote_in.post_id} does not exist",
        )

    existing_vote = db.scalar(
        select(Vote).where(
            Vote.post_id == vote_in.post_id,
            Vote.user_id == current_user.id,
        )
    )

    if vote_in.dir == 1:
        if existing_vote is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has already voted on post {vote_in.post_id}",
            )
        db.add(Vote(post_id=vote_in.post_id, user_id=current_user.id))
        db.commit()
        return Message(message="successfully added vote")

    if existing_vote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vote does not exist",
        )

    db.delete(existing_vote)
    db.commit()
    return Message(message="successfully deleted vote")

