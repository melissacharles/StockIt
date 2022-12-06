## 📌 StockIt

### Table of contents

- Introduction
- Requirements
- Installation
- How To Use


### Introduction

This module provides a framework to easily visualize a stock price and volume for any stock, as well as, stock market recommendations based off of analyst ratings. The web application will display a Pandas dataframe containing daily historical stock data including open price, close price, high, low and volume.

- Submit bug reports and feature suggestions, or track changes email
  melissacharles.py@gmail.com
  
 ### Requirements

This module requires the following dependencies:

- [Streamlit](https://www.https://streamlit.io/)
- [Python](https://www.python.org/downloads/release/python-3110/)

### Installation

Install **Steamlit** locally as you would normally install an open source framework. 
  *Open a terminal window* >
  
    $ pip install streamlit
    $ streamlit hello

Next, install **yfinance** locally via terminal for data that will be pulled:

    $ pip install yfinance
    
### How To Use
 - Clone this repository
 - Follow installation steps
 - In main.py file, change tickerSymbol to stock of choice. 
 - Run application in terminal by entering following command:
    
    $ streamlit run stockit.py

  - Optional: Sort chart by date, zoom in and out or expand chart
