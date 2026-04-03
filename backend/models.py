from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    amount: float
    merchant: str
    category: str
    type: str
    timestamp: datetime