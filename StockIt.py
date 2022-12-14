import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# StockIt Application
Shown are the stock **closing price** and ***volume*** of Apple! 
Bonus: Stock **Recommendations**
""")

#define the ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2012-12-6', end='2022-12-6')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Recent Market Ratings
""")
tickerData.recommendations