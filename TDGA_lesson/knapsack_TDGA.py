#!/usr/bin/env python
# coding: utf-8

__author__  = "Akira Terauchi"
__version__ = "0.01"
__date__    = "22 Jul 2020"

from tdga.td_selection import ThermoDynamicalSelection

import random
from analyzer import Analyzer

from deap import base
from deap import creator
from deap import tools
import numpy as np

W = 744
items = [
    (75, 7),
    (84, 9),
    (58, 13),
    (21, 5),
    (55, 16),
    (95, 28),
    (28, 15),
    (76, 43),
    (88, 60),
    (53, 37),
    (58, 44),
    (81, 63),
    (32, 34),
    (89, 95),
    (54, 61),
    (23, 29),
    (42, 57),
    (52, 72),
    (58, 83),
    (53, 84),
    (30, 48),
    (26, 45),
    (40, 74),
    (40, 78),
    (26, 52),
    (39, 79),
    (25, 64),
    (23, 64),
    (16, 55),
    (12, 74)
]

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, len(items))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evalation(individual):
    v_sum = 0
    w_sum = 0
    for i, x in enumerate(individual):
        v, w = items[i]
        v_sum += x*v
        w_sum += x*w
    return (v_sum,) if w_sum <= W else (0, )


toolbox.register("evaluate", evalation)
toolbox.register("mate", tools.cxUniform, indpb=0.5)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)

stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

Np = 32
t_init = 10
Ngen = 100
tds = ThermoDynamicalSelection(Np=Np, t_init=t_init, scheduler=lambda x: x)
toolbox.register("select", tds.select)


def main():
    pop = toolbox.population(n=Np)
    CXPB, MUTPB, NGEN = 1, 1, Ngen

    print("Start of evolution")

    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("Evaluated %i individuals" % len(pop))

    analizer = Analyzer()
    for g in range(NGEN):
        print("-- Generation %i --" % g)
        elite = tools.selBest(pop, 1)
        elite = list(map(toolbox.clone, elite))
        offspring = list(map(toolbox.clone, pop))

        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):

            if random.random() < CXPB:
                toolbox.mate(ind1, ind2)
                del ind1.fitness.values
                del ind2.fitness.values

        gen = pop + offspring  # 2Np
        for mutant in gen:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        gen += elite

        invalid_ind = [ind for ind in gen if not ind.fitness.valid]
        print("Evaluated %i individuals" % len(invalid_ind))
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        selected = toolbox.select(gen, k=Np)
        pop[:] = selected

        record = stats.compile(pop)

        print("  Min %s" % record["min"])
        print("  Max %s" % record["max"])
        print("  Avg %s" % record["avg"])
        print("  Std %s" % record["std"])

        analizer.add_pop(list(map(toolbox.clone, pop)))

    print("-- End of (successful) evolution --")

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
    analizer.plot_entropy_matrix(file_name="TDGA_entropy.png")
    analizer.plot_stats(file_name="TDGA_stats.png", optimum_val=1099)
    return best_ind


if __name__ == "__main__":
    ret_ = main()
