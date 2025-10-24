import random
import numpy as np
from sklearn.linear_model import LogisticRegression

# ======================================
# 🎰 Cassino Inteligente com Aprendizado
# ======================================

simbolos = ["🍒", "🍋", "🍀", "💎", "🔔", "⭐"]
saldo = float(input("💰 Digite seu saldo inicial: R$ "))
saldo_inicial = saldo

historico = []
resultados = []

def girar_slot():
    """Gira os 3 rolos da máquina"""
    return [random.choice(simbolos) for _ in range(3)]

def calcular_lucro(rolo, aposta):
    """Define ganhos com base nas combinações"""
    if len(set(rolo)) == 1:
        print("🎉 JACKPOT! 3 iguais!")
        return aposta * 5
    elif len(set(rolo)) == 2:
        print("✨ Duas combinações iguais!")
        return aposta * 2
    else:
        return -aposta

def treinar_modelo():
    """Treina um modelo com base no histórico"""
    if len(historico) < 5:
        return None
    X = np.array(historico)
    y = np.array(resultados)
    modelo = LogisticRegression()
    modelo.fit(X, y)
    return modelo

print("\n🎰 Bem-vindo ao Cassino Inteligente 🎰")
print("Combine símbolos e veja a IA aprender com suas apostas!\n")

while True:
    print(f"💵 Saldo atual: R$ {saldo:.2f}")
    entrada = input("Digite o valor da aposta (ou 'sair'): ")

    if entrada.lower() == "sair":
        break

    try:
        aposta = float(entrada)
        if aposta <= 0 or aposta > saldo:
            print("❌ Valor inválido!\n")
            continue
    except:
        print("❌ Digite um número válido!\n")
        continue

    # IA faz uma previsão sobre a aposta
    modelo = treinar_modelo()
    if modelo:
        prob_ganho = modelo.predict_proba([[aposta]])[0][1]
        if prob_ganho > 0.6:
            print(f"🤖 A IA acha que essa aposta tem {prob_ganho*100:.1f}% de chance de sucesso!")
        else:
            print(f"⚠️ A IA acha que essa aposta é arriscada ({prob_ganho*100:.1f}% chance)")

    input("Pressione ENTER para girar a máquina... 🎲")

    # Gira o slot
    rolos = girar_slot()
    print(f"🎰 | {' | '.join(rolos)} | 🎰")

    lucro = calcular_lucro(rolos, aposta)
    saldo += lucro

    print(f"💰 Resultado: {'+' if lucro > 0 else ''}{lucro:.2f}\n")

    # Salva histórico para IA aprender
    historico.append([aposta])
    resultados.append(1 if lucro > 0 else 0)

    if saldo <= 0:
        print("💀 Você ficou sem saldo! Fim de jogo.")
        break

# Resumo final
print("\n🏁 Fim do jogo!")
print(f"Saldo final: R$ {saldo:.2f}")
lucro_total = saldo - saldo_inicial
print(f"Lucro total: {'+' if lucro_total >= 0 else ''}{lucro_total:.2f}")
print("Obrigado por jogar o 🎰 Cassino Inteligente!")
