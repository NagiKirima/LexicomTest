from pydantic import BaseModel, Field


status_field = Field(default='success')
address_field = Field(min_length=5, max_length=128)
phone_field = Field(pattern=r"^[78][0-9]{10}$")


class ApiKey(BaseModel):
    api_key: str


class WriteData(BaseModel):
    phone: str = phone_field
    address: str = address_field


class Success(BaseModel):
    status: str = status_field


class Address(BaseModel):
    status: str = status_field
    address: str = address_field