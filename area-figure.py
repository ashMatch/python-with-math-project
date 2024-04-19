import type_area
print("Esse programa calcula a area de uma figura plana")
game_on = input("você quer jogar?[y]yes/[n]no: ")

if (game_on.lower() == "y") is False:
    print("\nBeleza! Se não quiser jogar eu nao vou te forçar.")
    print("Seu corpo suas regras\n")
else:
    print("escolha qual figura voce quer")
    print("Quadrado = 1")
    print("Retangulo = 2")
    print("Triangulo = 3")
    print("Circunferencia = 4")
    user_choice = input("escolha o numero da opção que voce quer ")

    
    ## print(type(user_choice))
    ## print(type_area.type_area(int(user_choice)))
