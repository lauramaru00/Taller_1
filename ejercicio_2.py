# Programa para gestionar calificaciones de estudiantes

# 1. Lista que almacena las calificaciones de los estudiantes.

calificaciones = []

cantidad = int(input("¿Cuantas calificaciones desea ingresar?: "))

for i in range(cantidad):
    calificacion = float(input(f"Ingrese una calificacion {i + 1}: "))
    calificaciones.append(calificacion)


# 2. Aplicar modificaciones a determinados elementos bajo un criterio
# Criterio: Si la calificacion es menor a 3.0, se le otorga una nivelación de 0.3

for i in range(len(calificaciones)):
    if calificaciones[i] < 3.0:
        calificaciones[i] = round(calificaciones[i] + 0.3, 2)


# 3. Realizar cálculos básicos sobre los valores que se obtienen de las calificaciones (Suma y Promedio)
suma = 0
for calificacion in calificaciones:
    suma += calificacion

promedio = suma / len(calificaciones)


# 4. Contador para verificar cuantos estudiantes reprobaron o aprobaron.

aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1


# 5. Imprimir los resultados finales.
print("Total de calificaciones:", calificaciones)
print(f"Promedio general del grupo: {promedio:.2f}")
print("Calificacion más alta:", max(calificaciones))
print("Calificacion más baja:", min(calificaciones))
print("Cantidad de estudiantes aprobados:", aprobados)
print("Cantidad de estudiantes reprobados:", reprobados)