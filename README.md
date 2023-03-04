## 📌 StockIt

### Table of contents

- Introduction
- Requirements
- Installation
- How To Use


### Introduction

This is a Python-based web application using the Streamlit library that retrieves stock prices and information using the Tiingo API, and displays it along with Bollinger Bands charts and stock recommendations for any S&P500 stock selected. The application allows for query parameters to be selected via a side panel and the stock ticker to be selected from a web-based text file.

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

Next, install the **pandas**, **requests** and **cufflinks** libraries to run this code locally. You can install these libraries by running the following command in your command prompt or terminal::

    $ pip install pandas requests cufflinks
    
### How To Use
 - Clone this repository
 - Follow installation steps
 - In main.py file, change tickerSymbol to stock of choice. 
 - Run application in terminal by entering following command:
    
    $ streamlit run stockit.py

  - Optional: Sort chart by date, zoom in and out or expand chart
