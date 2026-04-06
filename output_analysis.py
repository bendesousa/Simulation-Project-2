import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_excel('baseline_cycle_times_updated.xlsx', header=None)
avg_cycle = data[0].dropna()
total_laptops = data[1].dropna()

# Avg cycle CI
n = len(avg_cycle)
mean_cycle = np.mean(avg_cycle)
ci_cycle = stats.t.interval(0.95, df=n-1, loc=mean_cycle, scale=stats.sem(avg_cycle))

# Total laptops mean
mean_laptops = np.mean(total_laptops)
ci_laptops = stats.t.interval(0.95, df=n-1, loc=mean_laptops, scale=stats.sem(total_laptops))

print(f"Avg Cycle Time - Mean: {mean_cycle:.2f} seconds, 95% CI: ({ci_cycle[0]:.2f}, {ci_cycle[1]:.2f})")
print(f"Total Laptops - Mean: {mean_laptops:.2f}, 95% CI: ({ci_laptops[0]:.2f}, {ci_laptops[1]:.2f})")