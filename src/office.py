import datetime
from datetime import datetime
import time
from collections import defaultdict


class Office:
    def __init__(self, name):
        self.name = name
        self.people_working = {}
        # a record of how many hours each employee has worked at this office
        # {week_number: {employee: [(start_time, end_time)...]}}
        self.time_sheet = defaultdict(lambda: defaultdict(list))

    def start_working_for(self, person):
        self.people_working[person.name] = person
        # add start time to timesheet
        current_date = datetime.now()
        self.time_sheet[current_date.isocalendar()[1]][person.name].append([datetime.now()])

    def finish_working_for(self, person):
        self.people_working.pop(person.name)
        current_date = datetime.now()
        current_year = current_date.isocalendar()[0]
        current_week = current_date.isocalendar()[1]
        # case employee hasn't stopped working since last week
        if current_week not in self.time_sheet:

            previous_week = current_week - 1
            end_of_previous_week = time.asctime(time.strptime('{} {} 1'.format(current_year, previous_week), '%Y %W %w'))
            end_of_previous_week = datetime.datetime.fromtimestamp(time.mktime(end_of_previous_week)).date()

            # update timesheet with end date of previous week
            self.time_sheet[previous_week][person.name][-1].append(end_of_previous_week)
            # update timesheet with end date of current week
            self.time_sheet[current_week][person.name][-1].append((end_of_previous_week, datetime.now()))

        else:
            self.time_sheet[current_week][person.name][-1].append(datetime.now())

    def display_time_sheet(self):
        for week_number, value in self.time_sheet.items():
            print(f"week: {week_number}")
            for employee, time_periods in value.items():
                hours = 0
                for time_period in time_periods:
                    if len(time_period) > 1:
                        diff = time_period[1] - time_period[0]
                        diff = diff.total_seconds()/3600
                        hours += diff
                print(f"employee: {employee} hours: {hours}")

                if hours > 40:
                    print("This employee is owed overtime pay!")






