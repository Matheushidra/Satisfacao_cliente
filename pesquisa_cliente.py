# Define uma constante que determina quantas vezes a pesquisa será repetida.
# O enunciado pede 50, mas para testar, estamos usando 10. 
TOTAL_ENTREVISTADOS = 10 

# Cria uma variável para guardar o número de pessoas que votaram "EXCELENTE". Começa em zero.
qtd_excelente = 0

# Cria uma variável para guardar o número de pessoas que votaram "RUIM". Começa em zero.
qtd_ruim = 0

# Exibe uma linha tracejada para enfeitar o cabeçalho do programa (multiplica o traço por 40)
print("-" * 40)
# Exibe o título do programa na tela
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB   ")
# Exibe outra linha tracejada fechando o cabeçalho
print("-" * 40)

# Inicia a estrutura de repetição (loop) que vai de 0 até o TOTAL_ENTREVISTADOS - 1
for i in range(TOTAL_ENTREVISTADOS):
    
    # Exibe em qual número de entrevistado estamos. O 'i + 1' é usado porque o contador 'i' começa no zero.
    print(f"\n--- Entrevistado {i + 1} de {TOTAL_ENTREVISTADOS} ---")
    
    # Pede para o usuário digitar o nome e guarda o texto digitado na variável 'nome'
    nome = input("Digite o nome: ")
    
    # Pede para o usuário digitar a idade, converte o texto para número inteiro (int) e guarda na variável 'idade'
    idade = int(input("Digite a idade: "))
    
    # Exibe as instruções de votação na tela para o usuário
    print("Avalie nosso atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    # Pede para o usuário digitar a opinião (1, 2 ou 3), converte para inteiro e guarda na variável 'opiniao'
    opiniao = int(input("Digite a sua opinião (1, 2 ou 3): "))
    
    # Inicia a estrutura de decisão para verificar o que o usuário digitou
    if opiniao == 1:
        # Se a opinião for igual a 1 (EXCELENTE), adiciona +1 à variável qtd_excelente
        qtd_excelente += 1
        
    elif opiniao == 3:
        # Se a opinião for igual a 3 (RUIM), adiciona +1 à variável qtd_ruim
        qtd_ruim += 1
        
    elif opiniao == 2:
        # Se a opinião for igual a 2 (BOM), o comando 'pass' diz ao programa para não fazer nada, 
        # já que o enunciado não pede para contar as respostas "BOM"
        pass
        
    else:
        # Se o usuário digitar qualquer número diferente de 1, 2 ou 3, exibe uma mensagem de erro
        print("Opção inválida! Este voto não será contabilizado.")

# Quando a repetição (for) termina, exibe uma quebra de linha (\n) seguida de uma linha de símbolos de igual
print("\n" + "=" * 40)
# Exibe o título da área de resultados
print("       RESULTADO FINAL DA PESQUISA      ")
# Exibe outra linha de símbolos de igual
print("=" * 40)

# Exibe na tela o texto com a quantidade final de votos acumulados na variável 'qtd_excelente'
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")

# Exibe na tela o texto com a quantidade final de votos acumulados na variável 'qtd_ruim'
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")

# Exibe uma última linha de símbolos de igual para fechar o programa visualmente
print("=" * 40)
