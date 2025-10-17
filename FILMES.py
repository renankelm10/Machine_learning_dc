import random

# ------------------------------
# DADOS SIMPLES
# ------------------------------
filmes = {
    "Ação": ["John Wick", "Mad Max", "Missão Impossível", "Gladiador"],
    "Comédia": ["Gente Grande", "As Branquelas", "Deadpool", "Superbad"],
    "Ficção": ["Matrix", "Interestelar", "Avatar", "Duna"],
    "Terror": ["Invocação do Mal", "It: A Coisa", "Corra!", "O Iluminado"]
}

# ------------------------------
# FUNÇÃO DE TREINAMENTO SIMPLES (IA LEVE)
# ------------------------------
def treinar(preferencias):
    """Ajusta o peso de cada gênero com base no gosto do usuário"""
    pesos = {genero: 1 for genero in filmes}  # Começa igual
    for genero, nota in preferencias.items():
        pesos[genero] += nota / 2  # Aumenta peso conforme nota
    return pesos

# ------------------------------
# FUNÇÃO DE RECOMENDAÇÃO
# ------------------------------
def recomendar(pesos):
    """Escolhe um gênero com mais probabilidade se o peso for alto"""
    generos = list(pesos.keys())
    prob = [pesos[g] for g in generos]
    genero_escolhido = random.choices(generos, weights=prob, k=1)[0]
    return random.choice(filmes[genero_escolhido])

# ------------------------------
# EXECUÇÃO PRINCIPAL
# ------------------------------
def main():
    print("🎬 Bem-vindo ao Recomendador de Filmes Inteligente!\n")
    preferencias = {}

    # Pergunta gostos do usuário
    for genero in filmes:
        nota = int(input(f"De 0 a 5, quanto você gosta de filmes de {genero}? "))
        preferencias[genero] = nota

    # IA ajusta os pesos
    pesos = treinar(preferencias)

    print("\n🤖 Recomendando filmes baseados nas suas preferências...\n")
    for _ in range(3):
        sugestao = recomendar(pesos)
        print(f"🎥 Você pode gostar de: {sugestao}")

    print("\n✨ Obrigado por usar o sistema de recomendação!")

if __name__ == "__main__":
    main()
