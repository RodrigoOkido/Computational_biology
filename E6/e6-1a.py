import math
import random

locations = []
run_limit = 50000
e =  2.718

def check_function(x, y):
    return math.pow((math.pow(x,2)+y-11),2) + math.pow((x+math.pow(y,2)-7),2)


def generate_neighbor():
    pos_x = random.randint(-10,10)
    pos_y = random.randint(-10,10)
    return pos_x,pos_y

def cost(x, y):
    return check_function(x,y)


def acceptance_probability (old_cost, new_cost, temp):
    if new_cost < old_cost:
        return 1.0
    else:
        calculate_exp = (new_cost - old_cost) / temp
        new_c = round(math.pow(e,calculate_exp),2)
        return new_c

def simulated_annealing():
    first_x = random.randint(-10,10)
    first_y = random.randint(-10,10)
    old_sol = cost(first_x, first_y)
    temp = 100
    temp_min = 0.00001
    alpha = 0.9
    run_times = 0
    while temp > temp_min or run_times < run_limit:
        i = 1
        while i <= 100:
            new_x, new_y = generate_neighbor()
            new_sol = cost(new_x, new_y)
            ap = acceptance_probability(old_sol, new_sol, temp)
            if ap > 0.5:
                sol = new_sol
                locations.append(sol)
                old_sol = new_sol
            i += 1
            run_times += 1
        temp = temp*alpha

    return locations



def main():
    simulated_annealing()
    print locations


if __name__ == "__main__":
    main()
