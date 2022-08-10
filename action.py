import os
import csv

class Action:
    def __init__(self, name, cost, profit):
        self.name = name
        self.cost = cost
        self.profit = profit

    def get_profit(self):
        return self.cost * self.profit/100.0
    
    def __str__(self):
        return f'{self.name}: {self.cost} -> {self.profit}%'
    
    def __repr__(self):
        return self.name


class ActionLoader:
    def __init__(self):
        self.actions = []

    def load_from_file(self, filename):
        with open(os.path.join('datasets', filename), 'r') as file:            
            data = csv.reader(file, delimiter=",")
            next(data)
            for row in data:
                if float(row[1]) >= 0 and float(row[2]) >= 0:
                    self.actions.append(Action(row[0], float(row[1]), float(row[2])))
                
    
