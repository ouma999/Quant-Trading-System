# Stock-prediction-Architecture
A hybrid ensemble machine learning system that trains on historical CSV data and generates live stock predictions using real-time Yahoo Finance data.
Project pipleine 
Your CSV Files(API)                   Yahoo Finance
      |                                 |
      | (years of history)              | (latest 300 days)
      |                                 |
      v                                 v
Train Ensemble Model    -->    Build Live Features
  (RF + GB + LR)                        |
                                        v
                               Predict with Trained Model
                                        |
                                        v
                               Summary Table + Charts
1.APIs
   ↓
2.Data Pipeline
   ↓
3.Feature Engineering
   ↓
4.ML Model-Gradient Boosting, XGBoost or RF libraries skitlearn 
   ↓
5.Strategy Logic:if prediction > 0.6 buy or if prediction < 0.4 sell
   ↓
6.Backtesting-Libraries:BacktraderZipline
Metrics:Sharpe ratio,max drawdown,win rate and annual return
   ↓
7.Dashboard- streamlit/plotly

<img width="511" height="336" alt="image" src="https://github.com/user-attachments/assets/babd06f5-4846-4fb6-8c29-0c81bb64298d" />



This project uses an Ensemble Model combining three algorithms for robust, diversified predictions:
ModelTypeStrengthRFRandom ForestHandles non-linear patterns, resistant to overfittingGBGradient BoostingHigh accuracy on structured data, captures complex relationshipsLRLogistic RegressionFast, int

Current Model Performance
MetricValueCurrent Accuracy52% (baseline — v1.0)
Target Accuracy58% – 65% (planned v2.0)
Status Under Active Optimization

The current model establishes a working baseline at 52% accuracy. Future iterations will target the 58–65% range through the following improvements:

Hyperparameter tuning (GridSearchCV / Optuna)
Additional technical indicators (RSI, MACD, Bollinger Bands, Volume Trends)
Improved class imbalance handling (SMOTE / resampling)
Feature selection refinement (drop low-importance features)
Expanding training window / adding more ticker diversity
Experimenting with LSTM or time-series-specific models


