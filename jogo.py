import time
import random

# A Pokédex Base (Os status vão escalar com o level no código)
inimigos_comuns = [
    {
        "nome": "Jacaré", "hp_base": 60, "xp": 30,
        "ataques": [
            {"peso": 50, "texto": "🐊 Jacaré dá uma rabada de pelucia nas pernas da Maitê!", "dano_base": 10},
            {"peso": 35, "texto": "🐊 Jacaré abocanha o braço da Maitê com força!", "dano_base": 25},
            {"peso": 15, "texto": "🐊 Jacaré tenta atacar, mas escorrega no próprio rabo e erra!", "dano_base": 0}
        ]
    },
    {
        "nome": "Onça", "hp_base": 55, "xp": 30,
        "ataques": [
            {"peso": 50, "texto": "🐆 Onça arranha fraquinho com a pata de pelúcia.", "dano_base": 10},
            {"peso": 40, "texto": "🐆 Onça dá um bote selvagem direto no joelho!", "dano_base": 25},
            {"peso": 10, "texto": "🐆 Onça se distrai com um mosquito e erra o bote.", "dano_base": 0}
        ]
    },
    {
        "nome": "Boneca de Pano", "hp_base": 40, "xp": 20,
        "ataques": [
            {"peso": 80, "texto": "🪆 Boneca dá um tapa mole que mal faz cócegas.", "dano_base": 10},
            {"peso": 10, "texto": "🪆 Boneca balança a cabeça de pano com força e acerta a Maitê!", "dano_base": 25},
            {"peso": 10, "texto": "🪆 Boneca cai de cara no chão antes de bater.", "dano_base": 0}
        ]
    },
    {
        "nome": "Leão", "hp_base": 65, "xp": 35,
        "ataques": [
            {"peso": 50, "texto": "🦁 Leão solta um rugido agudo de brinquedo.", "dano_base": 10},
            {"peso": 35, "texto": "🦁 Leão pula e crava os dentes de feltro!", "dano_base": 25},
            {"peso": 15, "texto": "🦁 Leão tropeça na própria juba e erra feio.", "dano_base": 0}
        ]
    },
    {
        "nome": "Tartaruga Colombiana", "hp_base": 80, "xp": 40,
        "ataques": [
            {"peso": 50, "texto": "🐢 Tartaruga joga a mala de viagem e acerta a canela da Maitê.", "dano_base": 10},
            {"peso": 15, "texto": "🐢 Tartaruga dá uma investida pesada com o casco e a mala!", "dano_base": 25},
            {"peso": 35, "texto": "🐢 Tartaruga tenta atacar, mas a mala pesa muito e ela tomba pra trás.",
             "dano_base": 0}
        ]
    },
    {
        "nome": "Tita (Clássico)", "hp_base": 50, "xp": 25,
        "ataques": [
            {"peso": 40, "texto": "🐻 Tita dá uma 'Patada de Pelúcia' leve.", "dano_base": 10},
            {"peso": 20, "texto": "🐻 Tita pula da cama e cai com tudo!", "dano_base": 25},
            {"peso": 40, "texto": "🐻 Tita tropeça numa peça de Lego e cai de cara.", "dano_base": 0}
        ]
    },
    {
        "nome": "Tita Amarelo", "hp_base": 50, "xp": 35,
        "ataques": [
            {"peso": 40, "texto": "🟡 Tita Amarelo solta um soquinho amarelado.", "dano_base": 10},
            {"peso": 20, "texto": "🟡 Tita Amarelo acerta um cruzado pesado!", "dano_base": 25, "chance_stun": 30},
            {"peso": 40, "texto": "🟡 Tita Amarelo erra o soco e bate na parede.", "dano_base": 0}
        ]
    }
]

boss_nega = {
    "nome": "Nega", "hp_base": 800,
    "ataques": [
        {"peso": 45, "texto": "🐈‍⬛ Nega dá uma patada rápida e ardida!", "dano_base": 40},
        {"peso": 45, "texto": "🐈‍⬛ Nega pula com as garras de fora! Dano rasgado!", "dano_base": 70},
        {"peso": 10, "texto": "🐈‍⬛ Nega conjura a magia da Sexta-Feira 13... Maitê fica hipnotizada de medo!",
         "dano_base": 0, "stun_certo": True}
    ]
}

jogar = "S"

