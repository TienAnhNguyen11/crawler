from fastapi import APIRouter
from typing import Union
from db.session import myDB
from schemas.api_response import dataEntity
from services.services import get_daily_price, get_realtime_price


router = APIRouter()


@router.get("/get_list_area")
async def get_list_area():
    return myDB['area'].find({})


@router.get("/get_list_type")
async def get_list_type(area):
    return get_list_area


@router.get("/get_daily_price")
async def get_daily_price(from_date: Union[str, None], to_date: Union[str, None], type_: Union[str, None] = None,
                    area: Union[str, None] = None):
    return get_daily_price


@router.get("/get_realtime_price")
async def get_realtime_price(from_date: Union[str, None], to_date: Union[str, None], type_: Union[str, None] = None):
    return get_realtime_price