"""
    ESTE SCRIPT ES UNA IMPLEMENTACION SIMPLE DE LA API ALOJADA EN yahoofinance para python.

    
    ##cambiar todo lo que esta de aqui para abajo pero tomar como ejemplo.
    LA IMPLEMENTACION ACTUAL CONSISTE EN CONSULTAS SIMPLES QUE SERAN EJECUTADAS POR UN BOT DE TELEGRAM
    -- EN DESARROLLO --
    LA IMPLEMENTACION CONSIDERA 3 FUNCIONES GENERALES:
        - CONSULTA DEL VALOR ACTUAL DE LOS INDICADORES DISPONIBLES, SEGUN LA WEB DE https://mindicador.cl/
        - CONSULTA EL VALOR DE LOS ULTIMOS 30 DIAS.
        - CONSULTA EL VALOR DE LOS INDICADORES PARA UNA FECHA EN ESPECIFICO. TAMBIEN LA FUNCION SE ENCUENTRA EN DISPONIBLE PARA CONSULTAR CON UN SOLO INDICADOR.
        - CONSULTA EL VALOR DE UN INDICADOR PARA UN AÑO EN ESPECIFICO.
        - LOS INDICADORES DISPONIBLES SON: ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc","utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"]. PARA MAS DETALLE CONSULTAR mindicador.cl
        - TODAS LAS FUNCIONES RETORNAN UN OBJETO DE TIPO DICCIONARIO QUE PERMITE FACILMENTE TRABAJAR CON EL (ESTE SE PENSO PARA TRABAJAR CON PANDAS Y SEABORN)
    Returns:
        _type_: _description_
    """

import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ticker = "MSFT"
msft = yf.Ticker("MSFT")  # Indica la accion a consultar.

# get all stock info (LA API VIENE COMO UN DICCIONARIO):


# def ObtenerInformacion(ticker):
#     ticker = yf.Ticker(ticker)
#     for keys, values in ticker.info.items():
#         print(str(keys) + ": " + str(values))


# ObtenerInformacion(ticker=ticker)

# get historical market data


# def ObtenerUltimoMes(ticker, number): ##PARA TENER EN CONSIDERACION ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
#     ticker_ob = yf.Ticker(ticker)
#     per = str(number) + 'mo'
#     # Revisar que otras opciones tengo
#     hist = ticker_ob.history(period=str(per))
#     # Se puede hacer un grafico para ver como se ha comportado
#     df_hist = pd.DataFrame(data=hist)
#     # print(df_hist)
#     # Genera visualizacion
#     sns.lineplot(df_hist, x=df_hist.index, y=df_hist['Close'])
#     # Format
#     plt.suptitle("Valor de " + ticker +
#                  " en dólares (Cierre sesión). Ult mes")
#     plt.ylabel("Valor de " + ticker + " en dólares (Cierre sesión).")
#     plt.xlabel("Valor de " + ticker + " por fecha.")
#     # Show
#     plt.show()

# ObtenerUltimoMes(ticker, 6)


# # show meta information about the history (requires history() to be called first)
msft.history_metadata

# hist = msft.history(period="6m")

# print(msft.history(period="6m").history_metadata)

# # show actions (dividends, splits, capital gains)
# msft.actions
# msft.dividends
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs

# # show share count
# msft.get_shares_full(start="2022-01-01", end=None)

# # show financials:
# # - income statement
# msft.income_stmt
# msft.quarterly_income_stmt
# # - balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet
# # - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# # see `Ticker.get_income_stmt()` for more options

# # show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders
# msft.insider_transactions
# msft.insider_purchases
# msft.insider_roster_holders

# # show recommendations
# msft.recommendations
# msft.recommendations_summary
# msft.upgrades_downgrades

# # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
# # Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
# msft.earnings_dates

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# msft.isin

# # show options expirations
# msft.options

# # show news
# msft.news

# get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
