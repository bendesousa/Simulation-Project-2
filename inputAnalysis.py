import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# =========================
# DATA LOADING
# =========================
df = pd.read_excel("Actual Real Data Final v42.xlsx", index_col="index").T
print(df.columns)
# =========================
# FITTING FUNCTION
# =========================

def fit_and_plot(data, dist, bounds=None, title=""):
    
    data = data.dropna()

    if bounds:
        result = stats.fit(dist, data, bounds)
    else:
        result = stats.fit(dist, data)

    print(f"\n--- {title} ---")
    print(result)

    result.plot()
    plt.title(title)
    plt.show()

    params = result.params._asdict()

    ks = stats.kstest(data, dist.name, args=tuple(params.values()))

    print("\n--- Goodness of fit (KS Test) ---")
    print(f"KS Statistic: {ks.statistic}")
    print(f"P-value: {ks.pvalue}")

    return result

def find_best_distribution(data, dists, dataset_name="Dataset", top_n=5):

    data = data.dropna()

    results = []

    for dist in dists:

        try:
            params = dist.fit(data)

            # log-likelihood
            loglik = np.sum(dist.logpdf(data, *params))

            k = len(params)
            aic = 2*k - 2*loglik

            results.append((dist, aic, params))

        except Exception:
            continue

    results.sort(key=lambda x: x[1])

    print("\n" + "="*60)
    print(f"Distribution Fit Results for: {dataset_name}")
    print("="*60)

    for i, (dist, aic, params) in enumerate(results[:top_n], start=1):

        # Separate shape parameters from loc/scale
        shapes = params[:-2] if len(params) > 2 else []
        loc = params[-2] if len(params) >= 2 else None
        scale = params[-1] if len(params) >= 1 else None

        print(f"\n{i}. {dist.name}")
        print(f"   AIC: {aic:.2f}")

        if shapes:
            for j, s in enumerate(shapes):
                print(f"   shape{j+1}: {s:.4f}")

        if loc is not None:
            print(f"   loc:   {loc:.4f}")

        if scale is not None:
            print(f"   scale: {scale:.4f}")

    print("\n(Lower AIC = better fit)")

    return results

# =========================
# TODO 1: Fit Params to Distribution Given
# =========================
fit_and_plot(df["Interarrival Times"], stats.expon, bounds=[(0,10), (0,45)], title="Fitted Interarrivals")

# =========================
# TODO 2: Fit When No Distribution Given
# =========================
candidates = [
    stats.expon,
    stats.gamma,
    stats.invgamma,
    stats.weibull_min,
    stats.lognorm,
    stats.norm,
    stats.uniform,
    stats.triang,
    stats.trapezoid,
    stats.cauchy,
    stats.wald
]

find_best_distribution(df["Service Times for Initial Phase"], candidates, dataset_name="Initial Phase")
find_best_distribution(df["Service Times for Placing Keyboard and Mouse"], candidates, dataset_name="Place Peripherals")
find_best_distribution(df["Service Times for Assembling the Case (Aluminum Plates)"], candidates, dataset_name="Assemble Case")