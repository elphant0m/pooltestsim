import random

def get_infection_rates(step_size):
    infection_rates = []
    fraction = step_size
    while fraction <= 1.0:
        infection_rates.append(fraction)
        fraction = fraction+step_size
    return infection_rates

def get_pool_sizes(pop_size, step_size):
    pool_sizes=[]
    i = 1
    while i*step_size <= pop_size:
        pool_sizes.append(i*step_size)
        i+=1
    return pool_sizes

def run_sim_steps(num_runs, pop_size, infection_rate, pool_sizes):
    num_infected = int(pop_size * infection_rate)
    avg_tests_used=[]
    for pool_size in pool_sizes:
        num_pools = int(pop_size / pool_size)
        if pop_size % pool_size != 0:
            num_pools += 1
        run_totals = 0
        for run in range(num_runs):
            pools = [False] * num_pools
            for i in range(num_infected):
                pools[random.randint(0,len(pools)-1)] = True
            for pool in pools:
                if pool: run_totals+=(pool_size+1)
                else: run_totals+=1
        avg_tests_used.append("%.1f"%(run_totals/num_runs))
    return avg_tests_used

# global variables
pop_size = 100
num_runs = 10
step_size = 5
write_to_file=True
file_name="output.csv"

# growing pool sizes
pool_sizes = get_pool_sizes(pop_size, step_size)
s = "rate\group_size,"+",".join([str(x) for x in pool_sizes])+"\n"
print(s)
if write_to_file:
    f = open(file_name,'w')
    f.write(s)

infection_rates = get_infection_rates(.05)
for infection_rate in infection_rates:
    s ="%1.1f%%,"%(infection_rate*100)
    data=",".join([str(x) for x in run_sim_steps(num_runs,pop_size,infection_rate,pool_sizes)])
    s+=data+"\n"
    print(s)
    if write_to_file:
        f.write(s)
    
if write_to_file:
    f.close
    