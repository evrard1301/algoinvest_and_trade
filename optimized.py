import math
import action
from state import State

algo = action.ActionLoader()
algo.load_from_file('dataset_0.csv')

class Solver:
    def __init__(self, actions):
        self.actions = actions
        self.mean_profit = 0
        self.mean_cost = 0

        for action in self.actions:
            self.mean_profit += action.get_profit()
            self.mean_cost += action.cost
        self.mean_profit /= len(self.actions)
        self.mean_cost /= len(self.actions)

    def run(self):
        opened = [State()]
        closed = []        
        N = len(self.actions) * 2
        
        for i in range(N):
            best = self.find_best(opened)

            if best is None:
                break
            
            opened.remove(best)
            closed.append(best)

            neighbors = self.successor(best, pow(1 - (i/N), 1.2))
            
            for neighbor in neighbors:
                assert(neighbor not in opened)
                if neighbor not in closed:
                    opened.append(neighbor)
                    
        print('----------------')
        print('->', len(self.find_best(closed).actions))
        print(self.find_best(closed).info())

        return self.find_best(closed)

    def successor(self, state, ratio=0.0):
        result = []
        actions = [i for i in self.actions if i not in state.actions]

        for action in actions:
            s = State(state.actions.union([action]), 0)
            s.cost = state.cost + action.get_profit()

            if s.total_cost <= 500 and action.get_profit() >= ratio * self.mean_profit:
                result.append(s)

        return result

    def find_best(self, states_list):
        if len(states_list) == 0:
            return None
        
        max_cost = -1
        best = None

        for state in states_list:
            if state.cost > max_cost:
                max_cost = state.cost
                best = state
                
        return best

Solver(algo.actions).run()
