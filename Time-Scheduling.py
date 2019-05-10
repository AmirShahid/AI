import random
from queue import PriorityQueue
import copy


class Task:
    def __init__(self, name, release_time, co_time, deadline):
        self.name = name
        self.release_time = release_time
        self.co_time = co_time
        self.deadline = deadline
        self.fin_time = None
        self.start_time = None

    def __str__(self):
        task = self
        return str(task.name) + ' ' + str(task.start_time) + ' ' + str(task.fin_time)

    def __eq__(self, other):
        return self.name == other.name


class scheduling:
    def __init__(self, genes):
        self.chromosome = genes
        self.fitness = self.cal_heuristic()

    def mate(self, sec_scheduling):
        new_genes = []
        # print(len(self.chromosome))
        for t1, t2 in zip(self.chromosome, sec_scheduling.chromosome):
            p = random.uniform(0, 1)
            if p < 0.45 and t1 not in new_genes:
                new_genes.append(t1)
            elif p < 0.9 and t2 not in new_genes:
                new_genes.append(t2)
            else:
                # print('rrrrrrandom')
                new_possib_genes = [possib_gene for possib_gene in posib_genes if possib_gene not in new_genes]
                # print(new_possib_genes)
                t3 = random.choice(new_possib_genes)
                new_genes.append(t3)

            # print('father:',self.chromosome[0] ,'mother:', sec_scheduling.chromosome[0] ,'child :', new_genes[0])
        return scheduling(new_genes)

    def cal_heuristic(self):
        h = 0
        tasks = sorted(self.chromosome, key=lambda t: t.fin_time)
        # print('sorted')
        # for i in tasks:
        #     print(i)
        # print('end')
        for i in range(len(tasks) - 1):
            if tasks[i].fin_time > tasks[i + 1].start_time:
                h += 1
        return h

    def __lt__(self, other):
        return self.fitness < other.fitness


posib_genes = []
best_timing = []
# chromosome = []
population = []
task_num = int(input())

for z in range(task_num):
    line = input().split()
    main_task = Task(line[0], int(line[1]), int(line[2]), int(line[3]))
    for st_time in range(main_task.release_time, (main_task.deadline - main_task.co_time) + 1):
        new_task = Task(line[0], int(line[1]), int(line[2]), int(line[3]))
        new_task.start_time = st_time
        new_task.fin_time = new_task.start_time + new_task.co_time
        # print(new_task.name, st_time)
        posib_genes.append(new_task)


# for gene in posib_genes:
#     print(gene)

def rand_choose(list, execpt):
    possib = [ind for ind in list if ind not in execpt]
    # if possib:
    return random.choice(possib)
    # else:
    #     return None


solve = False
# print(population.queue)
population_size = task_num
# while len(population) <  population_size :
genes_list = []
while len(genes_list) < task_num:
    genes_list.append(rand_choose(posib_genes, genes_list))
c = scheduling(genes_list)
# for i in c.chromosome:
#     print(i)
# print(c.fitness)
# population.put((c.fitness, c))
population.append(c)
# break


generation = 0

# for i in population:
# i.chromosome = sorted(i.chromosome,key=lambda i:i.fin_time)
# print(i.chromosome[0] , i.chromosome[1] )


while not solve and generation < 10 ** 3:
    childs = []
    # bests = []
    # print('generation:', generation, 'fitness:', population[0].fitness)

    for best in range(int(population_size * 0.1)):
        if best < len(population):
            person = population[best]
            childs.append(person)
        else:
            break

    for rest in range(int(population_size * 0.9)):
        father = random.choice(population)
        # print(father,'popu:',population[0])
        # a=[person for person in population if person  != father]
        mother = random.choice(population)
        child = father.mate(mother)
        childs.append(child)
    # print('ch:',childs)
    if len(childs) == 0 and len(population) == 1:
        childs.append(population[0])
    population = childs
    population = sorted(population, key=lambda schedule: schedule.fitness)
    best_timing = population[0].chromosome
    if population[0].fitness==1:
        population = [population[0]]
        # print(len(population))
    if population[0].fitness <= 0:
        solve = True
        best_timing = population[0].chromosome
        # print('YEAAY !!!! fitness is ZERO :))))))')

    generation += 1

best_timing.sort(key=lambda x: x.start_time)
for task in best_timing:
    print(task.name, task.start_time, task.fin_time)

for task in best_timing:
    print()
    print(task.name, task.start_time, task.fin_time, end=' ')
    for i in range(task.fin_time):
        print(i)
        if i < task.start_time:
            print(' ', end='')
        elif i > task.start_time:
            print('_', end='')
