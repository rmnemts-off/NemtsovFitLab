import pytest

@pytest.mark.asyncio
async def test_muscle_groups_requires_auth(client):
    response = await client.get("/api/v1/exercises/muscle-groups")
    assert response.status_code == 403
