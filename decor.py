import json

"""var = {
    "first": "jane",
    "last": "Doe",
    "hobbies": ['running', 'football'],

    "children": [
        {
            "fisrt": "alex",
            "age": 5
        },
        {
            "first": "bob",
            "age": 8
        }
    ]

}

personJ = json.dumps(var, indent=3)
print(personJ)

per = json.loads(personJ)
print(per)"""


# Decorators
def start_end_dec(func):
    def wrapper(*args, **kwargs):
        print('start')
        res = func(*args, **kwargs)
        print("end")
        return res

    return wrapper


@start_end_dec  # decorator
def add(x, y):
    return x + y


res = add(20, 10)
print(res)
