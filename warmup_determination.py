import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('warmup_determination.xlsx', header=None)
df.columns = ['cycle_time', 'timestamp']
df = df.sort_values('timestamp').reset_index(drop=True)

windows = [10, 20, 50, 100]

fig, axes = plt.subplots(2, 2, figsize=(14, 8))
axes = axes.flatten()

for i, w in enumerate(windows):
    df['moving_avg'] = df['cycle_time'].rolling(window=w, center=True).mean()
    axes[i].plot(df['timestamp'], df['cycle_time'], alpha=0.3, label='Raw cycle time')
    axes[i].plot(df['timestamp'], df['moving_avg'], label=f'Moving avg (w={w})', linewidth=2)
    axes[i].set_xlabel('Simulation Time (minutes)')
    axes[i].set_ylabel('Cycle Time (minutes)')
    axes[i].set_title(f'w={w}')
    axes[i].legend()

plt.tight_layout()
plt.savefig('welch_comparison.png', dpi=150)
plt.show()