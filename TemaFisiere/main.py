import csv

# Numele fișierelor
CATEGORIES_FILE = 'categories.csv'
TASKS_FILE = 'tasks.csv'


# Funcția pentru adăugarea unei noi categorii
def add_category(category):
    with open(CATEGORIES_FILE, 'r') as file:
        categories = file.read().splitlines()
        if category in categories:
            print("Categoria există deja.")
            return

    with open(CATEGORIES_FILE, 'a') as file:
        file.write(category + '\n')


# Funcția pentru adăugarea unui nou task
def add_task(task, deadline, responsible, category):
    with open(CATEGORIES_FILE, 'r') as file:
        categories = file.read().splitlines()
        if category not in categories:
            print("Categoria nu există.")
            return

    with open(TASKS_FILE, 'r') as file:
        tasks = list(csv.reader(file))
        for row in tasks:
            if task == row[0]:
                print("Taskul există deja.")
                return

    with open(TASKS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task, deadline, responsible, category])


# Funcția pentru listarea task-urilor în funcție de categorie
def list_tasks_by_category():
    with open(TASKS_FILE, 'r') as file:
        tasks = list(csv.reader(file))
        tasks.sort(key=lambda x: x[3])  # Sortare după categorie

        for row in tasks:
            print(f"Task: {row[0]}, Deadline: {row[1]}, Responsabil: {row[2]}, Categorie: {row[3]}")


# Funcția pentru sortare
def sort_tasks(option):
    options = {
        1: lambda tasks: sorted(tasks, key=lambda x: x[0]),  # sortare ascendentă după task
        2: lambda tasks: sorted(tasks, key=lambda x: x[0], reverse=True),  # sortare descendentă după task
        3: lambda tasks: sorted(tasks, key=lambda x: x[1]),  # sortare ascendentă după dată
        4: lambda tasks: sorted(tasks, key=lambda x: x[1], reverse=True),  # sortare descendentă după dată
        5: lambda tasks: sorted(tasks, key=lambda x: x[2]),  # sortare ascendentă după persoană responsabilă
        6: lambda tasks: sorted(tasks, key=lambda x: x[2], reverse=True),
        # sortare descendentă după persoană responsabilă
        7: lambda tasks: sorted(tasks, key=lambda x: x[3]),  # sortare ascendentă după categorie
        8: lambda tasks: sorted(tasks, key=lambda x: x[3], reverse=True),  # sortare descendentă după categorie
    }

    with open(TASKS_FILE, 'r') as file:
        tasks = list(csv.reader(file))
        tasks = options.get(option, lambda tasks: tasks)(tasks)

        for row in tasks:
            print(f"Task: {row[0]}, Deadline: {row[1]}, Responsabil: {row[2]}, Categorie: {row[3]}")


def read_categories_from_input():
    categories = input("Introduceți categoriile separate prin virgulă: ")
    category_list = [category.strip() for category in categories.split(',')]

    for category in category_list:
        add_category(category)


# Funcția pentru filtrare
def filter_tasks(field, value):
    fields = {
        1: 0,  # Task
        2: 1,  # Data
        3: 2,  # Persoană responsabilă
        4: 3,  # Categorie
    }

    field_index = fields.get(field)
    if field_index is None:
        print("Opțiunea de filtrare nu este validă.")
        return

    with open(TASKS_FILE, 'r') as file:
        tasks = list(csv.reader(file))
        filtered_tasks = [row for row in tasks if row[field_index].startswith(value)]

        for row in filtered_tasks:
            print(f"Task: {row[0]}, Deadline: {row[1]}, Responsabil: {row[2]}, Categorie: {row[3]}")


# Funcția pentru adăugarea unui nou task
def add_new_task():
    task = input("Introduceți un nou task: ")
    deadline = input("Introduceți data limită (format: DD.MM.YYYY HH:MM): ")
    responsible = input("Introduceți persoana responsabilă: ")
    category = input("Introduceți categoria: ")

    add_task(task, deadline, responsible, category)


# Funcția pentru editarea detaliilor referitoare la un task
def edit_task():
    with open(TASKS_FILE, 'r') as file:
        tasks = list(csv.reader(file))
        for i, row in enumerate(tasks):
            print(f"{i + 1}. Task: {row[0]}, Deadline: {row[1]}, Responsabil: {row[2]}, Categorie: {row[3]}")

    choice = int(input("Introduceți numărul task-ului pe care doriți să îl editați: ")) - 1
    if choice < 0 or choice >= len(tasks):
        print("Numărul introdus nu este valid.")
        return
    task = input("Introduceți noul task: ")
    deadline = input("Introduceți noua dată limită (format: DD.MM.YYYY HH:MM): ")
    responsible = input("Introduceți noua persoană responsabilă: ")
    category = input("Introduceți noua categorie: ")

    tasks[choice] = [task, deadline, responsible, category]

    with open(TASKS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)


# Funcția pentru ștergerea unui task
def delete_task():
    with open(TASKS_FILE, 'r') as file:
        tasks = list(csv.reader(file))
        for i, row in enumerate(tasks):
            print(f"{i + 1}. Task: {row[0]}, Deadline: {row[1]}, Responsabil: {row[2]}, Categorie: {row[3]}")

    choice = int(input("Introduceți numărul task-ului pe care doriți să-l ștergeți: ")) - 1
    if choice < 0 or choice >= len(tasks):
        print("Numărul introdus nu este valid.")
        return

    del tasks[choice]

    with open(TASKS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)


# Meniul principal
def main_menu():
    read_categories_from_input()
    while True:
        print("\n----- MENIU -----")
        print("1. Listare date")
        print("2. Sortare")
        print("3. Filtrare date")
        print("4. Adăugare task")
        print("5. Editare task")
        print("6. Ștergere task")
        print("0. Ieșire")

        choice = int(input("Introduceți opțiunea dorită: "))

        if choice == 1:
            list_tasks_by_category()
        elif choice == 2:
            sort_option = int(input("Introduceți opțiunea de sortare dorită: "))
            sort_tasks(sort_option)
        elif choice == 3:
            filter_field = int(input("Introduceți câmpul după care se realizează filtrarea: "))
            filter_value = input("Introduceți valoarea utilizată pentru filtrare: ")
            filter_tasks(filter_field, filter_value)
        elif choice == 4:
            add_new_task()
        elif choice == 5:
            edit_task()
        elif choice == 6:
            delete_task()
        elif choice == 0:
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")


# Rularea meniului principal
if __name__ == '__main__':
    main_menu()
