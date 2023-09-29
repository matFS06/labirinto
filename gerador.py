import random

def generate_maze(width, height):
    # Inicialize uma matriz para representar o labirinto
    maze = [['#'] * (2 * width + 1) for _ in range(2 * height + 1)]

    # Função para cavar caminhos no labirinto
    def dig(x, y):
        maze[y][x] = ' '  # Marcar a célula como vazia

        # Direções possíveis (cima, baixo, esquerda, direita)
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Verificar se a próxima célula é válida
            if 0 < nx < 2 * width and 0 < ny < 2 * height and maze[ny][nx] == '#':
                mx, my = x + dx // 2, y + dy // 2
                maze[my][mx] = ' '  # Remover a parede entre as células
                dig(nx, ny)  # Recursivamente cavar a próxima célula

    # Comece a cavar a partir do ponto inicial (1, 1)
    dig(1, 1)

    # Defina os pontos de entrada e saída
    maze[0][1] = ' '
    maze[2 * height][2 * width - 1] = ' '

    # Converter a matriz do labirinto em uma única string
    maze_str = '\n'.join([''.join(row) for row in maze])

    return maze_str

if __name__ == "__main__":
    width = 10
    height = 5
    maze = generate_maze(width, height)
    print(maze)
