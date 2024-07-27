"""
    ESTE SCRIPT ES UNA IMPLEMENTACION SIMPLE DE LA API ALOJADA EN yahoofinance para python.


    ##cambiar todo lo que esta de aqui para abajo pero tomar como ejemplo.
    EL SCRIPT SIGUIENTE CONSIDERA DIFERENTES OPERACIONES QUE SERAN UTILIZADAS EN MI PROCESOS DE VALORACION DE EMPRESAS, EL SCRIPT PRINCIPAL CON EL USO DE LA LIBRERIA SE PUEDE CONSULTAR EN https://pypi.org/project/yfinance/
    Y TAMBIEN EN LA PAGINA DEL CREADOR. https://aroussi.com/post/python-yahoo-finance.


    LA IMPLEMENTACION ACTUAL CONSISTE EN CONSULTAS SIMPLES SOBRE LA INFORMACION HISTORICA RELEVANTE DE UNA ACCION EN BASE A SU SIMBOLO O CODIGO CORRESPONDIENTE INSCRITO EN LA NYSE.
    -- EN DESARROLLO --
    LA IMPLEMENTACION CONSIDERA LAS SIGUIENTES FUNCIONES:
        - OBTIENE TODA LA INFORMACION BASICA QUE SE TIENE REGISTRO EN https://finance.yahoo.com/ .
        - OBTENER EL ULTIMO MES DE COMPORTAMIENTO DEL ACTIVO EN BASE A SU SIMBOLO ORIGINAL.
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


def ObtenerInformacion(ticker):
    ticker = yf.Ticker(ticker)
    for keys, values in ticker.info.items():
        # Imprime en el formato necesario la informacion de los principales ejecutivos
        if str(keys) == 'companyOfficers':
            print('companyOfficers:')
           /** OJO: AQUI VIENE UNA LISTA CON LOS EJECUTIVOS PRINCIPALES ***/
            for exec in range(0, len(ticker.info["companyOfficers"])):
                for keys1, values1 in ticker.info["companyOfficers"][exec].items():
                    print("         "+str(keys1) + ": " + str(values1))
                print("\n")
        # imprime el diccionario normalmente
        else:
            print(str(keys) + ": " + str(values))


# ObtenerInformacion(ticker=ticker)

# get historical market data

def ObtenerUltimoMes(ticker, number): ##PARA TENER EN CONSIDERACION ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    ticker_ob = yf.Ticker(ticker)
    per = str(number) + 'mo'
    # Revisar que otras opciones tengo
    hist = ticker_ob.history(period=str(per))
    # Se puede hacer un grafico para ver como se ha comportado
    df_hist = pd.DataFrame(data=hist)
    # print(df_hist)
    # Genera visualizacion
    sns.lineplot(df_hist, x=df_hist.index, y=df_hist['Close'])
    # Format
    plt.suptitle("Valor de " + ticker +
                 " en dólares (Cierre sesión). Ult mes")
    plt.ylabel("Valor de " + ticker + " en dólares (Cierre sesión).")
    plt.xlabel("Valor de " + ticker + " por fecha.")
    # Show
    plt.show()

# ObtenerUltimoMes(ticker, 6)


# # show meta information about the history (requires history() to be called first)
# msft.history_metadata # Indica cuando se actualiza


# # show actions (dividends, splits, capital gains)
actions = pd.DataFrame(data=msft.actions)
print(actions)
# msft.dividends
dividends = pd.DataFrame(data=msft.dividends)
print(dividends)
# msft.splits
splits = pd.DataFrame(data=msft.splits)
print(splits)
# msft.capital_gains  # only for mutual funds & etfs
# cap_gains = pd.DataFrame(data=msft.capital_gains)
# print(cap_gains)

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
