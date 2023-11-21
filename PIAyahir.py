import datetime

print("Bienvenido al Instituto de Migración de Australia")

tipo_familia = input("¿La familia es monoparental (S/N)?: ").upper()

puntos_totales = 0
print("\nDatos del progenitor 1:")
sexo = input("Sexo (M/F/N): ")
fecha_nacimiento = input("Fecha de nacimiento (yyyy-mm-dd): ")
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
grado_academico = input("Grado académico (P/U/T/N): ")

oficios_deseados = ["Desarrollador de software", "Ingeniero eléctrico", "Analista de datos", "Técnico de soporte", 
                   "Contador financiero", "Diseñador gráfico", "Ingeniero de sistemas", "Especialista en marketing", 
                   "Técnico de redes", "Asistente administrativo"]  

print (oficios_deseados)

tiene_oficio = input("¿Tiene alguno de los 10 oficios requeridos? (S/N): ").upper() == 'S'

hoy = datetime.date.today()
puntos_edad_fertil = max(15 - (hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)) - 20), 0)

puntos_adicionales = 0
if tiene_oficio in oficios_deseados:
    puntos_adicionales += 8
if grado_academico == 'P':
    puntos_adicionales += 5
elif grado_academico == 'U':
    puntos_adicionales += 3

puntos_totales += 6 + puntos_edad_fertil + puntos_adicionales

if tipo_familia == 'N':
    print("\nDatos del progenitor 2:")
    sexo = input("Sexo (M/F/N): ")
    fecha_nacimiento = input("Fecha de nacimiento (yyyy-mm-dd): ")
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    grado_academico = input("Grado académico (P/U/T/N): ")

    tiene_oficio = input("¿Tiene alguno de los 10 oficios requeridos? (S/N): ").upper() == 'S'

    puntos_edad_fertil = max(15 - (hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)) - 20), 0)

    puntos_adicionales = 0
    if tiene_oficio in oficios_deseados:
        puntos_adicionales += 8
    if grado_academico == 'P':
        puntos_adicionales += 5
    elif grado_academico == 'U':
        puntos_adicionales += 3

    puntos_totales += 6 + puntos_edad_fertil + puntos_adicionales

numero_hijos = int(input("\n¿Cuántos hijos tiene la familia?: "))
puntos_hijos = 0

for i in range(numero_hijos):
    print(f"\nDatos del hijo {i + 1}:")
    sexo = input("Sexo (M/F/N): ")
    fecha_nacimiento = input("Fecha de nacimiento (yyyy-mm-dd): ")
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()

    if sexo == 'F':
        puntos_hijos += max(15 - (hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)) - 20), 0)

puntos_totales += numero_hijos * 8 + puntos_hijos

print(f"\nEl puntaje total de la familia es: {puntos_totales} puntos")

