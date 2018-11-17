import random as r
import numpy as np

seed = 72187312
np.random.seed(seed)


class Customer:
    #default as low clas customers without catalogue
    def __init__(self):
        self.age = 0
        self.name =  str(id(self))
        self.catalogue = False
        self.high_class = False
        self.history = []

    def has_birthday(self):
        self.age += 1

    def toggle_catalogue(self):
        self.catalogue = not self.catalogue

    def toggle_class(self):
        self.high_class =  not self.high_class

    def buy(self):
        if self.catalogue and self.high_class:
            print('buys $50')
            return 50
        elif not self.catalogue and self.high_class:
            print('buys $25')
            return 25
        elif self.catalogue and not self.high_class:
            print('buys $20')
            return 20
        elif not self.catalogue and not self.high_class:
            print('buys $10')
            return 10

# simulation interaction utilities

def spawn_Customer():
    customer = Customer()
    return customer

def generate_population(n):
    population = []
    for i in range(n):
        custy = spawn_Customer()
        population.append(custy)
    return population

def cycle_revenue(population):
    revenue = 0
    for i in range(len(population)): # for every customer
        revenue = revenue + population[i].buy() # add what they bought to the revenue pool for the cycle
    return revenue

def cycle_expense(catalogues_sent):
    return catalogues_sent * 15

def cycle_profit(population,catalogues_sent=10):
    revenue = cycle_revenue(population)
    expense = cycle_expense(catalogues_sent)
    profit = revenue - expense
    print('cycle ebit = ' + str(profit))
    return profit

def catalogue_sender(send_to_high = False, send_to_low = False, population = []):
    sent_catalogues = 0
    if send_to_high:
        for i in range(len(population)):
            if population[i].high_class:
                print('debug - sending to high value customer'+population[i].name)
                if not population[i].catalogue:
                    population[i].toggle_catalogue()
                    sent_catalogues += 1
    else:
        for i in range(len(population)):
            print('debug -  not! sending to high value customer'+population[i].name)

    if send_to_low:
        for i in range(len(population)):
            if not population[i].high_class:
                print('debug - sending to low value customer'+population[i].name)
                if not population[i].catalogue:
                    population[i].toggle_catalogue()
                    sent_catalogues += 1
    else:
        for i in range(len(population)):
            print('debug - not! sending to low value customer'+population[i].name)

    return sent_catalogues

def catalogue_reseter(population=[]):
    for i in range(len(population)):
        if population[i].catalogue:
            population[i].toggle_catalogue()
            population[i].has_birthday()


def customer_promoter(population = [], H_to_L_Cat = 0.2 , L_to_H_Cat = 0.7 , H_to_L = 0.6 , L_to_H = 0.5):
    for i in range(len(population)):
        print(population[i].name)
        rv = s = np.random.uniform(0,1)
        if population[i].high_class and population[i].catalogue:
            if rv <= H_to_L_Cat:
                population[i].toggle_class()
                print('debug -- high to low with catalogue')
        elif population[i].high_class and not population[i].catalogue:
            if rv <= H_to_L:
                population[i].toggle_class()
                print('debug -- high to low with OUT catalogue')
        elif  not population[i].high_class and population[i].catalogue:
            if rv <= L_to_H_Cat:
                population[i].toggle_class()
                print('debug -- low to high with catalogue')
        else:
            if rv <= L_to_H:
                population[i].toggle_class()
                print('debug -- low to high with Outcatalogue')




def output_string(counter,profits):
        print('\n \n \n \n' + '------------' + '\n \n \n \n' + 'total profits in ' + str(counter-1)+ ' periods: $' + str(profits) +
        ' for the send low only policy' + '\n \n \n \n' +'------------')

def simulation_string(counter):
    print('\n \n' )
    print('run ' + str(counter))
    print('------------')  



def simulation_core(n,send_to_high,send_to_low):
    customer = generate_population(10)
    profits = 0
    counter = 1

    while counter <= 20:
        simulation_string(counter)
        sent_catalogues = catalogue_sender(send_to_high,send_to_low,customer)
        profits += cycle_profit(customer, sent_catalogues)
        customer_promoter(customer)
        catalogue_reseter(customer)
        counter += 1
    output_string(counter,profits)
    return profits/n





def answer_question():
    both = simulation_core(1000,True,True)
    high = simulation_core(1000,True,False)
    low =  simulation_core(1000,False,True)
    none = simulation_core(1000,False,False)
    print('none: '+str(none))
    print('both: '+str(both))
    print('high: '+ str(high))
    print('low: '+str(low))
    maximum = max(none,both,high,low)
    print(maximum)




answer_question()



