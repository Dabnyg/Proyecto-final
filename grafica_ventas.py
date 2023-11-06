import tkinter as tk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

mydb = None
ventana_grafica_ventas = None

def cerrar_ventana_grafica_ventas():
    global ventana_grafica_ventas, mydb
    if ventana_grafica_ventas is not None:
        ventana_grafica_ventas.destroy()
    if mydb is not None:
        mydb.close()

def mostrar_ventana_grafica_ventas():
    global ventana_grafica_ventas, mydb
    if ventana_grafica_ventas is None:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",  # Cambia esto a tu contraseña de MySQL
            database="grupal_10"  # Cambia esto a tu base de datos
        )
        
        ventana_grafica_ventas = tk.Tk()
        ventana_grafica_ventas.title("Gráfico de Ventas")
        ventana_grafica_ventas.geometry("800x600")
        ventana_grafica_ventas.configure(bg="#CCB0F4")
        
        cursor = mydb.cursor()
        cursor.execute("SELECT `fecha de venta`, Producto, cantidad FROM ventas")
        result = cursor.fetchall()
        
        fecha_de_venta = []
        productos = {}
        for row in result:
            fecha, producto, cantidad = row
            if fecha not in fecha_de_venta:
                fecha_de_venta.append(fecha)
            if producto not in productos:
                productos[producto] = []
            productos[producto].append(cantidad)
        
        fig, ax = plt.subplots()
        width = 0.2
        x = np.arange(len(fecha_de_venta))
        
        for i, (producto, cantidades) in enumerate(productos.items()):
            ax.bar(x + i * width, cantidades, width, label=producto)
        
        ax.set_xlabel("Fechas de Venta")
        ax.set_ylabel("Cantidad Vendida")
        ax.set_title("Gráfico de Ventas por Producto y Fecha")
        ax.set_xticks(x + width * len(productos) / 2)
        ax.set_xticklabels(fecha_de_venta)
        ax.legend()
        
        container = tk.Frame(ventana_grafica_ventas, bg="#CCB0F4")
        container.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
        boton_volver = tk.Button(ventana_grafica_ventas, text="Volver al menú", command=cerrar_ventana_grafica_ventas,bg="#CCB0F4", fg="#0B0B0B", font=("Helvetica", 12))
        boton_volver.place(relx=0.5, rely=0.02, anchor='n')


def abrir_ventana_grafica_ventas():
    global ventana_grafica_ventas
    if ventana_grafica_ventas is None:
        ventana_grafica_ventas = tk.Tk()
        ventana_grafica_ventas.title("Gráfica de Ventas")
        ventana_grafica_ventas.geometry("800x600")
        ventana_grafica_ventas.configure(bg="#CCB0F4")
    
        opciones_frame = tk.Frame(ventana_grafica_ventas, bg="#CCB0F4")
        opciones_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        productos_button = tk.Button(opciones_frame, text="Grafica de Ventas", command=mostrar_ventana_grafica_ventas, bg="#CCB0F4", fg="white", font=("Helvetica", 12))
        productos_button.pack(side="left", padx=10)