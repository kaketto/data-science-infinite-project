class CastleKilmereMember:

    location = 'England'
  
    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words: str):
        return f"{self._name} says {words}"

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"

bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')
print(bromley.says('Hello'))

class Pupil(CastleKilmereMember):

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
            'Broomstick Flying': False,
            'Art': False,
            'Magical Theory': False,
            'Foreign Magical Systems': False,
            'Charms': False,
            'Defence Against Dark Magic': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Potions': False,
            'Transfiguration': False
        }

    @staticmethod
    def passed(grade):

        grades = {
                'O': True,
                'Ordinary': True,
                'Pa': True,
                'Passed': True,
                'A': True,
                'Acceptable': True,
                'Po': False,
                'Poor': False,
                'H': False,
                'Horrible': False,
                }
        return grades.get(grade, False)

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")

cleon = Pupil(name='Cleon Bery',
              birthyear=2008,
              sex='male',
              house='House of Courage',
              start_year=2018,
              pet=('Cotton', 'owl'))

print(cleon.says('Hola'))

print(bromley.location)
print(CastleKilmereMember.location)

class Professor(CastleKilmereMember):

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, subject: {self.subject})")

class Ghost(CastleKilmereMember):

        def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house: str = None):
            super().__init__(name, birthyear, sex)
            self.year_of_death = year_of_death
            
            if house is not None:
                self.house = house

        def __repr__(self):
            return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, year of death: {self.year_of_death})")

flynn = Pupil('Flynn Gibbs', 2008, 'male', 'House of Courage', 2018, ('Twiggles', 'owl'))
cassidy = Pupil('Cassidy Ambergem', 2007, 'female', 'House of Courage', 2018, ('Ramses', 'cat'))
mirren = Professor('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')
blade = Professor('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

print(flynn)
print(blade)

def goodbye(function):
    def wrapper(*args, **kwargs):
        original_output = function(*args, **kwargs)
        new_output = original_output + f" Goodbye, have a great day!"
        return new_output
    return wrapper

@goodbye
def say_words(person, words):
    return f"{person} says: {words}"

print(say_words("Cleon", "Hey Flynn!"))