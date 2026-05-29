import data_get as dg
import numpy as np
import matplotlib.pyplot as plt

stocks = dg.data_request()

covReturns, meanReturns = dg.calc_returns(stocks)

MC_sim = 100  #start
T = 252*10   #timeframe in working days
inPortfolio = 10000 #dolars

weights= np.random.random(len(meanReturns))
weights /= np.sum(weights)

def start_MC(inPortfolio,weights, meanReturns, covMatrix, MC_sim, T):
    """MC Simulation"""
    import numpy as np
    meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)
    meanM = meanM.T             #meanMatrix = meanMatrix.Transposed
    
    portfolio_sim = np.full(shape=(T, MC_sim), fill_value=0.0)
    for m in range(0, MC_sim):
        Z = np.random.normal(size=(T, len(weights)))
        L = np.linalg.cholesky(covMatrix)
        dailyReturns = meanM + np.inner(L, Z)
        portfolio_sim[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*inPortfolio
    return portfolio_sim

portfolio_sim = start_MC(inPortfolio, weights, meanReturns, covReturns, MC_sim, T)
    
plt.plot(portfolio_sim)
plt.ylabel("Portfolio Value (US$)")
plt.xlabel("Days")
plt.title("MC Simulation for Portfolio")
plt.show()