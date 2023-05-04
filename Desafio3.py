# Desafio Interagir com usuário pedidindo dois numeros, somando e exibindo o resultado na tela
primeiro = input("Primeiro Número = ")
segundo = input("Segundo Número = ")
print("A soma é",
      int(primeiro) + int(segundo))  # Neste caso a concatenação de string e numeros (inteiros) é escrita desta forma
# Descobrindo as classes "tipos" das variaveis 
print (type (primeiro)) #Exiba o tipo da classe contida na variavel "primeiro"
print (type(segundo))  #Exiba o tipo da classe contida na variavel "segundo"
#Outra forma de fazer o mesmo exercicio 
n1 = int(input("Informe o primeiro numero: ")) # No "primeiro" caso o tipo da classe da variavel era uma string pois está entre ""
# Já neste exemplo antes da entrada do string eu defino que tudo oque estiver dentro do () será convertido para inteiro
n2 = int(input("Informe o segundo número: "))
print ("A soma é ", n1+n2) # Exibe o resultado da soma de N1 + N2
print (type(n1)) 
print (type(n2))
print ("Fim do exercicio!")




