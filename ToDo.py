import json
import os
from tabulate import tabulate

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"desc": description, "done": False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    table = [[i + 1, t["desc"], "✔" if t["done"] else "✘"] for i, t in enumerate(tasks)]
    print(tabulate(table, headers=["#", "Задача", "Статус"]))

def mark_done(index):
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    del tasks[index]
    save_tasks(tasks)

# Пример работы (для теста)
if __name__ == "__main__":
    add_task("Выучить Git")
    add_task("Сделать TODO приложение")
    list_tasks()
