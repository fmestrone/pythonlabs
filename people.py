people = {}

mike = {
    "name": "Mike",
    "age": 36,
    "email": "mike@youwish.com"
}

mark = {
    "name": "Mark",
    "age": 37,
    "email": "mark@youwish.com"
}

people["mark"] = mark

people["mike"] = mike

people["irina"] = {
        "name": "Irina",
        "age": 25,
        "email": "irina@youwish.com"
    }

otherPeople = {
    "federico": {
        "name": "Federico",
        "age": 35,
        "email": "fed@youwish.com"
    },
    "peter": {
        "name": "Peter",
        "age": 39,
        "email": "peter@youwish.com"
    },
    "martin": {
        "name": "Martin",
        "age": 33,
        "email": "martin@youwish.com"
    }
}

if "peter" in people:
    print(people["peter"]["name"])
else:
    print("There is no Peter")

people.update(otherPeople)

if "peter" in people:
    print(people["peter"]["name"])
else:
    print("There is no Peter")

newInstructors = {
    "peter": {
        "name": "Ken",
        "age": 39,
        "email": "ken@youwish.com"
    }
}

people.update(newInstructors)

if "peter" in people:
    print(people["peter"]["name"])
else:
    print("There is no Peter")

del people["peter"]

if "peter" in people:
    print(people["peter"]["name"])
else:
    print("There is no Peter")

for k, v in people.items():
    print(k, v["name"])
