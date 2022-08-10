class State:
    def __init__(self, actions=set(), cost=0):
        self.actions = set(actions)
        self.cost = cost
        
    def __repr__(self):
        return f'{self.actions} => {self.cost}'
    
    @property
    def total_profit(self):
        return sum([i.get_profit() for i in self.actions])

    @property
    def total_cost(self):
        return sum([i.cost for i in self.actions])

    def info(self):
        return f'{self.actions} ({self.cost}): {self.total_profit} ({self.total_cost})'
