from requests import put, get, post, delete


def create():
    """Создает работу с id = 1"""
    res = post("http://127.0.0.1:5000/api/v2/jobs", json={"id": 3, "job": "cool", "work_size": "12", "collaborators": "123", "is_finished": True, "team_leader": 1})
    print(res.json(), )


def change():
    """Правильно оформленное изменение работы"""
    res = put("http://127.0.0.1:5000/api/v2/jobs/1", json={'collaborators': '2, 3', 'id': 5, 'is_finished': False, 'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 20})
    print(res.json())


def delete_job():
    """удаляем"""
    res = delete("http://127.0.0.1:5000/api/jobs/1")
    print(res.json())


def wrong_word():
    res = put("http://127.0.0.1:5000/api/jobs/hello", json={'collaborators': '2, 3', 'is_finished': False, 'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 20})
    print(res.json())


def get_all():
    res = get("http://127.0.0.1:5000/api/jobs")
    print(res.json())


def get_one():
    """Не вся информация"""
    res = put("http://127.0.0.1:5000/api/jobs/1")
    print(res.json())


def exists_id():
    res = put("http://127.0.0.1:5000/api/job/1", json={"id": 1, 'team_leader': 1, 'work_size': 50})
    print(res.json())


if "__main__" == __name__:
    create()
    change()
    get_all()
    exists_id()
