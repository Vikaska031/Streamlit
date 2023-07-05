import yfinance as yf
import streamlit as st

st.write("""
# Простое приложение для цен на акции

Показаны акции **цена закрытия** и **объем** акций Apple!
Сделано Ивановой Викаськой

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.image("https://i.pinimg.com/originals/40/d4/e2/40d4e2065c357bd9c5d5b85b0efeb445.jpg", caption="Улыбнись")

