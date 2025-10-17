import matplotlib.pyplot as plt
import math
import random

# --- Função fractal controlada por IA ---
def arvore_ia(x, y, comprimento, angulo, nivel):
    if nivel == 0:
        return
    # IA decide aleatoriamente o ângulo e a redução do ramo
    angulo_ramo = random.choice([15, 20, 25, 30])
    reducao = random.choice([0.65, 0.7, 0.75])

    # Calcula a posição do próximo ponto
    x2 = x + comprimento * math.cos(math.radians(angulo))
    y2 = y + comprimento * math.sin(math.radians(angulo))

    # Desenha linha do ramo
    plt.plot([x, x2], [y, y2], color='green', linewidth=nivel)  # linha mais grossa nos ramos principais

    # Chama recursivamente para os dois ramos
    arvore_ia(x2, y2, comprimento * reducao, angulo - angulo_ramo, nivel - 1)
    arvore_ia(x2, y2, comprimento * reducao, angulo + angulo_ramo, nivel - 1)

# --- Loop de múltiplas gerações (IA experimentando combinações) ---
for geracao in range(5):  # 5 árvores diferentes
    plt.figure(figsize=(8, 10))
    arvore_ia(0, 0, 100, 90, 7)
    plt.axis('off')
    plt.title(f"Árvore IA - Geração {geracao+1}")
    plt.show()
