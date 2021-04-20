Obra=[]
avaliacao = "SIM"
while avaliacao == "SIM":
  imovel=[input("Imóvel: "),
            float(input("Valor: ")),
            int(input("Código: ")),
            input("Cidade: ")]
  obra.append(imovel)
  avaliacao = input("Digite "SIM" para continuar: ").upper()

for imovel in obra:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Código.......: ", elemento[2])
  print("Cidade.......: ", elemento[3])

busca=input("
Digite o nome do proprietário do imóvel que deseja buscar: ")
for imovel in obra:
  if busca==imovel[0]:
    print("Valor..: ", elemento[1])
    print("Código.:", elemento[2])

depreciacao=input("
Digite o nome do proprietário da obra: ")
for imovel in obre:
  if depreciacao==imovel[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.4
    print("Novo valor: ", elemento[1])

codigo=int(input("
Digite o código do imovel que será excluído da base de dados: "))
for imovel in obra:
  if imovel[2]==codigo:
    obra.remove(imovel)

for imovel in obra:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Código.......: ", elemento[2])
  print("Cidade.: ", elemento[3])