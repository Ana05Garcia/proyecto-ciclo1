import tkinter as tk
import requests
import datetime
import time

#funcion para hayar temperatura segun la region
def obtener_temperatura():
    ciudad = ubicacion_entry.get()

    API_KEY = "40d14b585fe6f0ba7ca641badf5e773e"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

    respuesta = requests.get(URL)
    datos = respuesta.json()

    if respuesta.status_code == 200:

        tempC = datos["main"]["temp"]
        tempK = tempC + 273.15
        tempF = (tempC * 9/5) + 32

        # cambiar imagen segun temperatura
        if tempC <= 10:
            mi_imagen_label.config(image=imagen_frio)

        elif tempC <= 20:
            mi_imagen_label.config(image=imagen_templado)

        else:
            mi_imagen_label.config(image=imagen_calor)

        
        resultado_label.config(text=f"{tempC} °C | {tempK} K | {tempF} °F")

        #condicionales para que los checkbuttons den la temperatura deseada (tuve que consultarlo)

        texto = ""


        if c.get() == 1:
            texto += f"{tempC} °C | "

        if f.get() == 1:
            texto += f"{tempF} °F | "

        if k.get() == 1:
            texto += f"{tempK} K | "

        resultado.config(text=texto)

    else:
        resultado_label.config(text="Ciudad no encontrada")


root = tk.Tk()

# variables

gen = tk.IntVar()
Miapellido = tk.StringVar()
Micorreo = tk.StringVar()
c = tk.IntVar()
f = tk.IntVar()
k = tk.IntVar()
Mipassword = tk.StringVar()
Minombre = tk.StringVar()
ciudad = tk.StringVar()

def codigo_boton():
    Minombre.set("")
    Miapellido.set("")
    Micorreo.set("")
    Mipassword.set("")
    ciudad.set("")
    gen.set(0)

root.title("ventana")
root.config(bg="#000000", bd=20, relief="solid")

# frame
frame = tk.Frame(root)
frame.pack()

frame.config(width=500, height=400, bg="#003047", bd=11, relief="sunken")

# reloj
reloj = tk.Label(frame, fg="white", bg="#003047", font=("Times New Roman", 20))
reloj.grid(row=0, column=0, columnspan=3, padx=25, pady=15)

dia = tk.Label(frame, fg="#ffffff", bg="#003047", font=("Times New Roman",17))
dia.grid(row=1, column=0, columnspan=3, pady=20,padx=30)

#imagenes
imagen_frio = tk.PhotoImage(file="frio.png")
imagen_templado = tk.PhotoImage(file="templado.png")
imagen_calor = tk.PhotoImage(file="calor.png")

mi_imagen_label = tk.Label(frame, image=imagen_templado, bg="#003047")
mi_imagen_label.grid(row=2, column=0, columnspan=3, pady=10)

# labels
nombre = tk.Label(frame, text="Ingresa tu nombre:", fg="#ffffff", bg="#003047", font=('arial',12))
nombre.grid(row=3, column=0, padx=25, pady=5, sticky="e")

apellido = tk.Label(frame, text="Ingresa tu apellido:", fg="#ffffff", bg="#003047", font=('arial',12))
apellido.grid(row=4, column=0, padx=25, pady=5, sticky="e")

correo = tk.Label(frame, text="Ingresa tu correo:", fg="#ffffff", bg="#003047", font=('arial',12))
correo.grid(row=5, column=0, padx=25, pady=5, sticky="e")

password = tk.Label(frame, text="Ingresa tu contraseña:", fg="white", bg="#003047", font=('arial',12))
password.grid(row=6, column=0, padx=25, pady=5, sticky="e")

ubicacion_label = tk.Label(frame, text="Ingresa la ciudad:", fg="white", bg="#003047", font=('arial',12))
ubicacion_label.grid(row=7, column=0, padx=25, pady=5, sticky="e")

temp=tk.Label(frame,text="temperatura en:", fg="white", bg="#003047", font=('arial',15))
temp.grid(row=1,column=2,rowspan=2)

# entrys
nombre_entry = tk.Entry(frame, width=20, fg="black", bg="#FDFFFE", font=('arial',12), textvariable=Minombre)
nombre_entry.grid(row=3, column=1, padx=5, pady=5)

apellido_entry = tk.Entry(frame, width=20, fg="black", bg="#FDFFFE", font=('arial',12), textvariable=Miapellido)
apellido_entry.grid(row=4, column=1, padx=5, pady=5)

