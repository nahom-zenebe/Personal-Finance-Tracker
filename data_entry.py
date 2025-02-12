from datetime import datetime

data_format="%d-%m-%Y"
CATEGORIES={"I":"Income","E":"Expense"}
def get_date(prompt,allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return  datetime.today().strftime(data_format)
    try:
        valid_date=datetime.strptime(date_str,data_format)
        return valid_date.strftime(data_format)
    except ValueError:
        print('Please enter a valid date in this format dd-mm-yy')
        return get_date(prompt,allow_default)
def get_amount():
    try:
        amount = float(input("Enter the amount:"))
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category('I' for Income or 'E' for Expense):").upper()
    if category  in CATEGORIES:
        return CATEGORIES[category]


    print("Please enter a valid category, please entry ('I' for Income or 'E' for Expense)")
    return get_category()


def get_description():
    return input("Enter the description:")

