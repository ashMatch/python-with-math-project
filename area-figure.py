from AreaMath import AreaMath
from type_area import type_area

area_math = AreaMath(4,5)

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
    print("Trapezoid = 5")
    user_choice = int(input("escolha o numero da opção que voce quer "))

    if user_choice == 1:
        print("Area do quadrado")
        print("\nA = L²\n")
        print(area_math.square_math())
    elif user_choice == 2:
        print("Area do Retangulo")
        print("\nA = Base x Altura\n")
        print(area_math.rectangle_math())
    elif user_choice ==3:
        print("Area do Triangulo")
        print("\nresultado igual:")
        print(area_math.triangle_math())
    elif user_choice == 4:
        print("Area da Circunferencia")
        print("\nA = PI x R²\n")

    elif user_choice == 5:
        print("Area da Trapezoid")
        print("\nA = (Base Maior + Base Menor/2) x h\n")
    
    ## print(type(user_choice))
    ## print(type_area.type_area(int(user_choice)))
