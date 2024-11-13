#dict
my_dict = {'Nikolai': 2002,
           'Matvei': 1999,
           'Vasilii': 2001}
print('Dict:', my_dict)
my_dict.update ({'Kate': 2004,
                'Eva': 2005})
print('Existing value:', my_dict['Vasilii'])
print('Not existing value:', my_dict.get('Lina'))
del_ = my_dict.pop('Nikolai')
print('Delete value:', del_)
print('Modified dict:', my_dict)

print()

#set
my_set = {135, 'Agusha', 0.1234, 'Agusha', 135}
print('Set:', my_set)
my_set.update({9.8765, 'Frutonyanya'})
my_set.remove (135)
print('New set:', my_set)
