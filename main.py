import pandas as pd
import csv
from  datetime import datetime

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

CSV.intialize_csv()
CSV.add_entry("20-07-2024",12000,"Income","Salary")






