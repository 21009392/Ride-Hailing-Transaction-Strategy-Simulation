class CityEnv:
    def __init__(self, users, drivers):
        self.users = users
        self.drivers = drivers
        self.orders = []

    def generate_order(self, user, t):
        pass

    def step(self):
        pass
def distance_based_matching(order, drivers):
    pass

def utility_based_matching(order, drivers, alpha=0.7):
    """
    utility = - distance - alpha * waiting_time
    """
    pass
def subsidy_strategy(order, level):
    order["subsidy"] = level
import numpy as np

def accept_prob(price, subsidy, sensitivity):
    utility = subsidy - sensitivity * price
    return 1 / (1 + np.exp(-utility))
def fulfillment_rate(orders):
    pass

def avg_waiting_time(orders):
    pass

def driver_idle_rate(drivers):
    pass
def run_experiment(strategy):
    pass
