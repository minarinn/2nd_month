class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = "имею высшее образование" if self.higher_education else "не имею высшего образования"
        print(f"Меня зовут {self.name}. Я родился(-ась) {self.birth_date}. "
              f"Я работаю как {self.occupation} и {education_status}.")

class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Даши, "
              f"я родился {self.birth_date}, работаю {self.occupation}.")

class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Даши, "
              f"я родился {self.birth_date}, работаю {self.occupation}.")

friend1 = Friend(name="Айдана", birth_date="02.06.2006", occupation="психолог", higher_education=True)
friend2 = Friend(name="Рамиль", birth_date="18.09.2007", occupation="инженер", higher_education=True)

classmate1 = Classmate(name="Жасмин", birth_date="22.12.2006", occupation="дизайнер", higher_education=False)
classmate2 = Classmate(name="Эрлан", birth_date="04.04.2006", occupation="медик", higher_education=True)

friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()
