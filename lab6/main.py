import random

matrix = [
    [0, 1, 7, 2, 8],
    [2, 0, 10, 3, 1],
    [7, 10, 0, 2, 6],
    [2, 3, 2, 0, 4],
    [8, 1, 6, 4, 0],
]

POPULATION_SIZE = 4
CITIES_SIZE = 5
ITERATIONS = 1000


class Chromosome:
    def __init__(self, cities):
        self.cities = cities

    def get_target_function(self):
        result = 0
        for i in range(len(self.cities)):
            from_city = self.cities[-1] if i == 0 else self.cities[i - 1]
            to_city = self.cities[i]
            result += matrix[from_city][to_city]
        return result


def main():
    cities_bypass_sheet = list(range(1, CITIES_SIZE))
    population = [Chromosome([0] + cities_bypass_sheet)]

    for _ in range(POPULATION_SIZE - 1):
        population.append(
            Chromosome(
                [0] + random.sample(cities_bypass_sheet, len(cities_bypass_sheet))
            )
        )

    for _ in range(ITERATIONS):
        # Crossover
        parents = random.sample(population, 4)
        break_point = random.randint(0, CITIES_SIZE - 1)
        for j in range(0, len(parents), 2):
            first_parent = parents[j]
            second_parent = parents[j + 1]

            first_child = first_parent.cities[:break_point]
            first_child += [
                city
                for city in second_parent.cities[break_point:]
                if city not in first_child
            ]
            first_child += [
                city
                for city in second_parent.cities[:break_point]
                if city not in first_child
            ]

            second_child = second_parent.cities[:break_point]
            second_child += [
                city
                for city in first_parent.cities[break_point:]
                if city not in second_child
            ]
            second_child += [
                city
                for city in first_parent.cities[:break_point]
                if city not in second_child
            ]

            # Mutation
            if random.randint(0, 99) == 0:
                index1, index2 = random.sample(range(CITIES_SIZE), 2)
                first_child[index1], first_child[index2] = (
                    first_child[index2],
                    first_child[index1],
                )

            # Add to population
            population.append(Chromosome(first_child))
            population.append(Chromosome(second_child))

        population.sort(key=lambda x: x.get_target_function())
        population = population[:POPULATION_SIZE]

    print(
        f"Результат: {[city + 1 for city in population[0].cities]} Значение ЦФ: {population[0].get_target_function()}"
    )


if __name__ == "__main__":
    main()
