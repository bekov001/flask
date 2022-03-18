from random import randint, choices

from data.db_session import global_init, create_session
from data.news import Department
from data.users import Jobs, OldUser

global_init(input())

session = create_session() 
department = session.query(Department).filter(Department.id == 1).first()


# for lst in department.members.split(', '):
#     arr = list(map(int, lst))  # list of member`s ids (integers)
#     for num in arr:
#         for job in session.query(Jobs).all():
#             if num in [int(x) for x in job.collaborators.split(', ')]:
#                 work_hours[num] = work_hours.get(num, 0) + job.work_size
#         # print(work_hours)
#         if work_hours[num] > 25:
#             result.append(num)
# # print(result)
#
# for user in session.query(OldUser).all():
#     if user.id in result:
#         print(user.surname, user.name)