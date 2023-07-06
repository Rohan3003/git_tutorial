from jsondiff import diff
import json

def read_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

file1_path = "file1.json"
file2_path = "file2.json"

file1_data = read_json(file1_path)
file2_data = read_json(file2_path)


diff_result = diff(file1_data, file2_data)

if not diff_result:
    print("The JSON files are identical.")
else:
    print("The JSON files are different.")
    print(diff_result)