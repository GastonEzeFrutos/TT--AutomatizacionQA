import csv
import json

def read_users_csv():
    with open("data/users.csv", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

data = read_users_csv()
print(data)