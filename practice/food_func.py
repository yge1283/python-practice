
import json
from tabulate import tabulate

# 파일 이름 설정
file = "foodlist.json"

def save_data(data):
    with open(file, "w") as f:
        json.dump(data, f)

def load_data():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

