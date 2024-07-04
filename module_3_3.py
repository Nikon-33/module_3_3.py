def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b="Маршал")
print_params(c=False)

values_list = ["Акула", False, 99]
values_dict = {"a": "Дельфин", "b": "True", "c": 66}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Змея", False]
print_params(*values_list_2, 44)
