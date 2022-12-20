# Pergunta 1: Qual é a sua faixa etária?
idade = input("Qual é a sua faixa etária? ")

# Converta a variável idade para um valor inteiro
idade = int(idade)

# Pergunta 2: Qual é o seu objetivo de investimento a longo prazo?
objetivo = input("Qual é o seu objetivo de investimento a longo prazo? ")

# Pergunta 3: Qual é o seu nível de tolerância ao risco?
tolerancia_risco = input("Qual é o seu nível de tolerância ao risco? ")

# Pergunta 4: Qual é o seu objetivo de retorno a longo prazo?
retorno = input("Qual é o seu objetivo de retorno a longo prazo? ")

# Pergunta 5: Qual é o seu nível de conhecimento sobre investimentos?
conhecimento = input("Qual é o seu nível de conhecimento sobre investimentos? ")

# Determine o perfil de investidor com base nas respostas
if idade <= 30 and objetivo == "crescimento" and tolerancia_risco == "alta" and retorno == "alto" and conhecimento == "alto":
  perfil = "agressivo"
elif idade > 30 and objetivo == "equilíbrio" and tolerancia_risco == "média" and retorno == "médio" and conhecimento == "médio":
  perfil = "moderado"
else:
  perfil = "conservador"

# Exiba o perfil de investidor
print("Seu perfil de investidor é:", perfil)

# Sugira ativos para o perfil de investidor
if perfil == "agressivo":
  print("Para o seu perfil agressivo, você pode considerar investir em ações, fundos imobiliários e criptomoedas.")
elif perfil == "moderado":
  print("Para o seu perfil moderado, você pode considerar investir em títulos de governo, fundos de índice e ações de empresas sólidas.")
else:
  print("Para o seu perfil conservador, você pode considerar investir em títulos de governo, CDBs e fundos de renda")
