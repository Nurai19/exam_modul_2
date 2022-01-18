class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def display_info(self):
        print(
            f'Name: {self.name}\nPopulation: {self.population}\nArea: {self.area}'
        )


USA = Country(name='USA', population='330 million', area=9000000)
USA.display_info()
