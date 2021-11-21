"""


"""


def solution(ings, menu, sell):
    # Hashing ings
    ings_dict = dict()
    for s in ings:
        name, price = s.split()
        ings_dict[name] = int(price)
    # print(ings_dict)

    # Hashing menu
    menu_dict = dict()
    for s in menu:
        name, ing, price = s.split()
        ingPrice = 0
        for i in list(ing):
            ingPrice += ings_dict[i]
        menu_dict[name] = int(price) - ingPrice
    
    # Calculate Sell
    answer = 0
    for s in sell:
        menu, amount = s.split()
        answer += menu_dict[menu]*int(amount)
    return answer

print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
print(solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"]))
