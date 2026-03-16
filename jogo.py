import time
import random

jogar = "S"

while jogar.upper() == "S":

    # Status resetados toda vez que o jogo começa
    vida_maite = 100
    vida_tita = 50
    mamadeiras_agua = 2
    pao_de_queijo = 1  # Novo item!
    dano_extra = 0  # Modificador de dano (começa zerado)

    print("=======================================")
    print(" 🧸 MAITÊ VS PELÚCIAS VIVAS 🧸")
    print(" Missão: Salvar a gatinha Meg!")
    print("=======================================\n")

    time.sleep(1)
    print("A porta do quarto abre rangendo...")
    time.sleep(1)
    print("O Tita ganhou vida e está bloqueando o caminho até a Meg!")
    print(f"Sua Vida (Maitê): {vida_maite} HP")
    print(f"Vida do Tita: {vida_tita} HP\n")

    while vida_maite > 0 and vida_tita > 0:
        print("=======================================")
        print("Escolha a ação da Maitê:")
        print(f"1 - Arranhão (Dano: {15 + dano_extra})")
        print(f"2 - Mordida (Dano: {20 + dano_extra})")
        print("3 - Risada de Naligo (ESPECIAL: Hit Kill)")
        print(f"4 - Mamadeirinha de Água (Cura: 30 HP) [Restam: {mamadeiras_agua}]")
        print(f"5 - Pãozinho de Queijo (Buff: +10 de Dano) [Restam: {pao_de_queijo}]")
        print("=======================================")

        escolha = input("Digite o número da ação e dê Enter: ")

        if escolha == "1":
            dano_final = 15 + dano_extra
            print(f"\n💅 Maitê desfere um arranhão violento na cara do Tita! (-{dano_final} HP)")
            vida_tita = vida_tita - dano_final
        elif escolha == "2":
            dano_final = 20 + dano_extra
            print(f"\n🦷 Maitê crava os dentinhos e dá uma mordida cabulosa! (-{dano_final} HP)")
            vida_tita = vida_tita - dano_final
        elif escolha == "3":
            print("\n✨ Maitê solta a famosa 'Risada de Naligo'!")
            print("O Tita não resiste a tanta fofura, derrete de tanto amor e desiste da luta!")
            vida_tita = 0
        elif escolha == "4":
            if mamadeiras_agua > 0:
                print("\n💧 Maitê toma a mamadeirinha de água, dá uma respirada e recupera energia!")
                vida_maite = min(vida_maite + 30, 100)
                mamadeiras_agua = mamadeiras_agua - 1
            else:
                print("\n❌ Acabou a água! Maitê joga a mamadeira no chão, fica brava e perde o turno!")
        elif escolha == "5":
            if pao_de_queijo > 0:
                print("\n🧀 Maitê come um pãozinho de queijo! Ela fica mais forte e seus ataques ganham +10 de dano!")
                dano_extra = 10
                pao_de_queijo = pao_de_queijo - 1
            else:
                print("\n❌ Já comeu tudo! Maitê procura mais pãozinho, chora um pouco e perde o turno!")
        else:
            print(
                "\n❌ Comando inválido! O papai passou no corredor, Maitê largou a guarda pra gritar 'PAAAAI!' e perdeu o turno!")

        # Só mostra a vida do Tita caindo se a Maitê usou um ataque (opções 1 ou 2)
        if vida_tita > 0 and escolha in ["1", "2"]:
            print(f"-> Vida do Tita agora é: {vida_tita} HP\n")
        elif vida_tita <= 0:
            print(f"-> A vida do Tita chegou a zero!\n")

        time.sleep(2)

        if vida_tita > 0:
            print("\n=======================================")
            print("🐻 Turno do Tita! Ele se prepara para atacar...")
            time.sleep(2)

            ataque_tita = random.choices(["fraco", "forte", "miss"], weights=[40, 20, 40])[0]

            if ataque_tita == "fraco":
                print("💥 Tita dá uma 'Patada de Pelúcia'! Dano leve.")
                vida_maite = vida_maite - 10
            elif ataque_tita == "forte":
                print("☄️ Tita pula da cama e cai com tudo! Dano crítico!")
                vida_maite = vida_maite - 25
            elif ataque_tita == "miss":
                print("💨 Tita tropeça numa peça de Lego e cai de cara. Errou o ataque!")

            if vida_maite > 0:
                print(f"-> Vida da Maitê agora é: {vida_maite} HP")
            else:
                print(f"-> A vida da Maitê chegou a zero!")

            time.sleep(2)

    print("\n=======================================")
    if vida_maite <= 0:
        print("💀 FIM DE JOGO! Tita capturou a Meg e dominou o quarto!")
    elif vida_tita <= 0:
        print("🏆 VITÓRIA! Maitê derrotou a pelúcia e salvou a gatinha Meg!")
    print("=======================================\n")

    jogar = input("Deseja jogar novamente? (S/N): ")
    print("\n")

print("👋 Jogo encerrado. O quarto da Maitê está seguro (por enquanto)!")