import flet as ft
import fun

dolar, euro, fecha, hora = fun.tasasBCV()

#Fila #1 y 1.5 (?), Tasa BCV USD y EUR y boton de copiar las tasas
def tBCV(dolar1): return ft.Text(f"Tasa BCV USD: {fun.format(dolar1)} Bs",
                        size=22,
                        color=ft.Colors.LIGHT_BLUE_200)

def btnCopyTasaBCV(): return ft.IconButton(icon=ft.Icons.COPY,
                        icon_color=ft.Colors.WHITE,
                        tooltip="Copiar Tasa DOLAR")

def tBCVEur(euro1): return ft.Text(f"Tasa BCV EURO: {fun.format(euro1)} Bs",
                        size=22,
                        color=ft.Colors.LIGHT_BLUE_200)

def btnCopyTasaBCVEUR(): return ft.IconButton(icon=ft.Icons.COPY,
                        icon_color=ft.Colors.WHITE,
                        tooltip="Copiar Tasa EURO")


#Fila #2, Campo de texto para ingresar bolivares y boton de copiar
def tboxBolivares(): return ft.TextField(label="Bolívares",
                        text_align=ft.TextAlign.RIGHT, width=200,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9,.]", replacement_string=""),
                        keyboard_type=ft.KeyboardType.NUMBER,
                        hint_text="0.00",
                        on_change=fun.formateo,
                        prefix_icon=ft.Icons.MONETIZATION_ON,
                        border_radius=10,
                        focused_border_color=ft.Colors.YELLOW_900,
                        border_color=ft.Colors.YELLOW_500,
                        expand=True,
                        content_padding=15
                        )
def btnCopyBS(): return ft.IconButton(icon=ft.Icons.COPY,
                        icon_color=ft.Colors.WHITE
                        )

#fila #3, Campo de texto para ingresar USD y boton de copiar
def tboxUSD(): return ft.TextField(label="USD",
                        text_align=ft.TextAlign.RIGHT, width=200,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9,.]", replacement_string=""),
                        keyboard_type=ft.KeyboardType.NUMBER,
                        hint_text="0.00",
                        on_change=fun.formateo,
                        prefix_icon=ft.Icons.MONETIZATION_ON,
                        border_radius=10,
                        focused_border_color=ft.Colors.YELLOW_900,
                        border_color=ft.Colors.YELLOW_500,
                        expand=True,
                        content_padding=15
                        )
def btnCopyUSD (): return ft.IconButton(icon=ft.Icons.COPY,
                        icon_color=ft.Colors.WHITE
                        )

#Fila #4, Campo de texto para ingresar USD y boton de copiar
def tboxEuros(): return ft.TextField(label="Euros",
                        text_align=ft.TextAlign.RIGHT, width=200,
                        input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9,.]", replacement_string=""),
                        keyboard_type=ft.KeyboardType.NUMBER,
                        hint_text="0.00",
                        on_change=fun.formateo,
                        prefix_icon=ft.Icons.MONETIZATION_ON,
                        border_radius=10,
                        focused_border_color=ft.Colors.YELLOW_900,
                        border_color=ft.Colors.YELLOW_500,
                        expand=True,
                        content_padding=15                        
                        )
def btnCopyEUR(): return ft.IconButton(icon=ft.Icons.COPY,
                        icon_color=ft.Colors.WHITE
                        )

#fila #5, fecha de la pasa
def fechaTasa(fechatasa): return ft.Text(f"Fecha de la tasa:  {fechatasa}",
                        size=20)

def horaTasa(horatasa): return ft.Text(f"Hora de la tasa: {horatasa}",
                        size=20)

#fila #6 botones de limpiar y actualizar
def btnLimpiarTodo(): return ft.IconButton(icon=ft.Icons.DELETE_SWEEP_OUTLINED,
                        icon_color=ft.Colors.RED_400,
                        icon_size=30,
                        tooltip="Limpiar todo")

def btnActualizarTasa(): return ft.IconButton(icon=ft.Icons.UPDATE,
                        icon_color=ft.Colors.WHITE,
                        icon_size=30,
                        tooltip="Actualizar Tasa"
                        )