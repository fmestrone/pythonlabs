people = {}

key = input("Key for next person: ")
name = input("Name for %s: " % key)
age = int(input("Age for %s: " % key))
email = input("Email for %s: " % key)

nextPerson = {
    "name": name,
    "age": age,
    "email": email
}

people[key] = nextPerson

print(people)

print(people[key]['age'])

