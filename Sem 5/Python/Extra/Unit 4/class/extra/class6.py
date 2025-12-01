import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Rajesh",
    "Sharma",
    datetime.date(1983, 2, 13), # year, month, day
    "No.1, C.G. Road, Ahmedabad",
    "555 456 0987",
    "info@example.com"
)

print(person.name)
print(person.email)
print(person.age())








