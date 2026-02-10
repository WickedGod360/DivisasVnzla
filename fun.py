import flet as ft
from bcv_exchange_rates.bcv import get_bcv_exchange_rates
from time import sleep
import threading
from pyperclip import copy

#Controladores

def tasas_bcv():
   try: 
    tasas = get_bcv_exchange_rates()['data']
    usdBCV = round(tasas['dolar']['value'], 2)
    eurBCV = round(tasas['euro']['value'],2)
    fecha = tasas['effective_date']
    timestamp = tasas ['run_timestamp']
    hora = timestamp.split(' ')[1]
    return usdBCV, eurBCV, fecha, hora

   except Exception as e:
      print(f"Error: {e}")
      return usdBCV == 0, eurBCV == 0, fecha == None, hora == None
      
dolar, euro, fecha, hora = tasas_bcv()

def format(numero):
    inicial = "{:,.2f}".format(numero)
    return inicial.replace(",", "X").replace(".", ",").replace("X", ".")


def limpiar(e, bs, usd, eur):
    bs.value=""
    usd.value=""
    eur.value=""   


def formateo(e, destino1, destino2, tasa1, tasa2, origen):
   currencyText = e.control.value.replace(".", "").replace(",", "")
   numero = float(currencyText or 0)
   resultado = numero/100
   currencyTextSHOW = f"{resultado:,.2f}".translate(str.maketrans(",.", ".,"))
   e.control.value = currencyTextSHOW
   if origen == "bs":
        resultadoUSD = resultado / tasa1
        resultadoEUR = resultado / tasa2
        resultadoBS = currencyTextSHOW
        destino1.value = f"{resultadoUSD:,.2f}".translate(str.maketrans(",.", ".,"))
        destino2.value = f"{resultadoEUR:,.2f}".translate(str.maketrans(",.", ".,"))
   elif origen == "usd":
         resultadoBS = resultado * tasa1
         resultadoEUR = resultadoBS / tasa2
         resultadoUSD = currencyTextSHOW
         destino1.value = f"{resultadoBS:,.2f}".translate(str.maketrans(",.", ".,"))
         destino2.value = f"{resultadoEUR:,.2f}".translate(str.maketrans(",.", ".,"))
   elif origen == "eur":
        resultadoBS = resultado * tasa2
        resultadoUSD = resultadoBS / tasa1
        resultadoEUR = currencyTextSHOW
        destino1.value = f"{resultadoBS:,.2f}".translate(str.maketrans(",.", ".,"))
        destino2.value = f"{resultadoUSD:,.2f}".translate(str.maketrans(",.", ".,"))
   e.control.selection_start = len(e.control.value)
   e.control.selection_end = len(e.control.value)
   e.control.update()
   destino1.update()
   destino2.update()


def copiar(e, campo_texto, origen):
    if origen == "txtBox":
        copy(campo_texto.value)
        print(f"{campo_texto.value}")
    elif origen == "USD":
        copy(format(dolar))
        print(f"{format(dolar)}")
    elif origen == "EUR":
        copy(format(euro))
        print(f"{format(euro)}")
        
    if not campo_texto.value == "":
        snack = ft.SnackBar(ft.Text(f"{campo_texto.value} copiado al portapapeles."))
        e.control.page.overlay.append(snack)
        snack.open = True
        e.control.icon = ft.Icons.CHECK_CIRCLE_OUTLINE
        e.control.icon_color = ft.Colors.GREEN_400
        e.control.update()
        e.control.page.update()
    else:
        snack = ft.SnackBar(ft.Text(f"No hay valor para copiar."))
        e.control.page.overlay.append(snack)
        snack.open = True

    def restaurar():
        sleep(1)
        e.control.icon = ft.Icons.COPY
        e.control.icon_color = None # Vuelve al color original
        e.control.update()
        e.control.page.update()

    threading.Thread(target=restaurar, daemon=True).start()


def actualizar_tasas(e, labelUSD, labelEUR, labelFecha):
    e.control.disabled = True
    e.control.icon = ft.Icons.DOWNLOAD
    e.control.update()
    e.control.page.update()
    usd, eur, fecha, hora = tasas_bcv()
    usdNum = "".join([c for c in labelUSD.value if c.isdigit() or c == "." or c == ","]).translate(str.maketrans(",.", ".,"))
    eurNum = "".join([c for c in labelEUR.value if c.isdigit() or c == "." or c == ","]).translate(str.maketrans(",.", ".,"))
    print(f"{usdNum} dolares {usd}//////// {eurNum} euros {eur}")

    if usdNum == str(usd) and eurNum == str(eur):
        snack = ft.SnackBar(ft.Text("No hay cambios en la tasa actual."))
        e.control.page.overlay.append(snack)
        snack.open = True
    else:    
        labelUSD.value = (f"Tasa BCV USD: {format(usd)} Bs")
        labelEUR.value = (f"Tasa BCV EURO: {format(eur)} Bs")
        labelFecha.value = (f"Fecha de la tasa: {fecha}")
        snack = ft.SnackBar(ft.Text("La tasa ha sido actualizada."))
        e.control.page.overlay.append(snack)
        snack.open = True
        print("Se han actualizado los valores")
    
    def restaurar():
        sleep(1)
        e.control.icon = ft.Icons.UPDATE
        e.control.icon_color = None
        e.control.disabled = False
        e.control.update()
        e.control.page.update()

    threading.Thread(target=restaurar, daemon=True).start()