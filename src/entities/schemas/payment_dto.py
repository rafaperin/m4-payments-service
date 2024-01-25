import datetime
import uuid
from typing import List

from src.utils.utils import CamelModel


class PaymentDTO(CamelModel):
    order_id: uuid.UUID
    creation_date: datetime.datetime
    payment_status: str

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
                "creation_date": "2024-01-01T00:05:23",
                "payment_status": "Confirmado"
            }
        }


class CreatePaymentDTO(CamelModel):
    order_id: uuid.UUID

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
            }
        }


class RemovePaymentDTO(CamelModel):
    order_id: uuid.UUID

    class Config:
        schema_extra = {
            "example": {
                "order_id": "00000000-0000-0000-0000-000000000000",
            }
        }


class PaymentDTOResponse(CamelModel):
    result: PaymentDTO


class PaymentDTOListResponse(CamelModel):
    result: List[PaymentDTO]
