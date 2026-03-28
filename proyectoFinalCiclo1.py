import tkinter as tk
import requests

def temperatura():
    ciudad = ubicacion_entry.get()
    codigo_boton()

    API_KEY = "40d14b585fe6f0ba7ca641badf5e773e"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

    respuesta = requests.get(URL)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        tempC = datos["main"]["temp"]
        tempK = tempC + 273.15
        tempF = (tempC * 9/5) + 32

        resultado_label.config(
            text=f"{tempC} °C | {tempK:.2f} K | {tempF:.2f} °F"
        )
    else:
        resultado_label.config(text="Ciudad no encontrada")


root = tk.Tk()

Mipassword = tk.StringVar()
Minombre = tk.StringVar()
ciudad = tk.StringVar()

def codigo_boton():

    Minombre.set("")
    Mipassword.set("")
    ciudad.set("")

root.title("ventana")
root.config(bg="#659c64", bd=20, relief="solid")

# frame
frame = tk.Frame(root)
frame.pack()

frame.config(width=500, height=400, bg="#212222", bd=11, relief="sunken")

# titulo
label = tk.Label(frame, text="clima", fg="#ffffff", bg="#333635", font=('arial',17))
label.grid(row=0, column=1, columnspan=2, pady=15)

# reloj
reloj = tk.Label(frame, font=("Arial", 30), text="")
reloj.grid(row=1, column=1, columnspan=2, padx=25, pady=15)

# labels
nombre = tk.Label(frame, text="Ingresa tu nombre:", fg="#ffffff", bg="#212222", font=('arial',17))
nombre.grid(row=2, column=1, padx=25, pady=15)

password = tk.Label(frame, text="Ingresa tu contraseña:", fg="white", bg="#212222", font=('arial',17))
password.grid(row=3, column=1, padx=25, pady=15)

ubicacion_label = tk.Label(frame, text="Ingresa la ciudad:", fg="white", bg="#212222", font=('arial',17))
ubicacion_label.grid(row=4, column=1, padx=25, pady=15)

# entrys
nombre_entry = tk.Entry(frame, width=20, fg="black", bg="#FDFFFE", font=('arial',17), textvariable=Minombre)
nombre_entry.grid(row=2, column=2, padx=25, pady=15)

password_entry = tk.Entry(frame, width=20, fg="black", bg="#FFFFFF", font=('arial',17), textvariable=Mipassword, show="*")
password_entry.grid(row=3, column=2, padx=25, pady=15)

ubicacion_entry = tk.Entry(frame, font=("Arial",14), width=20, textvariable=ciudad)
ubicacion_entry.grid(row=4, column=2)

# botón
boton = tk.Button(frame, text="enviar",command=temperatura, font=("Arial",14), bg="#4CAF50", fg="white", padx=20,)
boton.grid(row=5, column=2, pady=10)

# resultado
resultado_label = tk.Label(frame, text="", font=("Arial",16), fg="white", bg="#20594e")
resultado_label.grid(row=6, column=1, columnspan=2, pady=15)

root.mainloop()