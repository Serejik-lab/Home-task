immutable_var = 1, 2, 3, 4.5, 'sao'
print(immutable_var)
# immutable_var[0] = 4
# Тип строки tuple не может изменяться, так как это некий фиксированный список, который не поддерживает назначение элементов

mutable_list = [1, 2, 3.5, 'sao']
mutable_list[0] = 5
mutable_list[1] = 14
mutable_list[2] = 0.001
mutable_list[3] = 'unknown'
mutable_list.append('Modified')
print(mutable_list)