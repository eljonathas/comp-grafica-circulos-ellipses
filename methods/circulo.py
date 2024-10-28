import math

from colorama import Fore


def desenhar_circulo(raio, largura_grid, altura_grid):
  grid = [['o' for _ in range(largura_grid)] for _ in range(altura_grid)]

  centro_x = largura_grid // 2
  centro_y = altura_grid // 2
  for y in range(altura_grid):
    for x in range(largura_grid):
      distancia = math.sqrt((x - centro_x)**2 + (y - centro_y)**2)
      if distancia <= raio:
        grid[y][x] = 'x'

  # Exibir o grid no terminal com cores
  for linha in grid:
    for elemento in linha:
      if elemento == 'x':
        print(Fore.GREEN + elemento, end=' ')
      else:
        print(Fore.RED + elemento, end=' ')
    print()
