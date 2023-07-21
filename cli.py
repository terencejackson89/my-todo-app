from todo_functions import read_tasks, write_tasks
import time

time_string = time.strftime("%B %d %Y %H:%M:%S")
print(f"Hello. It is currently {time_string}")

while True:
    option = input("Select add, show, edit, complete, or exit: ").strip().lower()

    if option.startswith('add'):
        task = option[4:]

        tasks = read_tasks()

        tasks.append(task.capitalize() + '\n')

        write_tasks(tasks)

        print(task.capitalize() + ' added!')

    elif option.startswith('show'):
        tasks = read_tasks()

        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")

    elif option.startswith('edit'):
        try:
            idx = int(option[5:].strip())
            tasks = read_tasks()
            new_task = input("Enter a new task for this slot: ").capitalize() + '\n'
            tasks[idx - 1] = new_task
            write_tasks(tasks)
            print("Task", idx, "successfully updated!")
        except ValueError:
            print("Please select the index of an existing task")

    elif option.startswith('complete'):
        try:
            idx = int(option[9:].strip())
            tasks = read_tasks()
            task = tasks[idx - 1]
            tasks.pop(idx - 1)
            write_tasks(tasks)
            print("Task: '{}' has been completed!".format(task))
        except IndexError:
            print("Please enter a valid index of a task")

    elif option == 'exit':
        break

    else:
        print("Please select a valid option")
