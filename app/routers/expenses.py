from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, user_id: int, db: Session = Depends(get_db)):
    total_amount = expense.total_amount
    exact_amounts = expense.exact_amounts
    percentages = expense.percentages

    # Validate inputs
    if percentages and sum(percentages) != 100:
        raise HTTPException(status_code=400, detail="Percentages must sum up to 100.")
    
    if exact_amounts and len(exact_amounts) < 1:
        raise HTTPException(status_code=400, detail="At least one exact amount must be provided.")

    return crud.add_expense(db=db, expense=expense, user_id=user_id)

@router.get("/expenses/user/{user_id}", response_model=list[schemas.Expense])
def read_user_expenses(user_id: int, db: Session = Depends(get_db)):
    expenses = crud.get_user_expenses(db=db, user_id=user_id)
    return expenses

@router.get("/expenses/", response_model=list[schemas.Expense])
def read_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db=db)
