import copy
import json
from typing import Optional

from credentials import DATABASE_CONFIG
from db_client import PostgresClient
from datetime import datetime
import time
from sys import argv


def load_json_file(file_name) -> list[dict] | None:
    utc = datetime.utcfromtimestamp(time.time())

    with open(file_name) as file:
        data = json.load(file)
    for item in data:
        item['create_at'] = utc
    return data


def save_json_file(file_name: str, data):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def get_table_name(file_name: str) -> str:
    name = file_name.split(".")
    return name[0]


def _insert(client: PostgresClient, table_name: str, data: dict):
    client.insert(table_name=table_name, data=data)


def _select(client: PostgresClient, table_name):
    return client.select(table_name=table_name)


def create_riddle_dump(data: Optional[list]):
    temp = {
        "text": "",
        "answer": "",
        "category": 100,
        "create_at": "CURRENT_TIMESTAMP",
        "riddle_type": 100,
        "riddle_age": 800
    }
    result = []
    if data:
        for item in data:
            temp['text'] = item[1]
            temp['answer'] = item[2]
            result.append(copy.deepcopy(temp))
        return result
    else:
        return result.append(temp)


def main():
    file_name = argv[1]
    data = load_json_file(file_name)
    table_name = get_table_name(file_name)
    client = PostgresClient(DATABASE_CONFIG)
    dump = create_riddle_dump(_select(client=client, table_name=table_name))
    save_json_file("fiddles_dump.json", dump)


if __name__ == '__main__':
    main()

