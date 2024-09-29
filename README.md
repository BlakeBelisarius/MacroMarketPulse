## MacroMarketPulse

This repository contains projects analyzing financial market movements driven by macroeconomic factors, both common and uncommon, such as interest rates, inflation, the yield curve, and money supply. Explore the impact of economic trends on market dynamics using Python for data analysis, visualizations, and predictive models.

### Projects Overview

1. **SPY Natural Log Returns and Macroeconomic Indicators**:
   - Study the relationships between SPY natural log returns and macroeconomic variables such as the Yield Curve and the 10-Year Treasury Constant Maturity Rate (GS10).
   - Use statistical and correlation analysis to identify trends.
   - Implement regression models to quantify the influence of these indicators on market returns.

2. **Federal Reserve Policy and Equity Market Reactions**:
   - Analyze how Federal Reserve interest rate decisions impact equity markets.
   - Explore the lagging effects of policy changes on market volatility and sector performance.
   - Use time series analysis and predictive modeling to understand market movements post-Fed meetings.

3. **Inflation Trends and Commodity Prices**:
   - Investigate the correlation between inflation data (CPI, PCE) and commodity prices (e.g., oil, gold).
   - Perform regression and rolling correlation analysis to track how inflationary pressures affect commodity markets over time.

4. **Yield Curve Inversion and Recession Signals**:
   - Examine the predictive power of yield curve inversions (e.g., 10Y-2Y spread) for recessions.
   - Backtest historical yield curve data to evaluate its performance as a recession indicator and its impact on equities and bonds.

5. **Money Supply (M2) and Asset Price Inflation**:
   - Study the relationship between changes in money supply (M2) and inflation in asset classes such as stocks, real estate, and cryptocurrencies.
   - Use visualization and correlation metrics to explore how liquidity injections influence asset bubbles and market performance.

### Features
- **Statistical Analysis**: Explore the relationships between various macroeconomic indicators and financial market movements.
- **Correlation and Regression Models**: Identify and quantify how different economic factors affect market trends.
- **Data Visualization**: Generate time series charts, scatter plots, heatmaps, and more to visualize economic impacts on markets.
- **Predictive Models**: Use machine learning models (e.g., regression) to predict market behavior based on economic data.
- **Backtesting**: Backtest economic data to evaluate historical performance of certain indicators in predicting market trends.

### Directory Tree

```plaintext
MacroMarketPulse/
│
├── data/
│   └── <raw and cleaned data files>
│
├── notebooks/
│   └── spy_macro_analysis.ipynb
│   └── fed_policy_equity_reaction.ipynb
│   └── inflation_commodity_analysis.ipynb
│   └── yield_curve_recession_signals.ipynb
│   └── money_supply_asset_prices.ipynb
│
├── src/
│   └── analysis.py
│   └── data_preprocessing.py
│   └── visualization.py
│
├── README.md
├── requirements.txt
└── LICENSE
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MacroMarketPulse.git
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. For PyTorch, it's best to install it manually. You can run:
   ```bash
   pip install torch torchvision torchaudio
   ```

### Usage
- Each project is contained within a Jupyter notebook under the `notebooks/` directory.
- To run the analyses, open the desired notebook and execute the cells.
- Use the scripts under `src/` for custom analyses and data preprocessing.

### Data Sources
- **Yahoo Finance**: Stock market data (SPY and others).
- **FRED API**: Macroeconomic indicators (Yield Curve, Interest Rates, CPI, etc.).
- **Other sources**: Data from other publicly available financial data platforms.

### License

This project is licensed under the **MIT License**.