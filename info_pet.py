# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    while True:
        print("Por favor, insira as informações sobre seu pet.")

        # Coleta do tipo de animal
        while True:
            tipo = input("Tipo de animal (ex: cachorro, gato, pássaro): ").strip().lower()
            if tipo:
                break
            else:
                print("O tipo de animal não pode estar vazio. Tente novamente.")

        # Coleta do nome do pet
        while True:
            nome = input("Nome do pet: ").strip()
            if nome:
                break
            else:
                print("O nome do pet não pode estar vazio. Tente novamente.")

        # Coleta da idade do pet, garantindo que seja um número inteiro
        while True:
            try:
                idade = int(input("Idade do pet (em anos): "))
                if idade < 0:
                    print("A idade não pode ser negativa. Tente novamente.")
                elif idade > 50:
                    print("A idade parece muito alta. Por favor, insira um valor realista.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para a idade.")

        # Coleta do peso do pet, garantindo que seja um número flutuante
        while True:
            try:
                peso = float(input("Peso do pet (em kg): "))
                if peso < 0:
                    print("O peso não pode ser negativo. Tente novamente.")
                elif peso > 200:
                    print("O peso parece muito alto. Por favor, insira um valor realista.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para o peso.")

        # Exibindo as informações coletadas
        print("\nInformações do pet:")
        print(f"Tipo: {tipo.capitalize()}")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Peso: {peso} kg")
        
        # Confirmação dos dados
        confirmacao = input("\nAs informações estão corretas? (s/n): ").lower()

        # Encerra se as informações estiverem corretas
        if confirmacao == 's':
            print("\nInformações confirmadas.")
            break
        else:
            print("\nVamos corrigir as informações.\n")

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
