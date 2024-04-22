from AreaMath import AreaMath
from type_area import type_area


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
        base = int(input("Informe a base: "))
        square_area = AreaMath(base)
        print(square_area.square_math())
    elif user_choice == 2:
        print("Area do Retangulo")
        print("\nA = Base x Altura\n")
        base = int(input("Informe a base: "))
        hight = int(input("Informe a altura: "))
        rectangle_area = AreaMath(base, hight)
        print(rectangle_area.rectangle_math())
        ##print(area_math.rectangle_math())
    elif user_choice ==3:
        print("Area do Triangulo")
        print("\nresultado igual:")
        base = int(input("Informe a base: "))
        hight = int(input("Informe a altura: "))
        triangle_area = AreaMath(base, hight)
        print(triangle_area.triangle_math())
    elif user_choice == 4:
        print("Area da Circunferencia")
        print("\nA = PI x R²\n")
        radius = int(input("Informe o raio da circunferencia: "))
        circle_area = AreaMath(0, 0, 0, radius)
        print(circle_area.circle_math())

    elif user_choice == 5:
        print("Area da Trapezoid")
        print("\nA = (Base Maior + Base Menor/2) x h\n")
        base = int(input("Informe a base menor: "))
        bigger_base = int(input("Informe a base maior: "))
        hight = int(input("Informe a altura: "))
        trapezoid_area = AreaMath(base, hight, bigger_base)
        print(trapezoid_area.trapezoid_math())

    ## print(type(user_choice))
    ## print(type_area.type_area(int(user_choice)))
