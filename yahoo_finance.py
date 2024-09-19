"""
    ESTE SCRIPT ES UNA IMPLEMENTACION SIMPLE DE LA API ALOJADA EN yahoofinance para python.


    ##cambiar todo lo que esta de aqui para abajo pero tomar como ejemplo.
    EL SCRIPT SIGUIENTE CONSIDERA DIFERENTES OPERACIONES QUE SERAN UTILIZADAS EN MI PROCESOS DE VALORACION DE EMPRESAS, EL SCRIPT PRINCIPAL CON EL USO DE LA LIBRERIA SE PUEDE CONSULTAR EN https://pypi.org/project/yfinance/
    Y TAMBIEN EN LA PAGINA DEL CREADOR. https://aroussi.com/post/python-yahoo-finance.


    LA IMPLEMENTACION ACTUAL CONSISTE EN CONSULTAS SIMPLES SOBRE LA INFORMACION HISTORICA RELEVANTE DE UNA ACCION EN BASE A SU SIMBOLO/CODIGO o TICK CORRESPONDIENTE INSCRITO EN LA NYSE.
    -- EN DESARROLLO --
    LA IMPLEMENTACION CONSIDERA LAS SIGUIENTES FUNCIONES:
        - OBTIENE TODA LA INFORMACION BASICA QUE SE TIENE REGISTRO EN https://finance.yahoo.com/ PARA UNA ACCION DETERMINADA (EN EL CODIGO LA VARIABLE ticker)
        - GRAFICA DEL COMPORTAMIENTO DEL PRECIO DE UNA ACCION EN PERIODOS ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        - GRAFICA DEL COMPORTAMIENTO DEL PRECIO DE UNA ACCION EN TODOS LOS PERIODOS ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        
    ####### EN DESARROLLO ########
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
import datetime as dt
import math as mt

ticker = "MSFT"
msft = yf.Ticker("MSFT")  # Indica la accion a consultar.

########################################
#### FUNCIONES BASICAS DE DATOS    #####
########################################
# OBTIENE LA INFORMACION GENERAL SOBRE LA EMPRESA DESDE UN DICCIONARIO Y LO FORMATEA


def ObtenerInformacion(ticker):
    LARGO_TXT = 100  # largo
    print(
        f"INFORMACION FINANCIERA DE {ticker} AL DIA DE :  {str(dt.datetime.now().date())}")
    print("\n")
    ticker = yf.Ticker(ticker)
    for keys, values in ticker.info.items():
        # Imprime en el formato necesario la informacion correspondiente al negocio.
        if str(keys) == 'longBusinessSummary':
            print(f" -- {keys} :")
            for i in range(0, len(values), LARGO_TXT):
                print(f"       {values[i:i+LARGO_TXT]}")
        # Imprime en el formato necesario la informacion de los principales ejecutivos.
        elif str(keys) == 'companyOfficers':
            print(f" -- {keys}")
            print("\n")
            # ** OJO: AQUI VIENE UNA LISTA CON LOS EJECUTIVOS PRINCIPALES ***/
            for exec in range(0, len(ticker.info["companyOfficers"])):
                for keys1, values1 in ticker.info["companyOfficers"][exec].items():
                    if keys1 != "maxAge":
                        print(f"    -- {keys1} : {values1}")
                print("\n")
        # imprime el diccionario normalmente
        else:
            print(f" -- {keys} : {values}")


####################################################################
#### OBTIENE EL VALOR DE LA STOCK PARA UN PERIODO DETERMINADO  #####
####################################################################
# RECIBE EL VALOR DE CODIGO DE UNA ACCION Y UN PERIODO

# PARA TENER EN CONSIDERACION ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
def ObtenerPeriodo(ticker, number):
    ticker_ob = yf.Ticker(ticker)
    per = str(number)
    hist = ticker_ob.history(period=str(per))
    # Se puede hacer un grafico para ver como se ha comportado
    df_hist = pd.DataFrame(data=hist)
    # print(df_hist)
    # Genera visualizacion
    sns.lineplot(df_hist, x=df_hist.index, y=df_hist['Close'])
    # Format
    plt.suptitle("Valor de " + ticker +
                 " en dólares (Cierre sesión). Periodo: " + per)
    plt.ylabel("Valor de " + ticker + " en dólares (Cierre sesión).")
    plt.xlabel("Fecha(AAAAMM)")
    # Mueve los valores del eje X
    plt.tick_params(axis='x', rotation=45)
    # Show
    plt.show()


# PARA TENER EN CONSIDERACION ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
def ObtenerUltimoMes(ticker, number):
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

# OBTIENE EL VALOR DE CIERRE DE UN PERIODO EN ESPECIFICO (OJO, AQUI RETORNA UN TIPO DE DATO DIFERENTE COMO PRODUCTO)


# PARA TENER EN CONSIDERACION ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
def ObtenerPeriodoStock(ticker, number):
    ticker_ob = yf.Ticker(ticker)
    # FALTA
    per = str(number)
    # Revisar que otras opciones tengo
    hist = ticker_ob.history(period=str(per))
    # Se puede hacer un grafico para ver como se ha comportado
    # df_hist = pd.DataFrame(data=hist)
    return hist['Close']


def ObtenerGraficosHistoricos(ticker):
    N_ROWS = 2  # Q Filas
    N_COL = 5  # Q Columnas
    periods = ['5d', '1mo', '3mo', '6mo',
               '1y', '2y', '5y', '10y', 'ytd', 'max']

    # Graph
    fig, axes = plt.subplots(nrows=N_ROWS, ncols=N_COL, figsize=(
        20, 15), sharex=False, sharey=False)
    fig.suptitle(f"Evolucion de la compañia: {ticker} - Periodos : {periods} ")
    min_val = 0
    max_val = 0

    # VISUALIZATION

    for i in range(0, N_ROWS):
        if i == 0:  # Fast Sol: Se dividen en 2 los ejes asi se pueden informar
            per = ['5d', '1mo', '3mo', '6mo', 'ytd']
        else:
            per = ['1y', '2y', '5y', '10y', 'max']
        for j in range(0, N_COL):
            # Obtener Datos
            data = ObtenerPeriodoStock(ticker, per[j])

            # Grafica la informacion obtenida
            axes[i, j].plot(data)
            axes[i, j].set_title(per[j])

            # Ajusta el valor maximo y minimo de Y segun el valor maximo de los datos

            min_val = data.min() * 0.95
            max_val = data.max() * 1.05
            # Ajustar con un margen del 5%
            axes[i, j].set_ylim([min_val, max_val])

            # Si es de la primera fila
            if (i == 0) or (per[j] in ('2y', '1y')):
                # Se ajusta el valor del eje Y para obtener una mejor visualizacion
                axes[i, j].tick_params(axis='x', rotation=45)

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar los márgenes
    plt.show()


ObtenerGraficosHistoricos(ticker)


# ObtenerUltimoMes(ticker, 6)


# # show meta information about the history (requires history() to be called first)
# msft.history_metadata # Indica cuando se actualiza
# # show actions (dividends, splits, capital gains)
# actions = pd.DataFrame(data=msft.actions)
# print(actions)
# # msft.dividends
# dividends = pd.DataFrame(data=msft.dividends)
# print(dividends)
# # msft.splits
# splits = pd.DataFrame(data=msft.splits)
# print(splits)
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
