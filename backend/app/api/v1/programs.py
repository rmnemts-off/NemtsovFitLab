from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_session
from app.models.user import User
from app.schemas.program import ProgramSchema
from app.services import program_service

router = APIRouter()


@router.get("/", response_model=list[ProgramSchema])
async def get_programs(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """Return all available programs (for the Shop tab)."""
    return await program_service.get_all_programs(session)
