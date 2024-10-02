#contact management list

import json

names=[]
ages=[]
emails=[]
people=[]


def add_person():
    name=input("name :")
    age=input("Age: ")
    email=input("email :")

    person = {"name": name, "age": age, "email": email}
    return person

def display_people(people):
    for i,person in enumerate(people):
        print(i+1,"-",person["name"],"|",person["age"],"|",person["email"])


def delete_contact(people):
    display_people(people)

    while True:
        number=input("enter a number to delete: ")
        try:
            number=int(number)
            if number<=0 or number>len(people):
                print("invalid number,out of the range")
            else:
                break
        except:
            print("Invalid Number")

    people.pop(number-1)
    print("Person is deleted")


def search(people):
    search_name=input("search for a name: ").lower()
    result=[]

    for person in people:
        name=person["name"]
        if search_name in name.lower():
            result.append(person)

    display_people(result)

print()
print("Hi,Welcome to the contact management system")
print("...........................................")
print()

#

while True:

    print("Contact list size",len(people))
    command = input("You can 'Add','Delete' or 'Search' and 'Q'for quit ").lower()
    if command=="add":
        person=add_person()
        people.append(person)
        print("person is added!")
    elif command=="delete":
        delete_contact(people)
    elif command=="search":
       search(people)
    elif command=="q":
        break
    else:
        print("Invalid command")


print(person)