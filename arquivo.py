
def saudacao(nome, idioma='pt'):
    """
    Recebe um nome e retorna uma saudação personalizada no idioma escolhido.
    Idiomas suportados: 'pt' (português), 'en' (inglês)
    """
    if idioma == 'en':
        return f"Hello, {nome}! Welcome to the world of Python."
    else:
        return f"Olá, {nome}! Bem-vindo ao mundo do Python."

# Exemplo de uso:

# Função para saudar múltiplos nomes
def saudar_multiplos(nomes, idioma='pt'):
    """
    Recebe uma lista de nomes e retorna uma lista de mensagens de saudação.
    """
    return [saudacao(nome, idioma) for nome in nomes]

# Função para registrar saudações em um arquivo
def registrar_saudacoes(mensagens, arquivo='saudacoes.txt'):
    """
    Salva as mensagens de saudação em um arquivo texto.
    """
    with open(arquivo, 'a', encoding='utf-8') as f:
        for msg in mensagens:
            f.write(msg + '\n')

# Função para contar saudações feitas
def contar_saudacoes(arquivo='saudacoes.txt'):
    """
    Conta o número de saudações registradas no arquivo.
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

# Exemplos de uso:
mensagem = saudacao("Maria")
print(mensagem)

mensagem_en = saudacao("John", idioma='en')
print(mensagem_en)

nomes = ["Ana", "Carlos", "Beatriz"]
mensagens = saudar_multiplos(nomes)
for m in mensagens:
    print(m)

registrar_saudacoes(mensagens)
print(f"Total de saudações registradas: {contar_saudacoes()}")