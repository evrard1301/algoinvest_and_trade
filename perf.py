import threading
import action
import optimized
import bruteforce
import os
import tqdm
import timeit
import numpy as np
import matplotlib.pyplot as plt

loader = action.ActionLoader()
loader.load_from_file('dataset_2.csv')

def run_opti(n):
    before = timeit.default_timer()
    solver = optimized.Solver(loader.actions[0:n])
    state = solver.run()
    opti_profit.append(state.total_profit)
    opti_cost.append(state.total_cost)
    return timeit.default_timer() - before

def run_bruteforce(n):
    before = timeit.default_timer()
    s = bruteforce.bruteforce(loader.actions[0:n])
    s.sort(key=lambda s: s[2])
    bf_profit.append(s[-1][2])
    bf_cost.append(s[-1][1])
    return timeit.default_timer() - before

max_val = 22
min_val = 1
inputs = np.arange(min_val, max_val)

opti_outputs = []
bf_outputs = []

opti_profit = []
bf_profit = []

opti_cost = []
bf_cost = []

print("Génération du rapport")

def run_all_opti(pbar):
    for i in range(min_val, max_val):
        opti_outputs.append(run_opti(i))
        pbar.update(1)

def run_all_bruteforce(pbar):
    for i in range(min_val, max_val):
        bf_outputs.append(run_bruteforce(i))
        pbar.update(1)


with tqdm.tqdm(total=(max_val - min_val) * 2) as pbar:
    t0 = threading.Thread(target=run_all_opti, args=[pbar])
    t1 = threading.Thread(target=run_all_bruteforce, args=[pbar])

    t0.start()
    t1.start()

    t0.join()
    t1.join()
    
fig = plt.figure()

axes, profit_axes, cost_axes = fig.subplots(3, 1)

axes.plot(inputs, bf_outputs, label='Bruteforce')
axes.plot(inputs, opti_outputs, label='Optimized')

axes.set(title='Comparing bruteforce and optimized algorithms',
         xlabel='number of actions',
         ylabel='execution time in seconds')

axes.legend()

profit_axes.set(xlabel='number of actions',
                ylabel='total profit')

profit_axes.plot(inputs, bf_profit, label="Bruteforce")
profit_axes.plot(inputs, opti_profit, label="Optimized")

profit_axes.legend()


cost_axes.set(xlabel='number of actions',
                ylabel='total cost')

cost_axes.plot(inputs, bf_cost, label="Bruteforce")
cost_axes.plot(inputs, opti_cost, label="Optimized")

cost_axes.legend()

plt.savefig('perf.png')
plt.show()
