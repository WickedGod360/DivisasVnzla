import flet as ft
import widgets as wg
import fun

# NOTA: Las funciones lambda y la lógica de negocio se quedan aquí afuera, 
# pero la CREACIÓN de los widgets y la petición al BCV DEBEN ocurrir dentro de main.

def main(page: ft.Page):
    # 1. Configuración de la página e Icono corregido
    page.fonts = {"Euclid Square": "/fonts/EuclidSquare-Regular.ttf"}
    page.theme = ft.Theme(font_family="Euclid Square")
    page.theme.visual_density = ft.VisualDensity.COMPACT
    page.window.width = 500
    page.window.height = 600
    page.window.resizable = True
    page.window.icon = "/icon.png"  
    page.title = "Divisas Venezuela"
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # 2. Carga de datos de red (Web Scraping) al iniciar la sesión
    dolar, euro, fecha, hora = fun.tasas_bcv()
    fecha_modif = fecha.replace("  ", " ")
        
    # 3. Instanciación de Widgets (Ahora sí asociados a esta instancia de 'page')
    tasa = wg.tasa_usd(dolar)
    tasa_bcv_eur = wg.tasa_euro(euro)
    fecha_tasa = wg.fecha_tasa(fecha_modif)

    bs = wg.tbox_bolivares()
    usd = wg.tbox_usd()
    eur = wg.tbox_euros()

    # 4. Asignación de Eventos (on_change)
    bs.on_change = lambda e: fun.formateo(e, usd, eur, dolar, euro, "bs")
    usd.on_change = lambda e: fun.formateo(e, bs, eur, dolar, euro, "usd")
    eur.on_change = lambda e: fun.formateo(e, bs, usd, dolar, euro, "eur")

    btn_bs = wg.btn_copiar_bs()
    btn_usd = wg.btn_copiar_usd()
    btn_eur = wg.btn_copiar_euro()
    btn_copiar_tasa_usd = wg.btn_copiar_tasa_usd()
    btn_copiar_tasa_eur = wg.btn_copiar_euro()
    btn_limpiar = wg.btn_limpiar()
    btn_actualizar_tasa = wg.btn_actualizar_tasa()

    # 5. Asignación de Eventos (on_click)
    btn_bs.on_click = lambda e: fun.copiar(e, bs, "txtBox")
    btn_usd.on_click = lambda e: fun.copiar(e, usd, "txtBox")
    btn_eur.on_click = lambda e: fun.copiar(e, eur, "txtBox")
    btn_copiar_tasa_usd.on_click = lambda e: fun.copiar(e, tasa, "USD")
    btn_copiar_tasa_eur.on_click = lambda e: fun.copiar(e, tasa_bcv_eur, "EUR")
    btn_limpiar.on_click = lambda e: fun.limpiar(e, bs, usd, eur)
    btn_actualizar_tasa.on_click = lambda e: fun.actualizar_tasas(e, tasa, tasa_bcv_eur, fecha_tasa)

    # 6. Construcción de la Interfaz
    contenedor = ft.Container(
        ft.Column([
            ft.Row([tasa, btn_copiar_tasa_usd], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([tasa_bcv_eur, btn_copiar_tasa_eur], alignment=ft.MainAxisAlignment.CENTER), 
            ft.Divider(height=30, color=ft.Colors.WHITE),
            ft.Row([bs, btn_bs], alignment=ft.MainAxisAlignment.CENTER),   
            ft.Row([usd, btn_usd], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([eur, btn_eur], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(height=20, color=ft.Colors.WHITE),
            ft.Row([fecha_tasa], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([btn_limpiar, btn_actualizar_tasa], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
        bgcolor=ft.Colors.with_opacity(0.1, color="#414141"),
        padding=10,
        border_radius=10,
        width=450,
        expand=True
    )
    
    page.add(contenedor)
    page.window.center()
    page.update()

if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir="assets",
        view=ft.AppView.FLET_APP
    )