import random
import time

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = 0

def create_individual(n):
    chromosome = [random.randint(0, 1) for _ in range(n)]
    return Individual(chromosome)

def evaluate(individual, weights, values, capacity):
    total_weight = 0
    total_value = 0
    for i, gene in enumerate(individual.chromosome):
        if gene == 1:
            total_weight += weights[i]
            total_value += values[i]
    if total_weight <= capacity:
        return total_value
    return 0

def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: x.fitness, reverse=True)
    return tournament[0]

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1.chromosome) - 1)
    child_chromosome = parent1.chromosome[:crossover_point] + parent2.chromosome[crossover_point:]
    return Individual(child_chromosome)

def mutate(individual, mutation_rate):
    for i in range(len(individual.chromosome)):
        if random.random() < mutation_rate:
            individual.chromosome[i] = 1 - individual.chromosome[i]
    return individual

def genetic_algorithm(weights, values, capacity, population_size, mutation_rate, generations):
    random.seed(time.time())

    population = [create_individual(len(weights)) for _ in range(population_size)]

    for generation in range(generations):
        for individual in population:
            individual.fitness = evaluate(individual, weights, values, capacity)

        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, 5)
            parent2 = tournament_selection(population, 5)
            child = crossover(parent1, parent2)
            new_population.append(child)

        for individual in new_population:
            mutate(individual, mutation_rate)

        population = new_population

    for individual in population:
        individual.fitness = evaluate(individual, weights, values, capacity)

    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[0]

weights = [6, 4, 3, 2, 5]
values = [5, 3, 1, 3, 6]
capacity = 15
population_size = 100
mutation_rate = 0.1 # шанс мутации
generations = 100

best_individual = genetic_algorithm(weights, values, capacity, population_size, mutation_rate, generations)

print("Numbers of items placed in the backpack:", best_individual.chromosome)
print("Maximum value that can be carried in a backpack:", best_individual.fitness)

"""
1. Создание начальной популяции:
   - Начальная популяция может состоять из особей, где каждая особь представлена битовой последовательностью 1 0 1.
   - Например, начальная популяция может выглядеть так:
     - Особь 1: 1 0 1
     - Особь 2: 1 0 1 
     - Особь 3: 1 0 1
     - ...

2. Выбор родителей:
   - Из текущей популяции выбираются пары родителей, которые будут участвовать в скрещивании.
   - Выбор родителей может происходить с использованием различных методов отбора, например, турнирный отбор или отбор по методу рулетки.
   - Например, могут быть выбраны следующие пары родителей:
     - Родитель 1: 1 0 1
     - Родитель 2: 1 0 1

3. Скрещивание (кроссовер):
   - Для каждой выбранной пары родителей производится скрещивание, чтобы создать новых потомков.
   - Во время скрещивания происходит комбинация генетической информации родителей.
   - Например, если точка разрыва выбрана после первого бита, то потомки будут иметь вид:
     - Потомок 1: 1 0 1
     - Потомок 2: 1 0 1

4. Мутация:
   - После скрещивания, в генетической информации потомков может произойти мутация - случайное изменение одного или нескольких битов.
   - Мутация вводит дополнительное разнообразие в популяцию.
   - Например, если в Потомке 1 произойдет мутация второго бита, то он может принять вид:
     - Потомок 1 после мутации: 1 1 1

5. Формирование новой популяции:
   - Новая популяция формируется путем замены части худших особей в текущей популяции на новых потомков, полученных в результате скрещивания и мутации.

Турнир:

Из этих особей, участвующих в турнире, выбирается "победитель" - особь с лучшим значением функции приспособленности (fitness).
"""
