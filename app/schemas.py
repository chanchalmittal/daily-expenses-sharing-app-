from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    email: str
    mobile_number: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    expenses: List["Expense"] = []

    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    total_amount: float
    exact_amounts: Optional[List[float]] = None
    percentages: Optional[List[float]] = None

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
