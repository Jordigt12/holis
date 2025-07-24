print("hola bienvenido a la calculadora de indice de masa corporal")
print ("primero que nada queremos conocerte.\nAsi que dinos ¿cual es tu nombre?")
nombre  = input("")
print ("perfecto"+" "+nombre) 
print ("Ahora por favor contesta las siguiente preguntas para poder calcular tu IMC")
print ("cual es tu altura en metros")
estatura = float(input  (""))
print("Ok perfecto"+" "+nombre)
print("Y ahora dime ¿cual es tu peso?")
peso=float(input(""))
IMC = peso/(estatura**2)
print("Bien tu IMC es:", IMC)
if IMC < 18.5:
    print ("tienes un porcentaje de grasa bajo")

elif 18.5 <= IMC < 25:
    print("tienes un porcentaje de grasa normal")

elif 25<= IMC < 30:
    print("tienes un porcentaje de grasa alto")

else:
    print("tienes obesidad")


