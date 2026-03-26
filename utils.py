from datetime import datetime, timedelta

def get_due_date():
    return (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

def calculate_fine(due_date):
    today = datetime.now()
    due = datetime.strptime(due_date, "%Y-%m-%d")

    if today > due:
        days = (today - due).days
        return days * 5
    return 0