while jogar.upper() == "S":

    # Progressão e Status
    level = 1
    xp = 0
    xp_pro_proximo = 100

    vida_maite = 100
    hp_maximo = 100
    escudo_bolacha = 0

    # Inventário e Equipamentos
    mamadeiras_agua = 2
    pao_de_queijo = 1
    risadas_naligo = 1
    slot_risada = 1
    beijos_stun = 0
    limite_beijos = 0

    # Novos Itens
    lutas_cassetete = 0
    tem_pistola_bolhas = False
    cartuchos_bolha = 0
    controles_videogame = 0

    passos_vazios = 0
    explorando = True
    boss_liberado = False

    print("=======================================")
    print(" 🧸 MAITÊ, a guerreira protetora 🧸")
    print(" Missão: Sobreviver à sexta-feira 13 e salvar a Meg!")
    print("=======================================\n")
    time.sleep(1)

    while explorando:
        # Resolve o amarelo do PyCharm inicializando as variáveis base
        iniciar_combate = False
        inimigo_atual = None
        inimigo_buffado_flag = False
        debuff_fralda = False
        matou_com_critico = False

        # CHECAGEM DE LEVEL UP
        if xp >= xp_pro_proximo and level < 5:
            level += 1
            xp = xp - xp_pro_proximo
            xp_pro_proximo = int(xp_pro_proximo * 1.5)

            # Escalonamento de HP da Maitê (+50 por level, até 300)
            hp_maximo = 100 + ((level - 1) * 50)
            vida_maite = hp_maximo

            print(f"\n🌟 LEVEL UP! Maitê alcançou o Level {level}! 🌟")
            print(f"-> HP Máximo aumentou para {hp_maximo}!")
            print("-> Dano base dos ataques aumentou!")

            if level == 3:
                print("🔓 DESBLOQUEADO: Slot extra de Risada, Cura liberada (Mamadeira) e Habilidade 'Beijinho' (Stun)!")
                slot_risada = 2
                limite_beijos = 1
            elif level == 5:
                print("🔓 DESBLOQUEADO: 2 usos do Beijinho por batalha!")
                limite_beijos = 2

            time.sleep(2)

        if level == 5 and not boss_liberado:
            print("\n🔥 A Teté já está com suas garras prontas pra enfrentar a Nega! 🔥")
            escolha_boss = input("Deseja enfrentar a Nega agora? (S/N): ")
            if escolha_boss.upper() == "S":
                inimigo_atual = boss_nega
                boss_liberado = True
                iniciar_combate = True
                escolha_quarto = "boss"
            else:
                print("Maitê decide espancar mais alguns lacaios antes de encarar a chefe...")
                boss_liberado = True
                escolha_quarto = "continua"
        else:
            print(f"\n--- QUARTO DA MAITÊ (Level {level} | XP: {xp}/{xp_pro_proximo}) ---")
            print(
                f"Escudo: {escudo_bolacha} | Cassetete: {'Ativo' if lutas_cassetete > 0 else 'Não'} | Bolhas: {cartuchos_bolha} | Controles: {controles_videogame}")
            print("1 - Andar pelo quarto")
            print(f"2 - Fazer um Mamazinho (Cura HP e restaura {slot_risada} Risada(s))")
            if boss_liberado:
                print("3 - ENFRENTAR A NEGA (BOSS FINAL)")
            escolha_quarto = input("O que a Maitê vai fazer? ")

        if escolha_quarto == "2":
            print(f"\n🍼 Maitê fez um mamazinho e virou outro bebê! Risada de Naligo +{slot_risada}")
            vida_maite = hp_maximo
            risadas_naligo = slot_risada
            print(f"-> HP no máximo ({hp_maximo})! Risadas disponíveis: {risadas_naligo}")
            time.sleep(2)

        elif escolha_quarto == "3" and boss_liberado:
            inimigo_atual = boss_nega
            iniciar_combate = True

        elif escolha_quarto == "1":
            print("\n🐾 Maitê anda pelo tapete...")
            time.sleep(1)

            achou_bicho_sorteio = random.choices([True, False], weights=[45, 55])[0]

            if achou_bicho_sorteio:
                inimigo_atual = random.choice(inimigos_comuns)
                iniciar_combate = True
                passos_vazios = 0
            else:
                passos_vazios += 1

                # O Pity System da Cozinha
                if passos_vazios >= 3:
                    print("\n🏃‍♀️ Maitê andou bastante e foi parar na cozinha!")
                    time.sleep(1)
                    evento_cozinha = random.choice(["papai", "mamae"])

                    if evento_cozinha == "papai":
                        print("👨 O Papai está comendo besteiras! Ele entrega uma Bolacha Salgada pra Maitê.")
                        escudo_bolacha = min(escudo_bolacha + 50, 100)
                        print(f"🛡️ Maitê ganhou 50 de Escudo! (Escudo Atual: {escudo_bolacha}/100)")
                    else:
                        print("👩 A Mamãe está cozinhando! Ela dá um beijo na Maitê (Risada Restaurada!)")
                        risadas_naligo += 1

                        item_mamae = random.choice(["cassetete", "pistola", "controle"])
                        if item_mamae == "cassetete":
                            print(
                                "🎁 A Mamãe também entregou o Cassetete de Brinquedo! (Dano e Crítico aumentados por 3 lutas)")
                            lutas_cassetete = 3
                        elif item_mamae == "pistola":
                            if not tem_pistola_bolhas:
                                print("🎁 A Mamãe entregou a Pistola de Bolhas! (Novo ataque liberado!)")
                                tem_pistola_bolhas = True
                                cartuchos_bolha += 2
                            else:
                                print("🎁 A Mamãe entregou +2 Cartuchos de Bolha!")
                                cartuchos_bolha += 2
                        elif item_mamae == "controle":
                            print(
                                "🎁 A Mamãe achou o Controle de Videogame do Papai perdido e deu pra Maitê! (Item Hit Kill)")
                            controles_videogame += 1

                    passos_vazios = 0
                    time.sleep(3)

                else:
                    evento_quarto = random.randint(1, 5)

                    if evento_quarto == 1:
                        print("Nada por aqui, só uns brinquedos espalhados.")
                    elif evento_quarto == 2:
                        print("Nada por aqui, apenas uma garrafa de água vazia.")
                    elif evento_quarto == 3:
                        print("Você encontrou o crachá do papai, devolva para ele na próxima.")
                    elif evento_quarto == 4:
                        print("🎶 Você encontrou o tecladinho de música e dançou! (+10 HP)")
                        vida_maite = min(vida_maite + 10, hp_maximo)
                    elif evento_quarto == 5:
                        print("👀 Você percebeu que tem algo embaixo do armário...")
                        investigar = input("Deseja investigar? (S/N): ")

                        if investigar.upper() == "S":
                            achado = random.choice(
                                ["cartucho", "cura", "risada", "cassetete", "fralda", "inimigo_buffado"])
                            if achado == "cartucho":
                                print("🫧 Você achou 1 Cartucho de Bolha escondido!")
                                cartuchos_bolha += 1
                            elif achado == "cura":
                                print("💧 Achou uma mamadeira perdida! (+30 HP)")
                                vida_maite = min(vida_maite + 30, hp_maximo)
                            elif achado == "risada":
                                print("🧸 Achou um ursinho fofo que fez cosquinha! (+1 Risada)")
                                risadas_naligo += 1
                            elif achado == "cassetete":
                                print("🏏 Encontrou um Cassetete de Brinquedo perdido! (Buff para 3 lutas)")
                                lutas_cassetete = 3
                            elif achado == "fralda":
                                print("💩 Eca! Uma fralda suja de cocô! O fedor deixa a Maitê fraca na próxima luta.")
                                debuff_fralda = True
                            elif achado == "inimigo_buffado":
                                print("⚠️ CUIDADO! Um inimigo estava escondido e furioso!")
                                inimigo_atual = random.choice(inimigos_comuns)
                                inimigo_buffado_flag = True
                                iniciar_combate = True
                        else:
                            print("Maitê ignorou o armário e continuou andando.")
                    time.sleep(2)

        elif escolha_quarto not in ["1", "2", "3"]:
            print("\n❌ Maitê ficou brincando com o próprio pé e não fez nada.")

        # ==========================================
        # LOOP DE BATALHA
        # ==========================================
        if iniciar_combate and inimigo_atual:
            nome_inimigo = inimigo_atual["nome"]

            escala_inimigo = 1.0 + ((level - 1) * 0.2)
            vida_inimigo = int(inimigo_atual["hp_base"] * escala_inimigo)

            if inimigo_buffado_flag:
                vida_inimigo = int(vida_inimigo * 1.5)
                nome_inimigo = "Super " + nome_inimigo

            xp_inimigo = inimigo_atual.get("xp", 1000)

            maite_stunada = False
            turnos_stun_inimigo = 0
            beijos_disponiveis = limite_beijos
            usos_bolha_batalha = 2

            escala_dano_maite = 1.0 + ((level - 1) * 0.125)

            if debuff_fralda:
                print("\n🤢 O fedor da fralda suja deixou a Maitê enjoada! (-50% de Dano nesta luta)")
                escala_dano_maite *= 0.5
                debuff_fralda = False

            if nome_inimigo == "Nega":
                print(f"\n🔥 MÚSICA DE CHEFE COMEÇA! A {nome_inimigo} desce do armário com os olhos brilhando!")
            else:
                print(f"\n⚠️ Um(a) {nome_inimigo} selvagem bloqueia o caminho!")

            time.sleep(2)

            while vida_maite > 0 and vida_inimigo > 0:

                if maite_stunada:
                    print("\n💫 Maitê está tonta e não consegue se mexer! Perdeu a vez!")
                    maite_stunada = False
                    time.sleep(2)
                else:
                    print("=======================================")
                    print(
                        f"Batalha: Maitê ({vida_maite} HP | 🛡️ {escudo_bolacha}) VS {nome_inimigo} ({vida_inimigo} HP)")

                    dano_arranhao = int(15 * escala_dano_maite)
                    dano_mordida = int(20 * escala_dano_maite)

                    if lutas_cassetete > 0:
                        dano_arranhao = int(dano_arranhao * 1.3)
                        dano_mordida = int(dano_mordida * 1.3)
                        print("(Buff do Cassetete Ativo!)")

                    print(f"1 - Arranhão (Dano: {dano_arranhao})")
                    print(f"2 - Mordida (Dano: {dano_mordida})")
                    print(f"3 - Risada de Naligo (ESPECIAL) [Restam: {risadas_naligo}]")
                    if level >= 3:
                        print(f"4 - Mamadeirinha de Água (Cura: 30 HP) [Restam: {mamadeiras_agua}]")
                        print(f"5 - Mandar Beijinho (STUN 1 Turno) [Restam: {beijos_disponiveis}]")
                    if tem_pistola_bolhas:
                        print(f"6 - Pistola de Bolhas (STUN 2 Turnos) [Cartuchos: {cartuchos_bolha}]")
                    if controles_videogame > 0:
                        print(f"7 - Jogar Controle do Papai (DANO MASSIVO) [Restam: {controles_videogame}]")

                    print("=======================================")
                    escolha = input("Digite o número da ação e dê Enter: ")

                    chance_base_crit = 35 if lutas_cassetete > 0 else 20
                    rolagem_crit = random.randint(1, 100)
                    multiplicador_crit = 2 if rolagem_crit <= chance_base_crit else 1
                    texto_crit = " CRÍTICO!!" if multiplicador_crit == 2 else ""

                    if escolha == "1":
                        dano_final = dano_arranhao * multiplicador_crit
                        print(f"\n💅 Maitê desfere um arranhão!{texto_crit} (-{dano_final} HP)")
                        if vida_inimigo - dano_final <= 0 and multiplicador_crit == 2: matou_com_critico = True
                        vida_inimigo -= dano_final

                    elif escolha == "2":
                        dano_final = dano_mordida * multiplicador_crit
                        print(f"\n🦷 Maitê crava os dentinhos!{texto_crit} (-{dano_final} HP)")
                        if vida_inimigo - dano_final <= 0 and multiplicador_crit == 2: matou_com_critico = True
                        vida_inimigo -= dano_final

                    elif escolha == "3":
                        if risadas_naligo > 0:
                            if nome_inimigo == "Nega":
                                print("\n❌ A Nega é imune à Risada! Ela é pura frieza felina!")
                                risadas_naligo -= 1
                            else:
                                print("\n✨ Maitê solta a famosa 'Risada de Naligo'!")
                                print(f"O(a) {nome_inimigo} derrete de amor!")
                                vida_inimigo = 0
                                risadas_naligo -= 1
                        else:
                            print("\n❌ Sem energia para rir! Perdeu o turno!")

                    elif escolha == "4" and level >= 3:
                        if mamadeiras_agua > 0:
                            print("\n💧 Maitê toma a mamadeirinha de água!")
                            vida_maite = min(vida_maite + 30, hp_maximo)
                            mamadeiras_agua -= 1
                        else:
                            print("\n❌ Acabou a água! Perdeu o turno!")

                    elif escolha == "5" and level >= 3:
                        if beijos_disponiveis > 0:
                            print("\n💋 Maitê manda um beijo com as mãozinhas!")
                            print(f"O(a) {nome_inimigo} fica molenga de amor! (Stun de 1 Turno)")
                            turnos_stun_inimigo = 1
                            beijos_disponiveis -= 1
                        else:
                            print("\n❌ Já mandou beijo demais. Perdeu o turno!")

                    elif escolha == "6" and tem_pistola_bolhas:
                        if cartuchos_bolha > 0 and usos_bolha_batalha > 0:
                            print("\n🫧 Maitê atira sabão direto nos olhos do inimigo!")
                            print(f"O(a) {nome_inimigo} está cego de sabão! (Stun de 2 Turnos)")
                            turnos_stun_inimigo = 2
                            cartuchos_bolha -= 1
                            usos_bolha_batalha -= 1
                        elif usos_bolha_batalha <= 0:
                            print("\n❌ Arma superaquecida! Só 2 usos por luta. Perdeu o turno!")
                        else:
                            print("\n❌ Sem cartuchos de bolha! Perdeu o turno!")

                    elif escolha == "7" and controles_videogame > 0:
                        print("\n🎮 Maitê arremessa o Controle do Papai direto na testa do alvo!")
                        if "Nega" in nome_inimigo:
                            print("A Nega toma uma pancada seca! (-100 HP)")
                            vida_inimigo -= 100
                        else:
                            print("HIT KILL! O inimigo foi esmagado pela tecnologia!")
                            vida_inimigo = 0
                        controles_videogame -= 1

                    else:
                        print("\n❌ Comando inválido ou item indisponível! Perdeu o turno!")

                    time.sleep(2)

                # Turno do Inimigo
                if vida_inimigo > 0:
                    if turnos_stun_inimigo > 0:
                        print(f"\n😵 O(a) {nome_inimigo} está atordoado e não consegue agir!")
                        turnos_stun_inimigo -= 1
                        time.sleep(2)
                    else:
                        print(f"\n🐻 Turno do(a) {nome_inimigo}...")
                        time.sleep(1)

                        lista_ataques = inimigo_atual["ataques"]
                        pesos = [atk["peso"] for atk in lista_ataques]
                        golpe_escolhido = random.choices(lista_ataques, weights=pesos)[0]

                        print(f"-> {golpe_escolhido['texto']}")

                        dano_inimigo_final = int(golpe_escolhido["dano_base"] * escala_inimigo)

                        if dano_inimigo_final > 0:
                            if escudo_bolacha > 0:
                                dano_no_escudo = min(escudo_bolacha, dano_inimigo_final)
                                escudo_bolacha -= dano_no_escudo
                                dano_inimigo_final -= dano_no_escudo
                                print(
                                    f"🛡️ O Escudo de Bolacha absorveu {dano_no_escudo} de dano! (Restam {escudo_bolacha} no escudo)")

                            if dano_inimigo_final > 0:
                                vida_maite -= dano_inimigo_final

                        if golpe_escolhido.get("stun_certo"):
                            maite_stunada = True
                        elif "chance_stun" in golpe_escolhido:
                            if random.randint(1, 100) <= golpe_escolhido["chance_stun"]:
                                print("💫 O golpe foi tão forte que Maitê ficou tonta! (STUN)")
                                maite_stunada = True

                        if vida_maite > 0:
                            print(f"-> Vida da Maitê agora é: {vida_maite} HP")
                        else:
                            print(f"-> A vida da Maitê chegou a zero!")
                            explorando = False

                        time.sleep(2)

            # Fim da Luta
            if vida_inimigo <= 0:
                if nome_inimigo == "Nega" or nome_inimigo == "Super Nega":
                    print("\n🏆 VITÓRIA ÉPICA! O feitiço da sexta-feira 13 se quebra!")
                    print("A mamãe Carol entra no quarto, guarda as pelúcias no armário e pega a Meg no colo.")
                    print("MAITÊ SALVOU O DIA!")
                    explorando = False
                else:
                    print(f"\n🏆 VITÓRIA! Maitê derrotou o(a) {nome_inimigo}!")

                    if lutas_cassetete > 0:
                        lutas_cassetete -= 1
                        if lutas_cassetete == 0:
                            print("🪵 O Cassetete de brinquedo quebrou após o uso!")

                    xp_ganho = xp_inimigo
                    if matou_com_critico:
                        print("🔥 BÔNUS DE CRÍTICO! (+20 XP)")
                        xp_ganho += 20

                    xp += xp_ganho
                    print(f"Ganhou {xp_ganho} XP! (Total: {xp}/{xp_pro_proximo})")
                    time.sleep(2)

    if vida_maite <= 0:
        print("\n=======================================")
        print("💀 FIM DE JOGO! A Nega afugentou a Maitê e sequestrou a Meg!")
        print("=======================================\n")

    jogar = input("\nDeseja jogar novamente do zero? (S/N): ")
    print("\n")

print("👋 Jogo encerrado.")