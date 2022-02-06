lst = ['в', '5', 'часов', '17', 'минут', 'температура',
       'воздуха', 'была', '+5', 'градусов']

new_lst = int(len(lst))
for _ in range(new_lst):
        new_of_lst = lst.pop(0)
        if new_of_lst.count(".") == 0 and new_of_lst.isdigit() and new_of_lst.isalnum():
            lst.append(f'"{int(new_of_lst):02d}"')
        elif new_of_lst.count(".") == 0 and new_of_lst[0] == "+" and new_of_lst[1].isdigit():
             lst.append(f'"+{int(new_of_lst):02d}"')
        else:
             lst.append(new_of_lst)
             print(' '.join(lst))
