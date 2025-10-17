import random # Importa o módulo random para gerar números aleatórios

# --- CLASSE POKEMON ---
class Pokemon:# Define a classe Pokemon
    def __init__(self, nome, tipo, hp, ataque): # Inicializa os atributos do Pokémon
        self.nome = nome # Nome do Pokémon
        self.tipo = tipo # Tipo do Pokémon (Fogo, Água, Planta, etc.)
        self.hp = hp # Pontos de vida do Pokémon
        self.ataque = ataque # Valor de ataque do Pokémon

    def atacar(self, outro): # Método para atacar outro Pokémon
        dano = random.randint(self.ataque - 3, self.ataque + 3) # Calcula o dano com uma variação aleatória
        outro.hp -= dano # Reduz o HP do outro Pokémon
        print(f"{self.nome} atacou {outro.nome} e causou {dano} de dano!") # Exibe o resultado do ataque
        if outro.hp <= 0: # Verifica se o outro Pokémon foi derrotado
            print(f"{outro.nome} foi derrotado!") # Exibe a mensagem de derrota

    def curar(self): # Método para curar o Pokémon
        if self.hp <= 15 and random.random() < 0.7:
            vidaextra = random.randint(10, 20) # Gera um valor de cura aleatório maior
            self.hp += vidaextra # Aumenta o HP do Pokémon
            print(f"{self.nome} se curou em {vidaextra} de HP!") # Exibe a quantidade de HP curada
            if self.hp > 35: # Limita o HP máximo
                self.hp = 35
        elif self.hp <= 5:  # Se o HP estiver muito baixo, cura automaticamente
            print(f"{self.nome} está com pouca vida e se curou automaticamente!")
        else:
            cura = random.randint(6, 10) # Gera um valor de cura aleatório
            self.hp += cura # Aumenta o HP do Pokémon 
            print(f"{self.nome} se curou em {cura} de HP!") # Exibe a quantidade de HP curada
# --- FUNÇÃO PARA ESCOLHER UM POKEMON ---
def escolher_pokemon():
    pokemons = [
        Pokemon("Charmander", "Fogo", 28, 15),
        Pokemon("Squirtle", "Água", 36, 12),
        Pokemon("Bulbasaur", "Planta", 35, 13)
    ]
    print("Escolha seu Pokémon:")
    for i, p in enumerate(pokemons, 1):
        print(f"{i}. {p.nome} ({p.tipo})")
    escolha = int(input("Digite o número: ")) - 1
    return pokemons[escolha]

# --- IA ESTRATÉGICA ---
def ia_estrategica(pokemon_inimigo, pokemon_jogador):
    print(f"\n💭 {pokemon_inimigo.nome} está pensando...")

    # Estratégia baseada em HP
    if pokemon_inimigo.hp <= 15 and random.random() < 0.7:
        # 70% de chance de se curar se estiver fraco
        pokemon_inimigo.curar()
    elif pokemon_jogador.hp <= 12 and random.random() < 0.6:
        # 60% de chance de ataque crítico se o jogador estiver fraco
        print(f"{pokemon_inimigo.nome} usou um ataque crítico!")
        dano_extra = random.randint(10, 18)
        pokemon_jogador.hp -= dano_extra
        print(f"{pokemon_jogador.nome} sofreu {dano_extra} de dano crítico!")
    else:
        # Ataque normal
        pokemon_inimigo.atacar(pokemon_jogador)

# --- FUNÇÃO DE BATALHA ---
def batalha(pokemon_jogador, pokemon_inimigo):
    print(f"\n🔥 A batalha começa! {pokemon_jogador.nome} VS {pokemon_inimigo.nome}\n")

    while pokemon_jogador.hp > 0 and pokemon_inimigo.hp > 0:
        # Turno do jogador
        print(f"\nSeu turno! O que deseja fazer?")
        print("1. Atacar")
        print("2. Curar")
        escolha = input("> ")

        if escolha == "1":
            pokemon_jogador.atacar(pokemon_inimigo)
        elif escolha == "2":
            pokemon_jogador.curar()
        else:
            print("Escolha inválida, você perdeu o turno!")

        if pokemon_inimigo.hp <= 0:
            print("🏆 Você venceu a batalha!")
            break

        # Turno da IA
        ia_estrategica(pokemon_inimigo, pokemon_jogador)

        if pokemon_jogador.hp <= 0:
            print("💀 Você foi derrotado!")
            break

        print(f"\n❤️ {pokemon_jogador.nome}: {pokemon_jogador.hp} HP | ⚡ {pokemon_inimigo.nome}: {pokemon_inimigo.hp} HP")

# --- FUNÇÃO PRINCIPAL ---
def main():
    jogador = escolher_pokemon()
    inimigo = random.choice([
        Pokemon("Pikachu", "Elétrico", 67, 14),
        Pokemon("Eevee", "Normal", 67, 13),
        Pokemon("Pidgey", "Voador", 80, 11)
    ])
    batalha(jogador, inimigo)

# --- EXECUTAR ---
if __name__ == "__main__":
    main()
