import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_excel('baseline_cycle_times_1.xlsx', header=None)[0].dropna()
n = len(data)
mean = np.mean(data)
se = stats.sem(data)
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)

print(f"Mean: {mean:.2f} minutes")
print(f"95% CI: ({ci[0]:.2f}, {ci[1]:.2f})")