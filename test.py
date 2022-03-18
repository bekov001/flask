from requests import get, post, delete


def create():
    """Создает работу с id = 100"""
    res = post("http://127.0.0.1:5000/api/v2/jobs", json={"id": 100, "job": "cool", "work_size": "12", "collaborators": "123", "is_finished": True, "team_leader": 1})
    print(res.json(), )


def delete_job():
    """удаляем"""
    res = delete("http://127.0.0.1:5000/api/v2/jobs/1")
    print(res.json())


def get_all():
    res = get("http://127.0.0.1:5000/api/v2/jobs")
    print(res.json())


def get_one():
    res = get("http://127.0.0.1:5000/api/v2/jobs/1")
    print(res.json())


if "__main__" == __name__:
    create()
    get_one()
    get_all()
    delete_job()
