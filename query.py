from random import randint, choices

from data.db_session import global_init, create_session
from data.users import Jobs, OldUser


global_init(input())
session = create_session()
news = OldUser(
    name="Scott",
    surname="Ridley",
    age=21,
    position="captain",
    speciality="research engineer",
    address="module_1",
    email="scott_chief@mars.org",

)
news.set_password("123456")
session.add(news)
session.commit()

data = [["Anuar", "Oleg", "Tair"],
        ["Sure", "Legenda", "Cook"],
        [randint(10, 100)
         for i in range(3)],
        ["assessment"] * 3,
        ["engineer", "it-speciality", "worker"],
        [f"module_{i}" for i in range(1, 4)],
        [f"{choices('hellloeowkfwjfwefkwjfkewjf', k=6)}@mars.org"
         for i in range(3)]
        ]
for i in range(3):
    news = OldUser(
        name=data[0][i],
        surname=data[1][i],
        age=data[2][i],
        position=data[3][i],
        speciality=data[4][i],
        address=data[5][i],
        email=data[6][i],

    )
    news.set_password("123456")
    session.add(news)
    session.commit()


for user in session.query(OldUser).all():
    print(user.name, user.surname)