from requests import put, get, post


def check(func):
    """Функция проверки, сверяет изменилась ли первая работа и печатает
    correct или incorrect"""
    def wrapper():
        a = (get("http://127.0.0.1:5000/api/job/1").json())
        func()
        b = (get("http://127.0.0.1:5000/api/job/1").json())
        print("correct" if a != b else "incorrect")
    return wrapper


def create():
    """Создает работу с id = 1"""
    res = post("http://127.0.0.1:5000/api/jobs", json={"id": 1, "job": "cool", "work_size": "12", "collaborators": "123", "is_finished": True, "team_leader.id": 1})
    print(res.json(), )


@check
def correct():
    """Правильно оформленное изменение работы"""
    res = put("http://127.0.0.1:5000/api/job/1", json={'collaborators': '2, 3', 'id': 5, 'is_finished': False, 'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 20})
    print(res.json())


@check
def return_back():
    """Меняет id с 1 на 5"""
    res = put("http://127.0.0.1:5000/api/job/5", json={'collaborators': '2, 3', 'id': 1, 'is_finished': False, 'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 20})
    print(res.json())


@check
def wrong_word():
    res = put("http://127.0.0.1:5000/api/job/hello", json={'collaborators': '2, 3', 'is_finished': False, 'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 20})
    print(res.json())


@check
def wrong_num():
    res = put("http://127.0.0.1:5000/api/job/1000", json={'collaborators': '2, 3', 'is_finished': False, 'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 20})
    print(res.json())


@check
def not_all_data():
    """Не вся информация"""
    res = put("http://127.0.0.1:5000/api/job/1", json={'team_leader': 1, 'work_size': 50})
    print(res.json())


@check
def exists_id():
    res = put("http://127.0.0.1:5000/api/job/1", json={"id": 1, 'team_leader': 1, 'work_size': 50})
    print(res.json())


if "__main__" == __name__:
    create()
    correct()
    return_back()
    wrong_word()
    wrong_num()
    not_all_data()
    exists_id()