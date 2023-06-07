# Operações numéricas simples com números do tipo inteiro (int)
# Adição (interativo) pedindo para um usuário informar dois números e depois a soma é realizada
nome = input("Por favor informe o seu nome? ")
print ("Obrigado", nome)
primeiro = input ("Vamos somar, por favor insira seu primeiro número: ")
segundo = input("Chegou a hora de informar o segundo número:  ")
print (nome, "a soma do primeiro mais o segundo número é igual", int(primeiro)+int(segundo))
# O mesmo exemplo pode ser usado para subtração, multiplicação e divisão
print ("Agora vamos fazer a subtração de dois números ")
sub1 = input ("Por favor informe o primeiro número: ")
sub2 = input ("Por favor informe o segundo número: ")
print (nome, "a subtração entre os números informados é: ", int(sub1)-int(sub2))
# Multiplicação
print ("Vamos multiplicar! ")
multi1 = input("Por favor informe o primeiro número à ser multiplicado: ")
multi2 = input("Por favor informe o segundo número a ser multiplicado: ")
print (nome, "a multiplicação entre o primeiro e so segundo número é:", int(multi1)*int(multi2))
# Divisão, para divisão inteira, que retorna apenas a parte inteira do resultado, você pode usar o operador de barra dupla (//): Ex 10//3 = 3
# Para divisão de ponto flutuante, você pode usar o operador de barra (/): Ex 10/3 = 3.333333333333333
print ("Agora vamos dividir!")
div1 = input("Por favor informe o dividendo : ")
div2 = input("Por favor informe o divisor: ")
print (nome, "o resultado da sua divisão é: ", int(div1)/int(div2))# Neste exemplo queremos co resultado com o ponto flutuante se for o caso portanto utilizamos o operador (/)
print ("Agora vamos resolver algumas equações simples!") # Nestes exemplos vamos resolver problemas que envolvem duas ou mais operações
print ("Problema: Você foi o supermercado para comprar (x) abacaxi, sabendo que cada abacaxi custa RS 2,00, chegando em casa percebeu (y) abacaxi não estavam em bom estado para utilização. Quantas frutas sobraram? E Qual o valor gasto no suoermercado?")
print (nome, "você foi ao mercado e comprou abacaxi ")
abacaxi = input ("Quantas frutas voce comprou?")
estragaram = input ("Quantas frutas estragaram?")
print (nome, "você comprou ", abacaxi, "abacaxis e gastou R$ ", int(abacaxi)*int(2), "porem ao ver que estragaram ", estragaram, "frutas, ficou claro que restaram apenas", int(abacaxi)-int(estragaram), "frutas" )
# Neste problema utilizamos as operações de multiplicar, para descobrir o valor gasto no supermercado, e a operação de subtração para descobrir quantos abaxis em bom estado de utilização sobraram

