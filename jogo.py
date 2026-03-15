import time
import random

# A variável que controla se o jogo continua rodando
jogar = "S"

# O Loop Gigante que engloba o jogo inteiro
while jogar.upper() == "S":

    # Status resetados toda vez que o jogo começa!
    vida_maite = 100
    vida_tita = 50

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

    # O Loop de Batalha (esteira interna)
    while vida_maite > 0 and vida_tita > 0:
        print("=======================================")
        print("Escolha o ataque da Maitê (1 ano e 5 meses de fúria):")
        print("1 - Arranhão (Dano: 15)")
        print("2 - Mordida (Dano: 20)")
        print("3 - Risada de Naligo (ESPECIAL: Hit Kill)")
        print("=======================================")

        escolha = input("Digite o número do ataque e dê Enter: ")

        if escolha == "1":
            print("\n💅 Maitê desfere um arranhão violento na cara do Tita!")
            vida_tita = vida_tita - 15
        elif escolha == "2":
            print("\n🦷 Maitê crava os dentinhos e dá uma mordida cabulosa!")
            vida_tita = vida_tita - 20
        elif escolha == "3":
            print("\n✨ Maitê solta a famosa 'Risada de Naligo'!")
            print("O Tita não resiste a tanta fofura, derrete de tanto amor e desiste da luta!")
            vida_tita = 0
        else:
            print(
                "\n❌ Comando inválido! O papai passou no corredor, Maitê largou a guarda pra gritar 'PAAAAI!' e perdeu o turno!")

        if vida_tita > 0:
            print(f"-> Vida do Tita agora é: {vida_tita} HP\n")
        else:
            print(f"-> A vida do Tita chegou a zero!\n")

        time.sleep(2)

        # Turno do Tita
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

    # Resultado Final da Partida
    print("\n=======================================")
    if vida_maite <= 0:
        print("💀 FIM DE JOGO! Tita capturou a Meg e dominou o quarto!")
    elif vida_tita <= 0:
        print("🏆 VITÓRIA! Maitê derrotou a pelúcia e salvou a gatinha Meg!")
    print("=======================================\n")

    # A pergunta que define se o loop gigante roda de novo
    jogar = input("Deseja jogar novamente? (S/N): ")
    print("\n")

# Se o cara digitar qualquer coisa que não seja 'S', o código cai aqui fora e encerra.
print("👋 Jogo encerrado. O quarto da Maitê está seguro (por enquanto)!")