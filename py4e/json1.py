import json

input = """
[
    {
        "id":"001",
        "x":"2",
        "name":"chuck"
    },
    {
        "id":"002",
        "x":"7",
        "name":"Meow"
    }
]"""

persons = json.loads(input)

for person in persons:
    print('id', person['id'])
    print('x', person['x'])
    print('name', person['name'])