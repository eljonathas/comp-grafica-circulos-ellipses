from colorama import Fore


def desenhar_triangulo(base, altura, largura_grid, altura_grid):
    grid = [['O' for _ in range(largura_grid)] for _ in range(altura_grid)]

    # ficar no centro
    centro_x = largura_grid // 2
    centro_y = altura_grid // 2
    start_y = centro_y - altura // 2

    for y in range(altura):
        altura_proporcional = y / altura
        largura_atual = int(
            base *
            (1 -
             altura_proporcional))  # A base vai diminuindo conforme subimos
        start_x = centro_x - largura_atual // 2  # Centralizando a base do triângulo
        for x in range(largura_atual):
            grid[start_y + y][start_x + x] = 'X'

    # Exibir o grid no terminal com cores
    for linha in grid:
        for elemento in linha:
            if elemento == 'X':
                print(Fore.GREEN + elemento, end=' ')
            else:
                print(Fore.RED + elemento, end=' ')
        print()
