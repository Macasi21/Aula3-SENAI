'''
#1 º Verificando aprovação

nota  = 6
if nota >= 7:
    print ("Aprovado")
else:
    print ("Reprovado")


#if aninhado

nota = 5
if nota >=7:
    print("Aprovado")
else:
    if nota >=5:
        print("Recuperação")
    else:
        print("Recuperação")

#uso do elif

vendas = 30000
meta = 20000

if vendas < meta:
    print("Sem Bonus")
elif vendas >=2 * meta:
    print("Bonus: Alto")
else:
    print("Bonus Medio")


# AND lógico

venda_funcionarios = 25000
meta_funcionarios = 20000
vendas_loja = 15000
meta_loja = 20000

if venda_funcionarios > meta_funcionarios and vendas_loja:
    print("Bonus Liberado")
else:
    print ("Sem Bonus")

# OR logico

idade = 17
autorizacao_pais = True

if idade >= 18 or autorizacao_pais:
    print ("Entrada Permitida")
else:
    print("Entrada Negada")


# comparador "In"

email = "joao@gmail.com"

if "@" in email:
    print("Valido")
else:
    print ("Invalido")


#Comparação Vazia

faturamento = ""
custo = ""

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print("Lucro", lucro)
else:
    print("Dados incompletos")


for i in range (1,11):
    print (i)



#Lista de nomes e imprima por linha

nomes = ['Jose', 'Joao', 'Maria']
for nome in nomes:
    print (nome)


# DEF 

def saudacao():
    print("Ola")



#Retorno ao valor

def soma(a,b):
    return a + b
resultado = soma(2,3)
print(resultado)



#crie uma funcao que receba dois numeros e retorna a media

def media(a, b):
    return (a+b)/2
resultado = media((float(input('Digite seu valor'))), (float(input('Digite seu valor'))))
print (resultado)



#Crie uma tupla com 3 cores RGB

colors = ("Red", "Green", "Blue")
print (colors[2])



#Dicionario em python

aluno = {'Nome':'Carlos', 'idade': 25}
print (aluno['idade'])


#crie um dicionario com nome, sobrenome e idade

user = {'Name': 'Joao','Last_Name': 'Carlos', 'age': 18}
print (user['Last_Name'])
'''