import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel('warmup_determination.xlsx', header=None)
df.columns = ['cycle_time', 'timestamp']

# Sort by timestamp
df = df.sort_values('timestamp').reset_index(drop=True)

# Welch's method - moving average with increasing window
w = 20  # adjust this window size
df['moving_avg'] = df['cycle_time'].rolling(window=w, center=True).mean()

plt.figure(figsize=(12, 5))
plt.plot(df['timestamp'], df['cycle_time'], alpha=0.3, label='Raw cycle time')
plt.plot(df['timestamp'], df['moving_avg'], label=f'Moving avg (w={w})', linewidth=2)
plt.xlabel('Simulation Time (minutes)')
plt.ylabel('Cycle Time (minutes)')
plt.title("Welch's Method - Warm-up Detection")
plt.legend()
plt.savefig('welch_method_warmup_detection.png')
plt.show()