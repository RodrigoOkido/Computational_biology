locations = []
run_limit = 50000
e =  2.718

def check_function(x, y):
    return pow((pow(x,2) + y − 11),2) + pow((x + pow(y,2) − 7), 2)


def simulated_annealing(sol):
    old_sol = cost(sol)
    temp = 1.0
    temp_min = 0.00001
    alpha = 0.9
    while temp > temp_min:
        i = 1
        while i <= 100:
            new_x, new_y = generate_neighbor(sol)
            new_sol = cost(new_x, new_y)
            ap = acceptance_probability(old_sol, new_sol, temp)
            if ap > random():
                sol = new_sol
                locations.append(sol)
                old_sol = new_sol
            i += 1
        temp = temp*alpha
    return locations

def generate_neighbor():
    pos_x = random.randint(-10,10)
    pos_y = random.randint(-10,10)
    return pos_x,pos_y

def cost(x, y):
    return check_function(x,y)


def acceptance_probability (old_cost, new_cost, temp):
    calculate_exp = ((new_cost - old_cost) / temp)
    return pow(e,calculate_exp)


def main():



if __name__ == "__main__":
    main()
