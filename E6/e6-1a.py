import math
import random

#List of locations passed
locations = []
#Limit of iterations to reach the ideal solution
run_limit = 50000
#Euler constant user for Item A of List VI
euler_a =  2.718
#Euler constant used for Item B of List VI
euler_b = 5.772156649

#Function for item A
def check_function_A(x, y):
    return math.pow((math.pow(x,2)+y-11),2) + math.pow((x+math.pow(y,2)-7),2)

#Function for item B
def check_function_B(x, y):
    euler_exp = -0.2*math.sqrt(math.pow(x,2)+math.pow(y,2))
    return -200*euler_exp

#Generate a random neighbor. This is a function to be used in Simulated Annealing.
def generate_neighbor():
    pos_x = random.uniform(-10.0,10.0)
    pos_y = random.uniform(-10.0,10.0)
    return pos_x,pos_y

#Function to determine the cost to move for the next position. Function to be
#used in Simulated Annealing.
def costA(x, y):
    return check_function_A(x,y)

#Function to determine the cost to move for the next position. Function to be
#used in Simulated Annealing.
def costB(x, y):
    return check_function_B(x,y)

#Funcion to verify the probability of the new solution to be accepted or not.
#Function used in Simulated Aneealing.
def acceptance_probability (old_cost, new_cost, temp):
    if new_cost < old_cost:
        return 1.0
    else:
        calculate_exp = (new_cost - old_cost) / temp
        if calculate_exp < 0:
            new_c = round(math.pow(e,calculate_exp),2)
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
    #old_sol = costA(first_x, first_y)
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
            #new_sol = costA(new_x, new_y)
            new_sol = costB(new_x, new_y)
            ap = acceptance_probability(old_sol, new_sol, temp)
            if ap > 0.7:
                sol = round(new_sol,2)
                locations.append(sol)
                old_sol = new_sol
            i += 1
            run_times += 1
        temp = temp*alpha

    return locations


#Main function
def main():
    simulated_annealing()
    print locations


if __name__ == "__main__":
    main()
