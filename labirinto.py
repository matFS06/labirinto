import tkinter as tk
from tkinter import messagebox
from collections import deque

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)

def bfs_labirinto(grafo, inicio, fim):
    queue = deque([(inicio, [inicio])])
    visitados = set()

    while queue:
        vertice, caminho = queue.popleft()
        if vertice == fim:
            return caminho

        for vizinho in grafo.vertices[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                queue.append((vizinho, caminho + [vizinho]))

def criar_grafo_labirinto(labirinto):
    grafo = Grafo()
    altura = len(labirinto)
    largura = len(labirinto[0])

    for i in range(altura):
        for j in range(largura):
            if labirinto[i][j] == ' ':
                vertice = (i, j)
                grafo.adicionar_vertice(vertice)

    for i in range(altura):
        for j in range(largura):
            if labirinto[i][j] == ' ':
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < altura and 0 <= y < largura and labirinto[x][y] == ' ':
                        grafo.adicionar_aresta((i, j), (x, y))

    return grafo

def marcar_labirinto(labirinto, caminho):
    # Função para marcar o labirinto com X ao longo do caminho
    labirinto_marcado = [list(linha) for linha in labirinto]
    for x, y in caminho:
        labirinto_marcado[x][y] = 'X'
    return labirinto_marcado

def imprimir_labirinto(labirinto):
    # Função para imprimir o labirinto no console
    for linha in labirinto:
        print("".join(linha))

def on_ver_caminho(labirinto, labirinto_label):
    grafo = criar_grafo_labirinto(labirinto)
    inicio = (0, labirinto[0].index(' '))
    fim = (len(labirinto) - 1, labirinto[-1].index(' '))

    caminho = bfs_labirinto(grafo, inicio, fim)

    if caminho:
        resposta = messagebox.askyesno("Caminho mais curto", "Quer ver as coordenadas do caminho mais curto?")

        if resposta:
            caminho_str = "\nCoordenadas do caminho mais curto:\n"
            for x, y in caminho:
                caminho_str += f"({x}, {y})\n"

            messagebox.showinfo("Caminho mais curto", caminho_str)

        # Atualiza o labirinto com as marcações
        labirinto_atualizado = marcar_labirinto(labirinto, caminho)
        labirinto_txt = "\n".join(["".join(linha) for linha in labirinto_atualizado])
        labirinto_label.config(text=labirinto_txt)


def criar_labirinto_frame(root, labirinto, titulo):
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP)

    # Exibindo o título centralizado na cor roxa
    title_label = tk.Label(frame, text=titulo, font=("Arial", 16), fg="purple")
    title_label.pack()

    # Exibindo o labirinto na tela
    labirinto_txt = "\n".join(labirinto)
    labirinto_label = tk.Label(frame, text=labirinto_txt, font=("Courier", 12))
    labirinto_label.pack()

    # Botão para ver o caminho
    btn_ver_caminho = tk.Button(frame, text="Ver Caminho", command=lambda: on_ver_caminho(labirinto, labirinto_label))
    btn_ver_caminho.pack()

def abrir_janela_labirintos():
    labirinto1 = [
        "#### ######################",
        "#### ######################",
        "##                   ######",
        "############    ### #######",
        "###### ##### #####     ####",
        "###    ###    ##   ## #####",
        "### ###### ####### ##   ###",
        "###     ##     ###   ##  ##",
        "### ### ######   # #  #  ##",
        "##   ##      ##    #    ###",
        "############### ###########"
    ]

    labirinto2 = [
        "##### ###############",
        "#                   #",
        "# #   #   #   #   # #",
        "# # # #   # # # # # #",
        "# #   #   #   #   # #",
        "# # # #   #   # #   #",
        "# #   #   #   #   ###",
        "# ####### ###    ## #",
        "#   ####            #",
        "################### #"
    ]

    root = tk.Tk()
    root.title("Labirinto e Caminho mais Curto")

    # Crie frames para cada labirinto
    criar_labirinto_frame(root, labirinto1, "Labirinto 1")
    criar_labirinto_frame(root, labirinto2, "Labirinto 2")

    # Adicione uma saudação com o nome do usuário
    saudacao_label = tk.Label(root, text=f"Bem-vindo", font=("Arial", 16), fg="purple")
    saudacao_label.pack()

    root.mainloop()

def abrir_janela_nickname():
    def on_botao_experimentar():
        nome_usuario = entry_nickname.get()
        if nome_usuario:
            janela_nickname.destroy()
            abrir_janela_labirintos(nome_usuario)

    janela_nickname = tk.Tk()
    janela_nickname.title("Digite seu Nickname")

    # Centralize verticalmente o conteúdo
    janela_nickname.geometry("300x200")
    frame_central = tk.Frame(janela_nickname)
    frame_central.pack(expand=True, fill="both")

    # Label "LABIRINTO" acima do campo de entrada de nickname
    label_labirinto = tk.Label(frame_central, text="LABIRINTO", font=("Arial", 24), fg="purple")
    label_labirinto.pack()

    # Espaço em branco para separação
    espaco_em_branco = tk.Label(frame_central, text="", font=("Arial", 12))
    espaco_em_branco.pack()

    # Label de instrução
    label_instrucao = tk.Label(frame_central, text="Digite seu Nickname:", font=("Arial", 16))
    label_instrucao.pack()

    # Campo de entrada de texto para o nickname
    entry_nickname = tk.Entry(frame_central, font=("Arial", 16))
    entry_nickname.pack()

    # Botão para experimentar
    botao_experimentar = tk.Button(frame_central, text="Experimentar", command=on_botao_experimentar, font=("Arial", 16))
    botao_experimentar.pack()

    janela_nickname.mainloop()

# Inicie abrindo a janela de nickname
abrir_janela_labirintos()
