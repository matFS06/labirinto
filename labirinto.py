import tkinter as tk
from tkinter import messagebox
from collections import deque

def bfs_labirinto(labirinto):
    # Função de busca em largura (BFS) para encontrar o caminho mais curto
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
    # Função para marcar o labirinto com X ao longo do caminho
    marked_labirinto = [list(row) for row in labirinto]
    for x, y in caminho:
        marked_labirinto[x][y] = 'X'
    return marked_labirinto

def imprimir_labirinto(labirinto):
    # Função para imprimir o labirinto no console
    for row in labirinto:
        print("".join(row))

def on_ver_caminho():
    caminho = bfs_labirinto(labirinto)

    if caminho:
        resposta = messagebox.askyesno("Caminho mais curto", "Quer ver as coordenadas do caminho mais curto?")

        if resposta:
            caminho_str = "\nCoordenadas do caminho mais curto:\n"
            for x, y in caminho:
                caminho_str += f"({x}, {y})\n"

            messagebox.showinfo("Caminho mais curto", caminho_str)
        
        # Atualiza o labirinto com as marcações
        labirinto_atualizado = marcar_labirinto(labirinto, caminho)
        labirinto_txt = "\n".join(["".join(row) for row in labirinto_atualizado])
        labirinto_label.config(text=labirinto_txt)
    else:
        messagebox.showinfo("Caminho mais curto", "Nenhum caminho encontrado.")

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

root = tk.Tk()
root.title("Labirinto e Caminho mais Curto")

# Exibindo o título centralizado na cor roxa
title_label = tk.Label(root, text="Caminhando contra o BUG", font=("Arial", 16), fg="purple")
title_label.pack()

# Exibindo o labirinto inicial na tela
labirinto_txt = "\n".join(labirinto)
labirinto_label = tk.Label(root, text=labirinto_txt, font=("Courier", 12))
labirinto_label.pack()

btn_ver_caminho = tk.Button(root, text="Ver Caminho", command=on_ver_caminho)
btn_ver_caminho.pack()

root.mainloop()
