import pytest
from src.office import Office
from src.person import Person
import datetime
from datetime import datetime


def test_finish_working():
    office = Office("test_office")
    eduardo = Person("Eduardo")
    boris = Person("Boris")
    office.start_working_for(eduardo)
    office.start_working_for(boris)
    office.finish_working_for(eduardo)
    assert "Boris" in office.people_working
    assert "Eduardo" not in office.people_working
    current_date = datetime.now()
    current_week = current_date.isocalendar()[1]
    assert len(office.time_sheet[current_week]["Boris"]) == 1
    assert len(office.time_sheet[current_week]["Boris"][0]) == 1

    assert len(office.time_sheet[current_week]["Eduardo"]) == 1
    assert len(office.time_sheet[current_week]["Eduardo"][0]) == 2

