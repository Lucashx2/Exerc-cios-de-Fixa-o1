# -*- coding: utf-8 -*-
"""
Soluções em Python para os exercícios propostos.
"""

# ----------------------------------------------------------------------------
# 1. MÉTODOS (FUNÇÕES)
# ----------------------------------------------------------------------------

def secao_1_metodos():
    """Executa todos os exemplos da seção 1."""
    print("\n--- Seção 1: Métodos (Funções) ---")
    
    # 1.1 Calculadora Simples
    print("\n--- 1.1 Calculadora Simples ---")
    class Calculadora:
        def somar(self, a, b):
            return a + b

        def subtrair(self, a, b):
            return a - b

        def multiplicar(self, a, b):
            return a * b

        def dividir(self, a, b):
            if b == 0:
                return "Erro: Divisão por zero não é permitida."
            return a / b

    calc = Calculadora()
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = calc.somar(num1, num2)
    elif operacao == '-':
        resultado = calc.subtrair(num1, num2)
    elif operacao == '*':
        resultado = calc.multiplicar(num1, num2)
    elif operacao == '/':
        resultado = calc.dividir(num1, num2)
    else:
        resultado = "Operação inválida."
        
    print(f"Resultado: {resultado}")

    # 1.2 Verificador de Palíndromos
    print("\n--- 1.2 Verificador de Palíndromos ---")
    def eh_palindromo(texto):
        # Remove espaços e converte para minúsculas
        texto_limpo = texto.replace(" ", "").lower()
        # Compara a string com sua versão invertida
        return texto_limpo == texto_limpo[::-1]

    palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    if eh_palindromo(palavra):
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')

    # 1.3 Fatorial (Recursivo)
    print("\n--- 1.3 Fatorial (Recursivo) ---")
    def fatorial_recursivo(n):
        # Caso base: fatorial de 0 ou 1 é 1
        if n == 0 or n == 1:
            return 1
        # Passo recursivo: n * fatorial(n-1)
        else:
            return n * fatorial_recursivo(n - 1)

    try:
        numero_fat = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
        if numero_fat < 0:
            print("Fatorial não definido para números negativos.")
        else:
            print(f"O fatorial de {numero_fat} é {fatorial_recursivo(numero_fat)}.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

    # 1.4 Conversor de Temperaturas
    print("\n--- 1.4 Conversor de Temperaturas ---")
    class ConversorTemperatura:
        def celsius_para_fahrenheit(self, celsius):
            return (celsius * 9/5) + 32

        def fahrenheit_para_celsius(self, fahrenheit):
            return (fahrenheit - 32) * 5/9

    conversor = ConversorTemperatura()
    escolha = input("Escolha a conversão (1: C->F, 2: F->C): ")
    
    try:
        temp = float(input("Digite a temperatura: "))
        if escolha == '1':
            resultado_temp = conversor.celsius_para_fahrenheit(temp)
            print(f"{temp}°C é igual a {resultado_temp:.2f}°F.")
        elif escolha == '2':
            resultado_temp = conversor.fahrenheit_para_celsius(temp)
            print(f"{temp}°F é igual a {resultado_temp:.2f}°C.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Temperatura inválida. Por favor, digite um número.")


# ----------------------------------------------------------------------------
# 2. ARRAYS MULTIDIMENSIONAIS (MATRIZES)
# ----------------------------------------------------------------------------

def secao_2_matrizes():
    """Executa todos os exemplos da seção 2."""
    print("\n\n--- Seção 2: Arrays Multidimensionais (Matrizes) ---")
    
    # 2.1 Maior e Menor Elemento em uma Matriz
    print("\n--- 2.1 Maior e Menor Elemento em uma Matriz ---")
    try:
        m = int(input("Digite o número de linhas (m): "))
        n = int(input("Digite o número de colunas (n): "))
        
        matriz = []
        for i in range(m):
            linha = []
            for j in range(n):
                elemento = int(input(f"Digite o elemento da posição [{i+1}][{j+1}]: "))
                linha.append(elemento)
            matriz.append(linha)

        maior = matriz[0][0]
        menor = matriz[0][0]

        for linha in matriz:
            for elemento in linha:
                if elemento > maior:
                    maior = elemento
                if elemento < menor:
                    menor = elemento
        
        print("\nMatriz informada:")
        for linha in matriz:
            print(linha)
            
        print(f"Maior elemento: {maior}")
        print(f"Menor elemento: {menor}")

    except ValueError:
        print("Dimensões ou elementos inválidos. Use apenas números inteiros.")

    # 2.2 Soma das Diagonais de uma Matriz Quadrada
    print("\n--- 2.2 Soma das Diagonais de uma Matriz Quadrada ---")
    try:
        ordem = int(input("Digite a ordem da matriz quadrada (n): "))
        
        matriz_quadrada = []
        print("Digite os elementos da matriz:")
        for i in range(ordem):
            linha = []
            for j in range(ordem):
                elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
                linha.append(elemento)
            matriz_quadrada.append(linha)

        soma_diag_principal = 0
        soma_diag_secundaria = 0

        for i in range(ordem):
            soma_diag_principal += matriz_quadrada[i][i]
            soma_diag_secundaria += matriz_quadrada[i][ordem - 1 - i]
            
        print("\nMatriz informada:")
        for linha in matriz_quadrada:
            print(linha)
            
        print(f"Soma da diagonal principal: {soma_diag_principal}")
        print(f"Soma da diagonal secundária: {soma_diag_secundaria}")

    except ValueError:
        print("Ordem ou elementos inválidos. Use apenas números inteiros.")


# ----------------------------------------------------------------------------
# 3. MANIPULAÇÃO DE OBJETOS E REFERÊNCIAS
# ----------------------------------------------------------------------------

def secao_3_referencias():
    """Executa todos os exemplos da seção 3."""
    print("\n\n--- Seção 3: Manipulação de Objetos e Referências ---")
    
    # 3.1 Manipulando Dados de um Objeto
    print("\n--- 3.1 Manipulando Dados de um Objeto ---")
    class Numero:
        def __init__(self, valor_inicial=0):
            self.valor = valor_inicial
        
        def imprimir_valor(self):
            print(f"O valor do atributo é: {self.valor}")

    # Criando a instância
    meu_numero = Numero()
    # Atribuindo um valor
    meu_numero.valor = 100
    # Chamando o método para imprimir
    meu_numero.imprimir_valor()
    # Em Python, id(objeto) retorna a identidade do objeto, que é única
    # e constante durante seu ciclo de vida (similar ao endereço de memória em CPython)
    print(f"A 'identidade' (endereço de memória simulado) do objeto é: {id(meu_numero)}")
    
    # 3.2 Trocando Valores entre Objetos
    print("\n--- 3.2 Trocando Valores entre Objetos ---")
    class ValorContainer:
        def __init__(self, valor):
            self.valor = valor

    def trocar_valores(ref_a, ref_b):
        # Troca os valores *dentro* dos objetos referenciados
        temp = ref_a.valor
        ref_a.valor = ref_b.valor
        ref_b.valor = temp

    try:
        val_a = int(input("Digite o valor para o objeto A: "))
        val_b = int(input("Digite o valor para o objeto B: "))
        
        objA = ValorContainer(val_a)
        objB = ValorContainer(val_b)
        
        print(f"Antes da troca: objA.valor = {objA.valor}, objB.valor = {objB.valor}")
        
        # Chama a função para trocar os valores
        trocar_valores(objA, objB)
        
        print(f"Depois da troca: objA.valor = {objA.valor}, objB.valor = {objB.valor}")
    
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")


# ----------------------------------------------------------------------------
# 4. CLASSES E OBJETOS
# ----------------------------------------------------------------------------

def secao_4_classes_objetos():
    """Executa todos os exemplos da seção 4."""
    print("\n\n--- Seção 4: Classes e Objetos ---")
    
    # 4.1 Sistema de Gerenciamento de Funcionários
    print("\n--- 4.1 Sistema de Gerenciamento de Funcionários ---")
    class Funcionario:
        def __init__(self, nome, id_func, salario, departamento):
            self.nome = nome
            self.id = id_func
            self.salario = salario
            self.departamento = departamento

        def __str__(self):
            return (f"ID: {self.id}, Nome: {self.nome}, "
                    f"Salário: R${self.salario:.2f}, Departamento: {self.departamento}")

    # Em Python, uma lista (list) é o equivalente dinâmico ao ArrayList do Java
    funcionarios = []
    
    while True:
        print("\nMenu de Funcionários:")
        print("1. Cadastrar Funcionário")
        print("2. Calcular total de salários por departamento")
        print("3. Listar todos os funcionários")
        print("4. Sair")
        
        opcao_func = input("Escolha uma opção: ")
        
        if opcao_func == '1':
            try:
                nome = input("Nome: ")
                id_func = int(input("ID: "))
                salario = float(input("Salário: R$"))
                depto = input("Departamento: ")
                funcionarios.append(Funcionario(nome, id_func, salario, depto))
                print("Funcionário cadastrado com sucesso!")
            except ValueError:
                print("ID ou salário inválido. Tente novamente.")
        
        elif opcao_func == '2':
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
                continue
            depto_busca = input("Digite o nome do departamento: ")
            total_salarios = 0
            for func in funcionarios:
                if func.departamento.lower() == depto_busca.lower():
                    total_salarios += func.salario
            print(f"Total de salários para o depto '{depto_busca}': R${total_salarios:.2f}")

        elif opcao_func == '3':
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                print("\n--- Lista de Funcionários ---")
                for func in funcionarios:
                    print(func)
        
        elif opcao_func == '4':
            break
        else:
            print("Opção inválida.")

    # 4.2 Agenda de Contatos
    print("\n--- 4.2 Agenda de Contatos ---")
    class Contato:
        def __init__(self, nome, telefone, email):
            self.nome = nome
            self.telefone = telefone
            self.email = email
            
        def __str__(self):
            return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

    agenda = []
    
    while True:
        print("\nMenu da Agenda:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Procurar Contato")
        print("4. Sair")
        
        opcao_agenda = input("Escolha uma opção: ")

        if opcao_agenda == '1':
            if len(agenda) >= 10:
                print("Agenda cheia (limite de 10 contatos atingido).")
                continue
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.append(Contato(nome, telefone, email))
            print("Contato adicionado!")
            
        elif opcao_agenda == '2':
            if not agenda:
                print("Agenda vazia.")
            else:
                print("\n--- Lista de Contatos ---")
                for contato in agenda:
                    print(contato)
                    
        elif opcao_agenda == '3':
            if not agenda:
                print("Agenda vazia.")
                continue
            nome_busca = input("Digite o nome do contato para procurar: ")
            encontrado = False
            for contato in agenda:
                if contato.nome.lower() == nome_busca.lower():
                    print("Contato encontrado:")
                    print(f"  Telefone: {contato.telefone}")
                    print(f"  Email: {contato.email}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contato não encontrado.")
                
        elif opcao_agenda == '4':
            break
        else:
            print("Opção inválida.")


# --- Função principal para executar as seções ---
def main():
    """Função principal que permite ao usuário escolher qual seção executar."""
    while True:
        print("\n==================== MENU PRINCIPAL ====================")
        print("Escolha a seção de exercícios que deseja executar:")
        print("1. Métodos (Funções)")
        print("2. Matrizes")
        print("3. Manipulação de Objetos e Referências")
        print("4. Classes e Objetos")
        print("5. Sair do programa")
        
        escolha_secao = input("Digite o número da sua escolha: ")
        
        if escolha_secao == '1':
            secao_1_metodos()
        elif escolha_secao == '2':
            secao_2_matrizes()
        elif escolha_secao == '3':
            secao_3_referencias()
        elif escolha_secao == '4':
            secao_4_classes_objetos()
        elif escolha_secao == '5':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Ponto de entrada do script
if __name__ == "__main__":
    main()