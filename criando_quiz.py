# QUIZ de Raciocinio Logico criado em Python , utilizando a biblioteca nativa Random
#A biblioteca random em Python é usada para gerar números aleatórios
import random
# Interação com o usuário, recebe o nome de quem vai responder o Quiz e retorna uma saudação
nome = input("Por favor informe seu nome: ")
print (nome, "vamos iniciar nosso Quiz Raciocinio Lógico!")
# Define uma lista de perguntas e respostas, para isto informe a "pergunta":"resposta" e para inserir uma nova pergunta insira , (virgula)
perguntas = {
    "Qual é o próximo número na sequência: 1, 3, 5, 7, ...?": "9",
    "Se você tiver uma régua de 30 cm e quiser cortá-la em 3 partes iguais, quanto medirá cada parte (responda 00 (unidade de medida))?": "10 cm",
    "Se você tem um fósforo e entra em uma sala escura onde há uma lâmpada a óleo, um lampião a gás e uma vela, o que você acende primeiro?": "fósforo",
    "Qual é a próxima letra na sequência A, E, I, M, Q, __?": "U",
    "Qual é o próximo número na sequência 1, 4, 9, 16, 25, __? ": "36",
    "Se há seis pássaros em um galho e você atira em um, quantos pássaros ainda estão no galho?": "5",
    "Se um pacote de balas custa R$ 1,20, quantos reais você precisaria para comprar cinco pacotes (responda com R$ e (virgula))?": "R$6,00",
    "Qual é o resultado da seguinte operação: (4 x 3) + (8 / 4) - 2? ": "12",
    "Se você tem uma pizza com oito fatias e comeu três fatias, quantas fatias sobram?": "5",
    "Se um triângulo tem um ângulo de 90 graus e outro ângulo de 45 graus, qual é o valor do terceiro ângulo (responda 00 graus)?": "45 graus"
}
# Embaralha as perguntas, para que as perguntas não saiam na mesma sequencia (ordem)
lista_perguntas = list(perguntas.items())
random.shuffle(lista_perguntas)
# Faz as perguntas e verifica as respostas, a pontuação inicia no 0 para cada resposta do usuário caso esteja correto o sistema soma + 1 e exibe a menssagem "Correto
# Para cada resposta incorreta, o sistema exibe a mensagem "incorreto" e ignora a pontuação (não soma)
pontuacao = 0
for pergunta, resposta in lista_perguntas:
    resposta_usuario = input(pergunta + " ")
    if resposta_usuario.lower() == resposta.lower():
        print("Correto!")
        pontuacao += 1
    else:
        print("Incorreto.")
# Exibe a pontuação final
print(nome, "você acertou", pontuacao, "de um total de", len(perguntas), "perguntas.")
