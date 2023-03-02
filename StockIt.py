import yfinance as yf
import streamlit as st
import pandas as pd
import cuffLinks as cf
import datetime


st.markdown('''
# StockIt Application
Shown are the stock **open price**, **close price** and ***volume*** of any S&P500 Stock! 
Bonus: Stock **Recommendations**
''')

st.write('---')

#Side Panel
st.sidebar.subheader('Stock Parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2013, 3, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2023, 3, 1))

#Pulling ticker data
ticker_list = pd.read_csv



tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(
    period='1d', 
    start='2012-3-1', 
    end='2023-3-1')

st.write("""
### Open Price
""")
st.line_chart(tickerDf.Open)

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