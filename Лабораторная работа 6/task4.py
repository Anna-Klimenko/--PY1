import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimeter=',') -> list[dict]:
    list_dict = []

    with open(filename, 'r') as f:
        list_lines = [line.rstrip().split(delimeter) for line in f]
        column = list_lines[0]
        list_value = [value for value in list_lines[1:]]

        for value in list_value:
            dict_ = dict(zip(column, value))
            list_dict.append(dict_)

    return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
