def rifma(input):
    my_st = input("Введите текст: ").split()
    v = lambda x: sum(1 for i in x if i in "аеёиоуыэюя")
    tmp = v(my_st[0])
    if all([v(i) == tmp for i in my_st]):
        return 'Парам пам-пам'
    return 'Пам парам'
print(rifma(input))
        