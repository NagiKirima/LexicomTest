from fastapi import APIRouter, HTTPException, status, Depends, Query
import aioredis

from depends import api_key_auth
from database import get_redis_connection
from settings import settings
from schemas import ApiKey, WriteData, Success, Address


router = APIRouter(
    prefix='/api',
    tags=['Test API']
)


@router.get('/key', response_model=ApiKey)
async def get_api_key():
    """Get API key"""

    return ApiKey(api_key=settings.api_key)


@router.get('/check_data', dependencies=[Depends(api_key_auth)], response_model=Address)
async def check_data(
    phone: str = Query(regex=r"^[78][0-9]{10}$", title="Phone number", description="Need to get data"),
    redis: aioredis.Redis = Depends(get_redis_connection)
):
    """Check data by phone number"""
     
    address = await redis.get(name=phone)

    if address is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Phone not found')

    return Address(address=address)


@router.post('/write_data', dependencies=[Depends(api_key_auth)], response_model=Success)
async def write_data(
    data: WriteData,
    redis: aioredis.Redis = Depends(get_redis_connection)
):
    """Write data to Redis"""
    
    result = await redis.set(name=data.phone, value=data.address, nx=True)

    if result is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Phone already registered')

    return Success()


@router.patch('/write_data', dependencies=[Depends(api_key_auth)], response_model=Success)
async def patch_data(
    data: WriteData,
    redis: aioredis.Redis = Depends(get_redis_connection)
):
    """Patch data in Redis"""
    
    result = await redis.set(name=data.phone, value=data.address, xx=True)

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Phone not found')

    return Success()