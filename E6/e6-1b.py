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
            if ap > 0.75:
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

def calc_media(lista):
    if len(lista) == 0:
        return -1
        
    size = len(lista)
    media_x = 0
    media_y = 0
    for i in range(len(lista)):
        media_x += lista[i].x
        media_y += lista[i].y
    return media_x/size, media_y/size

def calc_desvio_padrao(lista):
    if len(lista) == 0:
        return -1

    media_x,media_y = calc_media(lista)
    dv_x = 0
    dv_y = 0
    for i in range(len(lista)):
        dv_x += math.pow(lista[i].x - media_x,2)
        dv_y += math.pow(lista[i].y - media_y,2)
    return math.sqrt(dv_x/len(lista)), math.sqrt(dv_y/len(lista))


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
    run_times = 0
    pop_1 = population_A
    pop_2 = population_B
    pop_generated = []
    while counter != 100 and run_times < run_limit:
        pop_generated = []
        pop_control = 0
        for i in range(len(pop_1)):
            new_pair = Pair(pop_1[i].x, pop_2[i].y)
            val = calc_pairs(new_pair.x, new_pair.y)
            if val > -0.2 and val < 0.2:
                population_X.append(new_pair)
                pop_generated.append(new_pair)
            else:
                mutated = mutation(new_pair)
                pop_generated.append(new_pair)
            if counter == 100:
                break

        if pop_control == 0:
            pop_2 = pop_generated
            pop_control = 1
        else:
            pop_1 = pop_generated
            pop_control = 0
        run_times += 1


def mutation(pair):
    mut_pair = pair
    mut_prob = random.uniform(0.0,1.0)
    if mut_prob > 0.75:
        mut_pair.x = random.uniform(-10.0,10.0)
        mut_pair.y = random.uniform(-10.0,10.0)
        return mut_pair
    return mut_pair

def calc_pairs(x,y):
    return check_function_ackley(x,y)


#Main function
def main():
    # simulated_annealing()
    # print locations

    generate_population()
    cross_population()
    for j in range(len(population_X)):
        print "( ",population_X[j].x, ",", population_X[j].y ," )"

    print "Media : ", calc_media(population_X)
    print "Desvio Padrao : ", calc_desvio_padrao(population_X)
    print "\n"
    del population_A[:]
    del population_B[:]
    del population_X[:]
if __name__ == "__main__":
    main()
