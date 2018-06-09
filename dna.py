import random
import string


class DNA:

    total_fitness = 0;
    
    def __init__(self, aim, mutation_rate):
        self.aim = aim
        self.mutation_rate = mutation_rate
        self.dna = []
        self.fitness = 0
    
    def new_char(self):
        choices = list(string.ascii_letters)
        choices.append(" ")
#        c = choices[0: 26]
        return random.choice(choices)

    def create_dna(self):
        for i in range(len(self.aim)):
            self.dna.append(self.new_char())

    def calc_fitness(self):
        DNA.total_fitness -= self.fitness
        self.fitness = 0
        for i in range(len(self.aim)):
            if self.dna[i] == self.aim[i]:
                self.fitness += 1
        self.fitness = self.fitness / len(self.aim) 
        DNA.total_fitness += self.fitness

    def get_total_fitness():
        return DNA.total_fitness
    
    def mutate(self):
        prob = random.random()
        if prob <= self.mutation_rate:
            index = random.randint(0, len(self.aim) - 1)
            self.dna[index] = self.new_char()
    
    def print_dna(self):
        for i in self.dna:
            print(i, end="")
