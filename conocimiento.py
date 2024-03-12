# Taller de conocimientos
  # Ejercicio 01

def calcular_imc(peso, altura):
    # Fórmula del IMC: peso / (altura^2)
    imc = peso / (altura ** 2)
    return imc

# Ejemplo de uso
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"El Índice de Masa Corporal (IMC) es: {imc:.2f}")

# f-string
mensaje = (f"Tabla de clasificaciones: \n Desnutricion moderada: 16,01-16,99 .\n Bajo peso: 18,5-22 ."
           f"\n Peso normal: 22,1-24,9 .\n Sobrepeso: 25-29,9")
print(mensaje)

# Ejercicio 02 y 03

destino = input("ingrese el destino donde desea comunicarse:")
duracion = int(input("ingrese la duracion de la llamada:"))

if destino == "estados unidos":
     costo = duracion * 900

if destino == "canada":
     costo = duracion * 800

if destino == " europa":
     costo = duracion * 950

if destino == "resto del mundo":
     costo = duracion * 1250

if duracion >15:
     descuento = costo * 0.20
     costo = costo - descuento


     print(f"el costo de su llamada e:, {costo}")


