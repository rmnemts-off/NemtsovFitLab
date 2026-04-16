import hashlib
import hmac
from urllib.parse import parse_qsl, unquote

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import settings

security = HTTPBearer()


def validate_init_data(init_data_raw: str) -> dict:
    """Validate Telegram Mini App initData HMAC signature."""
    parsed = dict(parse_qsl(unquote(init_data_raw), keep_blank_values=True))
    received_hash = parsed.pop("hash", None)
    if not received_hash:
        raise ValueError("Missing hash")

    data_check_string = "\n".join(
        f"{k}={v}" for k, v in sorted(parsed.items())
    )
    secret_key = hmac.new(
        b"WebAppData", settings.bot_token.encode(), hashlib.sha256
    ).digest()
    expected_hash = hmac.new(
        secret_key, data_check_string.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_hash, received_hash):
        raise ValueError("Invalid hash")

    return parsed


async def get_current_telegram_id(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> int:
    scheme, token = credentials.scheme, credentials.credentials
    if scheme.lower() != "tma":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        data = validate_init_data(token)
        import json
        user = json.loads(data["user"])
        return int(user["id"])
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