correo_entry = tk.Entry(frame, width=20, fg="black", bg="#FDFFFE", font=('arial',12), textvariable=Micorreo)
correo_entry.grid(row=5, column=1, padx=5, pady=5)

password_entry = tk.Entry(frame, width=20, fg="black", bg="#FFFFFF", font=('arial',12), textvariable=Mipassword, show="*")
password_entry.grid(row=6, column=1, padx=5, pady=5)

ubicacion_entry = tk.Entry(frame, font=("Arial",12), width=20, textvariable=ciudad)
ubicacion_entry.grid(row=7, column=1, pady=5, padx=5)

# genero
genero = tk.Label(frame, text="Seleccione su genero:", bg="#003047", fg="white", font=('arial',14))
genero.grid(row=4, column=2, padx=25, pady=5)

fem = tk.Radiobutton(frame, text="Femenino", variable=gen, value=1)
fem.grid(row=5, column=2, pady=5)

male = tk.Radiobutton(frame, text="Masculino", variable=gen, value=2)
male.grid(row=6, column=2, pady=5)

otro = tk.Radiobutton(frame, text="Otro genero", variable=gen, value=3)
otro.grid(row=7, column=2, pady=5)

# botones
boton = tk.Button(frame, text="enviar", command=codigo_boton, font=("Arial",14), bg="#000000", fg="white", padx=20)
boton.grid(row=8, column=1, columnspan=1, pady=10)

botont = tk.Button(frame, text="encontrar clima", command=obtener_temperatura, font=("Arial",14), bg="#000000", fg="white", padx=20)
botont.grid(row=8, column=0, columnspan=1, pady=10)

# checkbuttons
check1= tk.Checkbutton(frame, text="C", bg="green", font=('arial',15),variable=c)
check1.grid(row=2,column=2)

check2= tk.Checkbutton(frame, text="F", bg="blue", font=('arial',15),variable=f)
check2.grid(row=2,column=2,rowspan=3)

check3= tk.Checkbutton(frame, text="K", bg="red", font=('arial',15),variable=k)
check3.grid(row=2,column=2,rowspan=5)
#resultado checkbuttons
resultado=tk.Label(frame, text="", font=("Arial",10), fg="white", bg="#003047")
resultado.grid(row=3,column=2,rowspan=1)

# resultado
resultado_label = tk.Label(frame, text="", font=("Arial",16), fg="white", bg="#003047")
resultado_label.grid(row=9, column=0, columnspan=3, pady=15)

#hora en tiempo real
def tiempo():
    while True:
        fecha = datetime.datetime.now()
        hora = fecha.strftime("%H:%M:%S")
        date= fecha.strftime("%A,%d-%B-%Y")

        reloj.config(text=f"  (●'◡'●) ◊◈◊Tiempo actual:◊◈◊ (●'◡'●)  \n{hora}")
        dia.config(text=f"◊◈◊Clima hoy: {date}◊◈◊")

        root.update()
        time.sleep(0.5)

tiempo()

root.mainloop()

"""
ANOTACIONES:----------------------------------------------------------------------->
1.los checkbuttons funcionan al presionar el boton de encontrar clima despues de indicar la unidad en el checkbutton
ya que, no sabia si los checkbuttons se tenian que comportar asi o que en el caso contrario era con un command poner el resultado
sin la necesidad de un boton para eso, en tal caso habria que poner las variables tempC,tempF y tempK como globales en vez de funcionar
solo en la funcion de temperatura.

2.Hubieron  algunas cosas que tuve que consultar, estas cosas que tuve que investigar estaran indicadas en un comentario

3 hay dos botones, el boton de encontrar temperatura es la que se usa para obtener la temperatura en el entry y en en los
checkbuttons, el boton de enviar es aquel que 'envia' el formulario y limpia todo lo puesto en los entrys

HAGO ESTAS ANOTACIONES YA QUE AUNQUE MI PROGRAMA CUMPLE LOS OBJETIVOS DICHOS EN EL DOCUMENTO, HAY COSAS QUE NO RECUERDO
SOBRE EL PROGRAMA QUE EL PROFESOR NOS DIO DE EJEMPLO EN LA CLASE Y ESTO PODRIA CAUSAR DIFERENCIAS EN EL FUNCIONAMIENTO DE 
FUNCIONES Y BOTONES EN PARTICULAR :P 
-------------------------------------------------------------------------------------------------------------------------------------"""
