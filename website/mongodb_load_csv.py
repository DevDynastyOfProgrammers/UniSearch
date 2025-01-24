import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/project")
db = client["project"]
collection = db["project"]

df = pd.read_csv("web-uni/universitetiFINAL.csv", sep=",", encoding="utf-8")

collection.insert_many(df.to_dict(orient="records"))

print("Данные успешно загружены в MongoDB!")