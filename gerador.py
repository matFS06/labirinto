import random

def generate_maze(width, height):
    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height

    maze = [['#'] * width for _ in range(height)]

    # Defina os pontos de entrada e saída
    start_x, start_y = 1, 0
    end_x, end_y = width - 2, height - 1

    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]
        maze[y][x] = ' '

        neighbors = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(neighbors)

        found = False
        for nx, ny in neighbors:
            if is_valid(nx, ny) and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[(ny + y) // 2][(nx + x) // 2] = ' '
                stack.append((nx, ny))
                found = True
                break

        if not found:
            stack.pop()

    # Adicione paredes nas laterais
    for y in range(height):
        maze[y][0] = '#'
        maze[y][width - 1] = '#'

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

def write_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        for row in maze:
            file.write("".join(row) + '\n')

if __name__ == "__main__":
    width = 21
    height = 11
    maze = generate_maze(width, height)
    
    # Defina os pontos de entrada e saída
    maze[0][1] = ' '  # Entrada
    maze[height - 1][width - 2] = ' '  # Saída
    
    print_maze(maze)

    # Escreva o labirinto em um arquivo de texto chamado "labirinto.txt"
    write_maze_to_file(maze, "labirinto.txt")
