import flet as ft
import widgets as wg
import fun


def main (page: ft.Page):
    page.fonts = {"Euclid Square": "/fonts/EuclidSquare-Regular.ttf"}
    page.theme = ft.Theme(font_family="Euclid Square")
    page.theme.visual_density = ft.VisualDensity.COMPACT
    page.window.width = 530
    page.window.height = 700
    page.window.resizable = True
    page.window.icon = "icon.ico"
    page.update()
    page.title = "Divisas Venezuela"
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    dolar, euro, fecha, hora = fun.tasasBCV()
    fechaModif=fecha.replace("  ", " ")
    
    tasa = wg.tBCV(dolar)
    tasaBCVEur = wg.tBCVEur(euro)
    fechaTasa = wg.fechaTasa(fechaModif)

    bs = wg.tboxBolivares()
    usd = wg.tboxUSD()
    eur = wg.tboxEuros()

    bs.on_change = lambda e: fun.formateo(e, usd, eur, dolar, euro, "bs")
    usd.on_change = lambda e: fun.formateo(e, bs, eur, dolar, euro, "usd")
    eur.on_change = lambda e: fun.formateo(e, bs, usd, dolar, euro, "eur")

    btnBS = wg.btnCopyBS()
    btnUSD = wg.btnCopyUSD()
    btnEUR = wg.btnCopyEUR()
    btnCopyTasa = wg.btnCopyTasaBCV()
    btnCopyTasaEUR = wg.btnCopyEUR()
    btnLimpiarTodo = wg.btnLimpiarTodo()
    btnActualizarTasa = wg.btnActualizarTasa()

    btnBS.on_click = lambda e: fun.copiar(e, bs, "txtBox")
    btnUSD.on_click = lambda e: fun.copiar(e, usd, "txtBox")
    btnEUR.on_click = lambda e: fun.copiar(e, eur, "txtBox")
    btnCopyTasa.on_click = lambda e: fun.copiar(e, tasa, "USD")
    btnCopyTasaEUR.on_click = lambda e: fun.copiar(e, tasaBCVEur, "EUR")
    btnLimpiarTodo.on_click = lambda e: fun.limpiar(e, bs, usd, eur)
    btnActualizarTasa.on_click = lambda e: fun.actualizarTasas(e, tasa, tasaBCVEur, fechaTasa)

    contenedor = ft.Container(
      ft.Column([
        ft.Row([tasa, btnCopyTasa], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([tasaBCVEur, btnCopyTasaEUR], alignment=ft.MainAxisAlignment.CENTER), 
        ft.Divider(height=30, color=ft.Colors.WHITE),
        ft.Row([bs, btnBS], alignment=ft.MainAxisAlignment.CENTER),   
        ft.Row([usd, btnUSD], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([eur, btnEUR], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color=ft.Colors.WHITE),
        ft.Row([fechaTasa], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btnLimpiarTodo, btnActualizarTasa], alignment=ft.MainAxisAlignment.CENTER)
      ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor=ft.Colors.with_opacity(0.1, color="#414141"),
        padding=30,
        border_radius=10,
        border=ft.border.all(2, ft.Colors.GREY_800),
        width=450)
    
    page.add(contenedor)
    page.window.center()
    page.update()
ft.app(target=main,
       assets_dir="assets",
      view=ft.AppView.FLET_APP)