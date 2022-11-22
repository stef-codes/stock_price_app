import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
 # Stock Price App

Shown are the stock closing price and volume of Google!

"""
)

tickersymbol = 'GOOGL'

tickerdata = yf.Ticker(tickersymbol)

tickerDf = tickerdata.history(period='id', start='2020-5-03', end='2022-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
