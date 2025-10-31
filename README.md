# KO Stock Analysis & Long-Term Trend Confirmation

**Analyzed Coca-Cola (KO) stock history and fundamentals. Calculated key technical indicators (SMA 50/200) to confirm a long-term bullish trend and identify strategic entry points for investors.**

---

## Project Motivation and Goal

The Coca-Cola Company (KO) is a defensive blue-chip stock, but understanding its long-term direction and volatility is key for investors.

This project's goal is to provide a comprehensive **Data Analysis** of KO's historical performance to generate **actionable, data-driven investment insights** by:

1.  **Technical Analysis:** Calculating and visualizing key technical indicators (Simple Moving Averages) to confirm trend strength.
2.  **Performance Analysis:** Analyzing price trends, volume spikes, and volatility patterns.
3.  **Investor Strategy:** Concluding with clear recommendations for long-term and short-term traders.

## Data and Methodology

### Datasets

| File Name | Description |
| :--- | :--- |
| `Coca-Cola_stock_history.csv` | Contains daily historical stock prices (Open, High, Low, Close, Volume) used for all technical indicator calculations. |
| `Coca-Cola_stock_info.csv` | Contains fundamental information (e.g., sector, beta, profit margins) used for foundational context. |

### Methodology

* **Time-Series Processing:** The historical data was loaded, cleaned, and the 'Date' column was converted to a proper index to ensure accurate time-series calculations.
* **Key Indicator:** The **50-Day and 200-Day Simple Moving Averages (SMA)** were calculated to define short-term momentum and long-term support/resistance levels.
* **Analysis Focus:** The analysis centered on the relationship between the price and the 200-Day SMA, which is a classic signal for a sustained **bullish trend**.

## Get Started

### Prerequisites

You will need Python 3.x and the following libraries:

```bash
pip install pandas numpy matplotlib seaborn
