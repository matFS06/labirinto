from collections import deque

def bfs_labirinto(labirinto):
    def is_valid(x, y):
        return 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]) and labirinto[x][y] == ' '

    def neighbors(x, y):
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    start = (0, labirinto[0].index(' '))
    end = (len(labirinto) - 1, labirinto[-1].index(' '))

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path

        for neighbor_x, neighbor_y in neighbors(x, y):
            if is_valid(neighbor_x, neighbor_y) and (neighbor_x, neighbor_y) not in visited:
                visited.add((neighbor_x, neighbor_y))
                queue.append(((neighbor_x, neighbor_y), path + [(neighbor_x, neighbor_y)]))

    return None

def marcar_labirinto(labirinto, caminho):
    marked_labirinto = [list(row) for row in labirinto]
    for x, y in caminho:
        marked_labirinto[x][y] = 'X'
    return marked_labirinto

def imprimir_labirinto(labirinto):
    print("\n======== LABIRINTO ========")
    for row in labirinto:
        print("".join(row))

def main():
    labirinto = [
        "#### ######################",
        "#### ######################",
        "##            #       #####",
        "###### #####    ### #######",
        "###### ##### #####     ####",
        "###    ###    ##   ## #####",
        "### ###### ####### ##   ###",
        "###     ##     ###   ##  ##",
        "### ### ######   # #  #  ##",
        "##   ##      ##    #    ###",
        "############### ############"
    ]

    caminho = bfs_labirinto(labirinto)

    if caminho:
        imprimir_labirinto(labirinto)
        resposta = input("Quer ver o caminho mais curto? 1. SIM | 2. NÃO: ")

        if resposta == '1':
            print("\nCoordenadas do caminho mais curto:")
            for x, y in caminho:
                print(f"({x}, {y})")

            print("\nCaminho mais curto:")
            marked_labirinto = marcar_labirinto(labirinto, caminho)
            imprimir_labirinto(marked_labirinto)
        elif resposta == '2':
            print("OK, obrigado!")
        else:
            print("Opção inválida.")
    else:
        print("Nenhum caminho encontrado.")

if __name__ == "__main__":
    main()
1
