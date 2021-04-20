nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
suspeitacovid=input("Suspeita de Covid? ").upper()

while suspeitacovid!="SIM" and  suspeitacovid!="NAO":
    print("Digite SIM ou NAO")
    suspeitacovid = input("Suspeita Covid? ").upper()

if suspeitacovid=="SIM":
    print("Encaminhe o paciente para sala VERMELHA.")
else:
    print("Encaminhe o paciente para sala BRANCA.")

if idade >= 65:
    print("Paciente COM prioridade de atendimento.")
else:
    sexo=input("Digite o sexo do paciente: ").upper()
    if sexo=="FEMININO" and idade>12:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade de atendimento.")
        else:
            print("Paciente SEM prioridade de atendimento.")
    else:
        print("Paciente SEM prioridade de atendimento.")