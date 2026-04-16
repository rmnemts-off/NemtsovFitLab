from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.program import Program
from app.schemas.program import ProgramSchema


async def get_all_programs(session: AsyncSession) -> list[ProgramSchema]:
    result = await session.execute(select(Program).order_by(Program.name))
    programs = result.scalars().all()
    return [ProgramSchema.model_validate(p) for p in programs]
