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

person1 = Person("Туратов Асанбек", "14 февраля 2007", "кинолог", False)
person2 = Person("Ли Дарья", "19 апреля 2006", "флорист", True)
person3 = Person("Чолпонкулов Байэл", "30 апреля 2006", "репетитор", True)

person1.introduce()
person2.introduce()
person3.introduce()
