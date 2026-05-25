import random

nome = input("Qual é o seu nome, nobre guerreiro? ")
classe = input("Escolha seu destino (Mago, Guerreiro ou Arqueiro): ").strip().lower()

if classe == "mago":
    arma, vida, ataque, mana = "Cajado Mágico", 40, 5, 35
elif classe == "guerreiro":
    arma, vida, ataque, mana = "Espada de Ferro", 85, 15, 0
else:
    classe = "arqueiro"
    arma, vida, ataque, mana = "Arco Curto", 55, 12, 10

v_max = vida
pocoes = 2
x = 0
y = 0
boss = True

while vida > 0 and boss:
    print(f"\nPosição: ({x}, {y})")
    print(f"Sua Vida: {vida}/{v_max} | Poções: {pocoes} | Mana: {mana} | Ataque: {ataque}")
    
    andar = input("Para onde vai agora? [W] Cima, [S] Baixo, [A] Esquerda, [D] Direita: ").strip().lower()
    
    if andar == "w":
        y += 1
    elif andar == "s":
        y -= 1
    elif andar == "d":
        x += 1
    elif andar == "a":
        x -= 1
    else:
        print("Pegou o caminho errado? Essa direção nem existe! Tente W, A, S ou D.")
        continue
        
    print("\nVocê caminha com cautela pelos corredores escuros...")
    
    if y >= 4:
        print("\nO CHÃO TREME! Você invadiu a sala do DRAGÃO DE LAVA!")
        m_nome, m_vida, m_ataque = "Dragão de Lava", 120, 18
        e_boss = True
    else:
        e_boss = False
        sorteio = random.randint(1, 10)
        
        if sorteio <= 3:
            item = random.choice(["pot", "atk", "hp"])
            if item == "pot":
                pocoes += 1
                print("Sorte sua! Achou uma Poção de Cura no chão.")
            elif item == "atk":
                ataque += 3
                print(f"Achou uma pedra mágica! Seu ataque subiu para {ataque}!")
            elif item == "hp":
                v_max += 15
                vida += 15
                print(f"Encontrou um pingente de vitalidade! Sua vida subiu para {vida}!")
            continue
            
        elif sorteio <= 7:
            m_nome, m_vida, m_ataque = random.choice([("Goblin asqueroso", 35, 6), ("Orc furioso", 55, 10)])
            print(f"Um {m_nome} saltou das sombras!")
        else:
            print("O silêncio ecoa pelo corredor... Você está seguro por enquanto.")
            continue

    while vida > 0 and m_vida > 0:
        print(f"\n{nome} (HP: {vida}/{v_max}) VS {m_nome} (HP: {m_vida})")
        # Menu ajustado com números para o jogador saber o que digitar
        opcao = input("Escolha sua ação:\n [1] Atacar\n [2] Usar Magia (10 Mana)\n [3] Beber Poção\n-> ").strip()
        
        if opcao == "67":
            print("\nO CÓDIGO SECRETO FOI ATIVADO! OS CÉUS SE ABREM!")
            dano_secreto = 999
            m_vida -= dano_secreto
            
            if classe == "mago":
                print(f"Do chão da masmorra, os portões do submundo se rasgam! Você invoca o lendário CERBERUS!")
            elif classe == "arqueiro":
                print(f"O tempo desacelera. Você prevê cada milímetro do espaço e dispara uma flecha invisível inevitável! Causou {dano_secreto} de dano!")
            else:
                print(f"Suas mãos queimam e sua espada comum se transforma na lendária EXCALIBUR banhada com sangue de dragon!")
                print(f"Uma onda de energia cortante dourada e vermelha rasga o cenário ao meio, causando {dano_secreto} de dano!")
                
            if m_vida <= 0:
                print(f"Vitória esmagadora! O {m_nome} virou poeira cósmica!")
                if e_boss:
                    boss = False
                break
                
        elif opcao == "1":
            m_vida -= ataque
            print(f"Você brandiu seu {arma} e causou {ataque} de dano!")
            
        elif opcao == "2":
            if mana >= 10:
                mana -= 10
                dano_magico = 25 if classe == "mago" else 12
                m_vida -= dano_magico
                print(f"Feitiço devastador conjurado! Causou {dano_magico} de dano!")
            else:
                print("Sem Mana suficiente para essa magia!")
                continue
                
        elif opcao == "3":
            if pocoes > 0 and vida < v_max:
                pocoes -= 1
                vida = min(vida + 30, v_max)
                print(f"Você engole a poção! Vida atual: {vida}")
            else:
                print("Sem poções ou sua vida já está cheia!")
                continue
        else:
            print("No meio do desespero errou o botão? Digite um comando válido!")
            continue

        # Se o monstro morreu com o ataque normal/magia, sai do loop ANTES de tomar contra-ataque
        if m_vida <= 0:
            print(f"Vitória! Você derrotou o {m_nome}!")
            if e_boss:
                boss = False
            break

        vida -= m_ataque
        print(f"O {m_nome} contra-ataca rápido e te causa {m_ataque} de dano!")

print("\n" + "===============".center(50))
if vida > 0 and boss == False:
    print(f"LENDÁRIO! {nome} derrotou o Dragão de Lava e limpou a masmorra!".center(50))
else:
    print(f"GAME OVER... {nome} virou lenda da pior forma possível nas profundezas.".center(50))
print("===============".center(50))
