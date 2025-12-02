import json
from pathlib import Path

from src.lab05.json_csv import json_to_csv, csv_to_json

current_directory_path = Path(__file__).parent.parent
root_directory_path = current_directory_path.parent.parent
samples_directory_path = f"{root_directory_path}/data/samples"


def test_json_to_csv_ok(tmp_path):
    people_json_path = f"{samples_directory_path}/people.json"
    output_csv_path = f"{tmp_path}/people.csv"
    json_to_csv(people_json_path, output_csv_path)
    with open(people_json_path) as people_json_file:
        people_json = json.load(people_json_file)  # list of dicts
    with open(output_csv_path) as output_csv_file:
        output_csv_list = output_csv_file.readlines()
    header_line_str = output_csv_list[0].rstrip("\n\r")
    splitted_headers = header_line_str.split(",")
    headers_set = set(splitted_headers)
    json_keys_set = set(people_json[0].keys())
    assert headers_set == json_keys_set
    assert len(output_csv_list) == len(people_json) + 1  # +1 for header


def test_json_to_csv_file_not_found():
    not_existing_json_path = f"{samples_directory_path}/not_existing_file.json"
    output_csv_path = "output.csv"
    try:
        json_to_csv(not_existing_json_path, output_csv_path)
    except FileNotFoundError as e:
        assert str(e) == f"Файл не найден: {not_existing_json_path}"
    else:
        assert False, "Expected FileNotFoundError was not raised"


def test_json_to_csv_input_file_not_json(tmp_path):
    invalid_json_path = f"{samples_directory_path}/people.csv"
    output_csv_path = f"{tmp_path}/output.csv"
    try:
        json_to_csv(invalid_json_path, output_csv_path)
    except ValueError as e:
        assert str(e) == "Неверный тип файла, ожидается JSON файл"
    else:
        assert False, "Expected ValueError was not raised"


def test_csv_to_json_ok(tmp_path):
    people_csv_path = f"{samples_directory_path}/people.csv"
    output_json_path = f"{tmp_path}/people.json"
    csv_to_json(people_csv_path, output_json_path)
    with open(people_csv_path) as people_csv_file:
        people_csv = people_csv_file.readlines()
    with open(output_json_path) as output_json_file:
        output_json = json.load(output_json_file)  # list of dicts
    header_line_str = people_csv[0].rstrip("\n\r")
    splitted_headers = header_line_str.split(",")
    headers_set = set(splitted_headers)
    json_keys_set = set(output_json[0].keys())
    assert headers_set == json_keys_set
    assert len(output_json) == len(people_csv) - 1  # -1 for header


def test_csv_to_json_file_not_found():
    not_existing_csv_path = f"{samples_directory_path}/not_existing_file.csv"
    output_json_path = "output.json"
    try:
        csv_to_json(not_existing_csv_path, output_json_path)
    except FileNotFoundError as e:
        assert str(e) == f"Файл не найден: {not_existing_csv_path}"
    else:
        assert False, "Expected FileNotFoundError was not raised"


# входной файл не csv формата → ожидаем ValueError;
def test_csv_to_json_input_file_not_csv(tmp_path):
    invalid_csv_path = f"{samples_directory_path}/people.json"
    output_json_path = f"{tmp_path}/output.json"
    try:
        csv_to_json(invalid_csv_path, output_json_path)
    except ValueError as e:
        assert str(e) == "Неверный тип файла, ожидается CSV файл"
    else:
        assert False, "Expected ValueError was not raised"