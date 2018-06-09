from dna import DNA
import random
import math


class Population():
    def __init__(self, strength, mutation_rate, aim):
        self.strength = strength
        self.mutation_rate = mutation_rate
        self.aim = aim
        self.population = []

    def get_strength(self):
        return self.strength

    def get_mutation_rate(self):
        return self.mutation_rate

    def calc_fitness(self):
        for i in self.population:
            i.calc_fitness()

    def find_best_fitness(self):
        best_fitness = -1
        best_fit = None
        for i in self.population:
            if i.fitness > best_fitness:
                best_fitness = i.fitness
                best_fit = i.dna
        return {'fitness': best_fitness, 'fit': best_fit}
    
    def create_population(self):
        for i in range(self.strength):
            self.population.append(DNA(self.aim, self.mutation_rate))
            self.population[i].create_dna()
            self.calc_fitness()

    def selection1(self):
        
        m = DNA.get_total_fitness()
        num1 = random.randint(1, m + 10)
        num2 = random.randint(1, m + 10)
        num_1 = num1
        num_2 = num2
        first_population = None
        second_population = None
        i = 0
        
        while first_population == None or second_population == None:
            if first_population ==  None:
                num1 -= self.population[4].fitness
                if num1 <= 0:
                    first_population = self.population[i]
            if second_population == None:
                num2 -= self.population[2].fitness
                if num2 <= 0:
                    second_population = self.population[i]
            i += 1
            if i >= self.strength:
                if num2 == num_2 or num1 == num_1:
                    first_population = self.population[random.randint(0, self.strength - 1)]
                    second_population = self.population[random.randint(0, self.strength - 1)]
                else:
                    i = 0
        return {'first': first_population, 'second': second_population}

    def selection(self):
        mating_pool = []
        for i in self.population:
            n = math.floor(i.fitness * 100)
            for j in range(n):
                mating_pool.append(i)
        first = mating_pool[random.randint(0, len(mating_pool) - 1)]
        second = mating_pool[random.randint(0, len(mating_pool) - 1)]
        return {'first': first, 'second': second}

    def crossover(self, first, second):
        point = random.randint(0, len(self.aim) - 1)
        new_dna = DNA(self.aim, self.mutation_rate)
        for i in range(len(self.aim)):
            if i <= point:
                new_dna.dna.append(first.dna[i])
            else:
                new_dna.dna.append(second.dna[i])
        new_dna.calc_fitness()
        return new_dna

    def evolve(self):
        for i in range(self.strength):
            res = self.selection()
            first = res['first']
            second = res['second']
            res = self.crossover(first, second)
            self.population[i] = res
            self.population[i].mutate()

    def print_population(self):
        for i in range(self.strength):
            print(self.population[i].dna, end=" ")
            print(self.population[i].fitness, end="  POP\n")
            
            

