from src.office import Office
from src.person import Person


def work():
    office = Office("e-corus")
    eduardo = Person("Eduardo")
    boris = Person("Boris")
    print(office.people_working)
    office.start_working_for(eduardo)
    office.start_working_for(boris)
    print(office.people_working)
    office.finish_working_for(eduardo)
    print(office.people_working)

    office.display_time_sheet()


if __name__ == '__main__':
    work()