from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from settings import settings


api_key_header = APIKeyHeader(name="ApiKey")


def api_key_auth(api_key: str = Depends(api_key_header)):
    '''Check api key in request Headers'''
    if api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Missing or invalid ApiKey"
        )