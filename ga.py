from population import Population

aim = 'Shrish Asthana'
strength = 100
mutation_rate = 0.2

population = Population(strength, mutation_rate, aim)
print(population.get_strength())
print(population.get_mutation_rate())

population.create_population()
population.print_population()

done = False
generation = 0

while not done:
    generation += 1
    response = population.find_best_fitness()
    best_fitness = response['fitness']
    best_fit = response['fit']
    print(best_fit, end=" ")
    print(best_fitness, end=" ")
    print(generation)
    if best_fitness == 1:
        done = True
    population.evolve()
    population.calc_fitness()
    #population.print_population()
    
