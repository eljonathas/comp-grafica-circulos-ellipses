from methods.circulo import desenhar_circulo
from methods.elipse import desenhar_elipse
from methods.triangulo import desenhar_triangulo

# Exemplo de uso:
print("Círculo com raio 5 em um grid 15x10:")
desenhar_circulo(5, 20, 20)

print()

print("Elipse com raio_x 6 e raio_y 3 em um grid 20x10:")
desenhar_elipse(6, 3, 20, 10)

print()

print("Triângulo com base 9 e altura 5 em um grid 20x10:")
desenhar_triangulo(9, 5, 10, 20)
