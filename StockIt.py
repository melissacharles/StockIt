import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime
import requests

st.markdown('''
# StockIt Application
Shown are the stock **open price**, **close price** and ***volume*** of any S&P500 Stock! 
Bonus: Stock **Recommendations**
''')

st.write('---')

# Side Panel
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2022, 3, 4))
end_date = st.sidebar.date_input("End date", datetime.date(2023, 3, 4))

# Pulling ticker data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/melissacharles/StockIt/main/ticker_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol

api_key = 'e768af1e7d6c1a0be2544a1602e896db21f7cccc'
url = f'https://api.tiingo.com/tiingo/daily/{tickerSymbol}/prices?startDate={start_date}&endDate={end_date}&token={api_key}'

response = requests.get(url)
tickerDf = pd.read_json(response.content.decode('utf-8'))

# Ticker Info
st.header(f"**{tickerSymbol}**")
st.write(f"Data for {start_date} - {end_date}")

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
