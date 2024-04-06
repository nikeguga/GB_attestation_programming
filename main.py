class Animal:
    def __init__(self, type, name, species, birth_date):
        self.name = name
        self.type = type
        self.species = species
        self.birth_date = birth_date
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def write_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.name},{self.species},{self.birth_date},{','.join(self.commands)}\n")


class Pet(Animal):
    def __init__(self, name, species, birth_date):
        super().__init__(name,'Pet', species, birth_date)


class Dog(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, "Dog", birth_date)


class Cat(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, "Cat", birth_date)


class Hamster(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, "Hamster", birth_date)


class BaggageAnimal(Animal):
    def __init__(self, name, species, birth_date):
        super().__init__(name, "Baggage animal", species, birth_date)


class Horse(BaggageAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, "Horse", birth_date)


class Camel(BaggageAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, "Camel", birth_date)


class Donkey(BaggageAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, "Donkey", birth_date)


class CommandCounter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            # Обработка исключений, если они возникли в блоке try
            print("An exception occurred:", exc_type, exc_value)
        # Дополнительные действия при выходе из блока try
        print("Exiting the context manager")


try:
    with CommandCounter() as counter:
        # Действия, которые могут вызвать исключения
        counter.add()  # Увеличиваем счетчик при заведении нового животного
except Exception as e:
    # Обработка исключений, если они возникли внутри блока try
    print("An exception occurred:", e)
