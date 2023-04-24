import interface, FUNC


def user_response():
    flag = True
    while flag:
        action = interface.menu()
        if action == 1:
            FUNC.add_contact(interface.get_contact())
        elif action == 2:
            FUNC.search_contact()
        elif action == 3:
            FUNC.print_contacts()
        elif action == 4:
            FUNC.delete_contact(interface.get_delete_contact())
        elif action == 5:
            FUNC.change_contact
        else:
            flag = False

user_response()
