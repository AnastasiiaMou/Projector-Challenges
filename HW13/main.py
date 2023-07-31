# Task 1 & Task 2


class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other):
        combined_name = f"{self.name} - {other.name}"
        combined_population = self.population + other.population
        return Country(combined_name, combined_population)

    def __repr__(self) -> str:
        return f"Country name = '{self.name}', population = {self.population})"


bosnia = Country("Bosnia", 10_000_000)
herzegovina = Country("Herzegovina", 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# Task 3
class Car:
    def __init__(self, brand, model, year, speed) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5


subaru = Car("Subaru", "Forester", 2003, 0)
print(subaru.model)
print(subaru.year)
subaru.brake()


# Task 4
class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "left":
            self.position_x -= steps
        elif self.orientation == "right":
            self.position_x += steps
        elif self.orientation == "up":
            self.position_y += steps
        elif self.orientation == "down":
            self.position_y -= steps

    def turn(self, direction):
        if direction == "left":
            orientations = ["left", "up", "right", "down"]
        elif direction == "right":
            orientations = ["right", "down", "left", "up"]

        current_index = orientations.index(self.orientation)
        self.orientation = orientations[(current_index + 1) % 4]

    def display_position(self):
        print(f"Current position: ({self.position_x}, {self.position_y})")


robotics = Robot("up", 0, 0)
robotics.move(5)
robotics.display_position()

robotics.turn("right")
robotics.move(3)
robotics.display_position()
