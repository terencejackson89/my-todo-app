FILEPATH = 'tasks.txt'


def read_tasks(filepath=FILEPATH):
    """ reads a file line-by-line into a list,
    and returns list to user
    """
    with open(filepath, 'r') as file:
        task_list = file.readlines()
    return task_list


def write_tasks(task_list, filepath=FILEPATH):
    """ writes a list of items into a file """
    with open(filepath, 'w') as file:
        file.writelines(task_list)


if __name__ == "__main__":
    print("HELLO FROM FUNCTIONS!!!")