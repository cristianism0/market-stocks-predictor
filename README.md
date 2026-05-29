# Monte Carlo Portfolio Simulation

Monte Carlo simulation applied to portfolio value forecasting over time.
Uses Cholesky decomposition to preserve asset correlation during sampling.

## What it does

- Downloads 10 years of historical data for 10 stocks via `yfinance`
- Calculates daily returns, mean and covariance matrix
- Runs N simulated portfolio trajectories over 2520 trading days (~10 years)
- Plots all simulated trajectories on a single chart

## How to run

```bash
pip install yfinance pandas numpy matplotlib
python src/main.py
```

Requires an internet connection to fetch data from Yahoo Finance.

## Limitations

- Portfolio weights are randomly generated at each run — no optimization is performed
- The model assumes future returns follow the same historical distribution, which rarely holds
- Does not account for transaction costs, dividends or stock splits
- Not suitable for real financial decisions

## Context

Study project for Python, Pandas and NumPy. The focus was understanding the mechanics of Monte Carlo simulation and the practical application of Cholesky decomposition for correlation between time series.