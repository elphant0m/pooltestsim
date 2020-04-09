import random

def get_pool_groupings(pop_size):
    pool_groupings = []
    for i in range(1,pop_size):
        if pop_size % i == 0:
            pool_groupings.append(i)
    return pool_groupings
    
def run_sim(num_runs,pop_size,percent_infected,pool_groupings):
    num_infected = int(pop_size * percent_infected)
    avg_tests_used=[]
    for num_pools in pool_groupings:
        pool_size = int(pop_size / num_pools)
        run_totals = 0
        for run in range(num_runs):
            pools = [False] * num_pools
            for i in range(num_infected):
                pools[random.randint(0,len(pools)-1)] = True
            for pool in pools:
                if pool: run_totals+=(pool_size+1)
                else: run_totals+=1
        avg_tests_used.append("%3.1f"%(run_totals/num_runs))
    print(*avg_tests_used,sep=",")


pop_size = 1000
num_runs = 100
pool_groupings = get_pool_groupings(pop_size)
print("rate\group_size",end=",")
print(*pool_groupings,sep=",")
infection_rates = [x * 0.1 for x in range(1,10)]
for infection_rate in infection_rates:
    print("%1.1f,"%(infection_rate),end="")
    run_sim(num_runs,pop_size,infection_rate,pool_groupings)
