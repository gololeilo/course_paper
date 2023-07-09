import json
from datetime import datetime
def get_data():
    with open('operations.json') as json_file:
        return json.load(json_file)

def get_filtered_data(data):
    new_data = []
    for transaction in data:
        if transaction['state'] == 'EXECUTED':
            new_data.append(transaction)
    return new_data

def get_sorted_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

def get_formatted(data):
    date_transaction = datetime.strptime(data[0]['date'], "%Y-%m-%dT%H:%M:%S.%f")
    date_transaction = date_transaction.strftime("%d.%m.%Y")
    print(date_transaction)
    """
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
    """