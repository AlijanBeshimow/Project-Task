import pickle


def load_tasks():
    try:
        with open("tasks.pickle", 'rb') as f:
            loaded_tasks = pickle.load(f)
            return loaded_tasks
    except:
        with open("tasks.pickle", 'wb') as f:
            pickle.dump([], f)
            return []


def save_tasks(tasks):
    with open("tasks.pickle", 'wb') as f:
        pickle.dump(tasks, f)
