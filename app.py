from flask import Flask, request, jsonify #isso importa a bluiblioteca Flask e suas funcionalidades

app = Flask(__name__)# aqui criamos uma instância da aplicação Flask

@app.route('/saudacao', methods=['GET'])# criamos uma rota para a função saudacao com a rota /saudacao em get
def saudacao():#essa primeira função lida com saudações individuais
    nome = request.args.get('nome', 'Visitante')#pega o nome da query string ou usa 'Visitante' como padrão
    idioma = request.args.get('idioma', 'pt')#pega o idioma da query string ou usa 'pt' como padrão
    if idioma == 'en':#se o idioma for inglês
        mensagem = f"Hello, {nome}! Welcome to the world of Python."#saudação em inglês
    else:#se não for inglês
        mensagem = f"Olá, {nome}! Bem-vindo ao mundo do Python."#saudação em português
    return jsonify({'mensagem': mensagem})#retorna a mensagem em formato JSON


# Saudação para múltiplos nomes
@app.route('/saudacoes', methods=['POST'])#essa segunda função lida com saudações múltiplas em post
def saudacoes():#essa segunda função lida com saudações múltiplas
    data = request.get_json()#essa pega o JSON enviado no corpo da requisição
    nomes = data.get('nomes', [])#separa ele em uma lista de nomes
    idioma = data.get('idioma', 'pt')#pega o idioma ou usa 'pt' como padrão
    mensagens = []#cria uma lista vazia para armazenar as mensagens
    for nome in nomes:#para cada nome na lista de nomes
        if idioma == 'en':#se o idioma for inglês
            mensagens.append(f"Hello, {nome}! Welcome to the world of Python.")#adiciona a saudação em inglês
        else:
            mensagens.append(f"Olá, {nome}! Bem-vindo ao mundo do Python.")#adiciona a saudação em português
    return jsonify({'mensagens': mensagens})#retorna as mensagens em formato JSON
# Registrar saudações em arquivo


@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    mensagens = data.get('mensagens', [])
    with open('saudacoes.txt', 'a', encoding='utf-8') as f:
        for msg in mensagens:
            f.write(msg + '\n')
    return jsonify({'status': 'ok', 'quantidade': len(mensagens)})

# Contar saudações
@app.route('/contar', methods=['GET'])
def contar():
    try:
        with open('saudacoes.txt', 'r', encoding='utf-8') as f:
            total = len(f.readlines())
    except FileNotFoundError:
        total = 0
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
