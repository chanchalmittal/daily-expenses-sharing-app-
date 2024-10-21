import pandas as pd
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import crud

def generate_balance_sheet(db: Session):
    expenses = crud.get_all_expenses(db)
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found.")
    
    data = []
    for expense in expenses:
        data.append({
            "Expense ID": expense.id,
            "Total Amount": expense.total_amount,
            "Exact Amounts": expense.exact_amounts,
            "Percentages": expense.percentages,
        })
    
    df = pd.DataFrame(data)
    return df
