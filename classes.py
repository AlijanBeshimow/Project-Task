import datetime


class Task:
    def __init__(self, name="", user="", category="", task_info=""):
        self.name = name
        self.user = user
        self.category = category
        self.task_info = task_info
        self.created_date = datetime.date.today()
        self.completed_date = datetime.date.today()

    def __repr__(self):
        return f"""
{self.name.capitalize()}\t{self.created_date}\t{self.completed_date}\t{self.user.capitalize()}\t{self.task_info}\t{self.category}"""
