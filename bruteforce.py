import action

algo = action.ActionLoader()
algo.load_from_file('dataset_0.csv')

def bruteforce(actions, current=[], cost=0, profit=0, solutions=[], index=0):
    
    if cost <= 500:
        solutions.append((current, cost, profit))
    
    for i in range(index, len(actions)):
        action = actions[i]
        
        bruteforce([i for i in actions if i != action],
            current + [action],
            cost + action.cost,
            profit + action.cost * action.profit/100.0,
            solutions,
            i)
    
    return solutions

if __name__ == '__main__':
    solutions = bruteforce(algo.actions)
    solutions.sort(key=lambda s: s[2])
    print(str(solutions[-1]))
