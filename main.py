# este es un comentario
"""dsosdosdosdosdo"""

# linter (revisa el codigo)
# type-hinting
# variables

variable = 20  # entero (int)
variable2 = 20.4  # flotante (float).
variabletexto = "hola"  # string (str) "h","o","l","a"
variablef = True  # booleano (bool)

# control+q
ingreso=input("Ingrese un precio:")

# conversion de datos
# int(valor) en entero
# float(valor) en flotante
# str(valor) en un string

ingreso_numerico=float(ingreso)

precio_con_iva=ingreso_numerico*1.19

print("el valor es ",precio_con_iva)

# tuplas

tupla= (20,30,40)  # con un parentesis. (es que no es mutable)

# set
set={20,30,40}  # con { } 1) no es ordenado
set={20,30,40,20}   # velocidad.

# lista
lista=[20,30,40]  # [ ]  1) es mutable, 2) es mas lento.

# diccionario
dic=dict(campo1="hola",campo2="mundo")   # key=value
dic={"campo1":"hola","campo2":"mundo"}


print(dic)










