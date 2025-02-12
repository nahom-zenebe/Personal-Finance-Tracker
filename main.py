import pandas as pd
import csv
from  datetime import datetime
from data_entry import get_amount,get_category,get_date,get_description

class CSV:
    CSV_FILE="finance_data.csv"
    COLUMNS = ["data", "amount", "category", "description"]

    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS )
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,data,amount,category,description):
        new_entry={
            "data":data,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("enrty add successfully")


def add():
    CSV.intialize_csv()
    date=get_date("Enter the date of the transaction (dd-mm-yyy) or enter for today's date ",allow_default=True)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)
add()










