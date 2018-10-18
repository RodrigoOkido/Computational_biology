import math
import random

#List of locations passed
locations = []
#Limit of iterations to reach the ideal solution
run_limit = 50000
#Euler constant used for Item B of List VI
euler_b = 5.772156649


#Function for item B
def check_function_ackley(x, y):
    euler_exp = -0.2*math.sqrt(math.pow(x,2)+math.pow(y,2))
    result = math.pow(euler_b, euler_exp)
    return -200*result


###################### SIMULATED ANNEALING ######################
# Algoritmo de Trajetoria (Item A do exercicio 2 da lista VI)

#Generate a random neighbor. This is a function to be used in Simulated Annealing.
def generate_neighbor():
    pos_x = random.uniform(-10.0,10.0)
    pos_y = random.uniform(-10.0,10.0)
    return pos_x,pos_y

#Function to determine the cost to move for the next position. Function to be
#used in Simulated Annealing.
def costB(x, y):
    return check_function_ackley(x,y)

#Funcion to verify the probability of the new solution to be accepted or not.
#Function used in Simulated Aneealing.
def acceptance_probability (old_cost, new_cost, temp):
    if new_cost > old_cost:
        return 1.0
    else:
        calculate_exp = (new_cost - old_cost) / temp
        if calculate_exp < 0:
            new_c = round(math.pow(euler_b,calculate_exp),2)
            if new_c < 0.01:
                return 0
            else:
                return new_c
        else:
            return 0

#Simulated Annealing Function.
def simulated_annealing():
    first_x = random.uniform(-10.0,10.0)
    first_y = random.uniform(-10.0,10.0)
    old_sol = costB(first_x, first_y)

    #Setting parameters values (Temp, Temp_min and Alpha)
    temp = 1.0
    temp_min = 0.000001
    alpha = 0.95
    run_times = 0
    while temp > temp_min or run_times < run_limit:
        i = 1
        while i <= 100:
            new_x, new_y = generate_neighbor()
            new_sol = costB(new_x, new_y)
            ap = acceptance_probability(old_sol, new_sol, temp)
            if ap > 0.6:
                sol = round(new_sol,2)
                locations.append(sol)
                old_sol = new_sol
            i += 1
            run_times += 1
        temp = temp*alpha

    #print run_times
    return locations


###################### GENETIC ALGORITHMS ######################
# Algoritmo baseado em populacaso (Item B do exercicio 2 da lista VI)

population_A = []
population_B = []
population_X = []

class Pair:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def generate_population():
    for i in range(0,100):
        gen_x = random.uniform(-10.0,10.0)
        gen_y = random.uniform(-10.0,10.0)
        generated = Pair(gen_x,gen_y)
        population_A.append(generated)

        #Checks for elites
        check_pair = calc_pairs(generated.x , generated.y)
        if(check_pair > -0.2 and check_pair < 0.2):
            population_X.append(generated)

    for j in range(0,100):
        gen_x = random.uniform(-10.0,10.0)
        gen_y = random.uniform(-10.0,10.0)
        generated = Pair(gen_x,gen_y)
        population_B.append(generated)


def cross_population():
    counter = 0
    while counter != 100:
        for i in range(len(population_A)):
            for j in range(len(population_B)):
                new_pair = Pair(population_A[i].x, population_B[j].y)
                val = calc_pairs(new_pair.x, new_pair.y)
                if val > -0.2 and val < 0.2:
                    population_X.append(new_pair)
                    counter += 1
                else:
                    population_B[j] = new_pair
                if counter == 100:
                    break


def calc_pairs(x,y):
    return check_function_ackley(x,y)


#Main function
def main():
    #simulated_annealing()
    #print locations

    generate_population()
    cross_population()
    for j in range(len(population_X)):
        print "( ",population_X[j].x, ",", population_X[j].y ," )"

if __name__ == "__main__":
    main()
