import random
from deap import base
from deap import creator
from deap import tools

def my_new(ind1, ind2):
    offspring1 = []
    offspring2 = []
    for i in range(len(ind1)):
        p = random.random()
        if p < 0.5:
            offspring1.append(ind1[i])
        else:
            offspring1.append(ind2[i])
    for i in range(len(ind1)):
        p = random.random()
        if p < 0.5:
            offspring2.append(ind1[i])
        else:
            offspring2.append(ind2[i])
    return offspring1, offspring2

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1) #遺伝子
toolbox.register("individual", tools.initRepeat, creator.Individual,toolbox.attr_bool, 100) #個体
toolbox.register("population", tools.initRepeat, list, toolbox.individual) #個体集団

def evalOneMax(individual): #評価関数 indivisualを数え上げる
    return sum(individual),

toolbox.register("evaluate", evalOneMax) #評価関数
toolbox.register("mate", my_new) #交叉
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05) #変異
toolbox.register("select", tools.selTournament, tournsize=3) #個体選択法

def main():
    # random.seed(1)

    N_GEN = 100 #世代数
    POP_SIZE = 1000 #個体数
    CX_PB = 0.5 #交叉確率
    MUT_PB = 0.2 #突然変異の確率

    pop = toolbox.population(n=POP_SIZE) #個体集団の生成

    print("Start of evolution")

    fitnesses = list(map(toolbox.evaluate, pop)) # 個体集団の適応度の評価
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))

    fits = [ind.fitness.values[0] for ind in pop] # 適応度の抽出

    g = 0
    while g < N_GEN:

        g = g + 1
        print("-- Generation %i --" % g)

        # 次世代個体の選択・複製
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        # 交叉
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CX_PB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # 突然変異
        for mutant in offspring:
            if random.random() < MUT_PB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # 適応度の再評価
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print("  Evaluated %i individuals" % len(invalid_ind))

        # 個体集団を新世代個体集団で更新
        pop[:] = offspring

        # 新世代の全個体の適応度の抽出
        fits = [ind.fitness.values[0] for ind in pop]

        # 適応度の統計情報の出力
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)


    print("-- End of (successful) evolution --")

    # 最良個体の抽出
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))


if __name__ == '__main__':

    main()
