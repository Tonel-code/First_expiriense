import random
stag_all = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
lift_start = random.choice(stag_all)
# power_on_off = 1
while True:
    maximum = max(stag_all)
    print ("Количество этажей - ", maximum)
    print("Положение лифта - этаж ", lift_start)

    call = int(input("Введите этаж для вызова лифта: "))
    while call < 1 or call > 17:
        call = int(input("Несуществующий этаж. Введите этаж для вызова лифта: "))

    if call == lift_start:
        print("Текущий этаж - ", call)
        stag_end = int(input("Введите этаж назначения: "))
        while stag_end == lift_start:
            stag_end = int(input("Вы на этом этаже. Введите этаж назначения: "))
        while stag_end < 1 or stag_end > 17:
            stag_end = int(input("Несуществующий этаж. Введите этаж назначения: "))
        if stag_end != 1 and stag_end < call:
            print(stag_all[call - 1:stag_end - 2:-1])
        elif stag_end > call and stag_end != 1:
            print("Промежуточные этажи - ", stag_all[call:stag_end:])
        elif stag_end == 1:
            print("Промежуточные этажи - ", stag_all[call - 1:stag_end - 1:-1])
        print("Текущий этаж - ", stag_end)
        print("__________________________________________________________")
    else:
        if call != 1 and call < lift_start:
            print("Промежуточные этажи - ", stag_all[lift_start - 1:call - 2:-1])
        elif call != 1 and call > lift_start:
            print("Промежуточные этажи - ", stag_all[lift_start:call:])
        elif call == 1:
            print("Промежуточные этажи - ", stag_all[lift_start - 1:call - 1:-1])
        lift_start = call
        print("Текущий этаж - ", lift_start)
        stag_end = int(input("Введите этаж назначения: "))
        while stag_end == lift_start:
            stag_end = int(input("Вы на этом этаже. Введите этаж назначения: "))
        while stag_end < 1 or stag_end > 17:
            stag_end = int(input("Несуществующий этаж. Введите этаж назначения: "))
        if stag_end != 1 and stag_end < lift_start:
            print("Промежуточные этажи - ", stag_all[lift_start - 1:stag_end - 2:-1])
        elif stag_end != 1 and stag_end > lift_start:
            print("Промежуточные этажи - ", stag_all[lift_start:stag_end:])
        elif stag_end == 1:
            print("Промежуточные этажи - ", stag_all[lift_start - 1:stag_end - 1:-1])
        print("Текущий этаж - ", stag_end)
        print("__________________________________________________________")

    lift_start = stag_end

# print(lift_start)