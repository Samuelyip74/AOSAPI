import json

json_string = '{ "1":"Red", "2":"Blue", "3":"Green"}'

parsed_json = json.loads(json_string)

print(parsed_json['1'])