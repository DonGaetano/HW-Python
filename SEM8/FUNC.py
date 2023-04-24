def add_contact(contact):
    data = open('telephones.txt', 'a')
    data.writelines(contact)
    data.write('\n')
    data.close()

def search_contact():
    contact_list = open('telephones.txt', 'r')
    search = input("Введите фамилию для поиска: ")
    for i in contact_list:
        if search in i:
            print(i)
    contact_list.close()

def print_contacts():
    contact_list = open('telephones.txt', 'r')
    num = 1
    for i in contact_list:
        print(f"{num}. {i}")
        num+=1
    contact_list.close()

def delete_contact(search):
    contact_list = open('telephones.txt', 'r')
    temp_list = []
    for i in contact_list:
        if search in i:
            continue
        temp_list.append(i)
    contact_list.close()

    contact_list = open('telephones.txt', 'w')
    for i in temp_list:
        contact_list.writelines(i)
    contact_list.close


def change_contact():
    contact_list = open('telephones.txt', 'r')
    temp_list = []
    name_to_check = input("Введите фамилию для поиска и изменения: ")
    data_to_change = input('Введите поле, которое нужно изменить("Имя", "Фамилия", "Отчество" или "Телефон"): ')
    new_data = input(f"Введите новое значение для поля {data_to_change} ")

    for i in contact_list:
        if name_to_check in i:
            data = i.split()
            if data_to_change == "Имя":
                data[0] = new_data
            if data_to_change == "Фамилия":
                data[1] = new_data
            if data_to_change == "Отчество":
                data[2] = new_data
            if data_to_change == "Телефон":
                data[3] = new_data
            changed_line = ''.join(data) + '\n'
            temp_list.append(changed_line)
        else:
            temp_list.append(i)
    contact_list.close()

    contact_list = open('telephones.txt', 'w')
    for i in temp_list:
        contact_list.writelines(i)
    contact_list.close()
