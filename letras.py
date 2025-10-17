import random
import os
import time

# --- Configurações ---
largura = 50   # largura do terminal
altura = 20    # altura da "tela"
velocidade = 0.1  # tempo entre frames (em segundos)

# --- Criando colunas da chuva ---
colunas = [0] * largura  # cada posição indica a altura da letra na coluna

# --- Letras que vão cair ---
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

# --- Função para limpar a tela ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Loop principal da animação ---
try:
    while True:
        limpar_tela()
        tela = []

        for y in range(altura):
            linha = ""
            for x in range(largura):
                if colunas[x] == y:
                    linha += random.choice(letras)
                else:
                    linha += " "
            tela.append(linha)

        print("\n".join(tela))

        # Atualiza posições das letras
        for i in range(largura):
            if random.random() > 0.9:
                colunas[i] = 0
            else:
                colunas[i] = (colunas[i] + 1) % altura

        time.sleep(velocidade)

except KeyboardInterrupt:
    print("\nSaindo da Matrix... Até a próxima!")
