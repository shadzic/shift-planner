import pendulum
from typing import List


class Person:
    """
    Person holds variables that specify:
     - name of the person
     - the number of hours of the contract,
     - whether this person can work as a runner or as a coatchecker
     - the list of shifts already assigned to that person
    """
    name: str
    contract_hours: float
    runner: bool
    coatchecker: bool
    assigned_shifts: List['Shift']
    assigned_total_hours: float

    def __init__(
            self,
            name: str,
            contract_hours: float,
            runner: bool = True,
            coatchecker: bool = True,
            assigned_shifts: List['Shift'] = None,
            assigned_total_hours: float = 0
    ):
        self.name = name
        self.contract_hours = contract_hours
        self.runner = runner
        self.contract_hours = coatchecker
        self.assigned_shifts = assigned_shifts
        self.assigned_total_hours = assigned_total_hours


class Shift:
    """
    Shift holds the variables that specify:
    - date and times for the shift
    - task of the shift (runner or coatcheck)
    - whether the shift is assigned or not
    - who was assigned to take this shift
    """
    datetime_start: pendulum.datetime
    datetime_end: pendulum.datetime
    task: str
    assigned: bool
    assigned_to: Person

    def __init__(
            self,
            datetime_start: pendulum.datetime,
            datetime_end: pendulum.datetime,
            task: str,
            assigned: bool,
            assigned_to: Person
    ):
        """

        @type assigned_to: Person
        """
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.task = task
        self.assigned = assigned
        self.assigned_to = assigned_to

# from dataclasses import dataclass
# @dataclass
# class Person:
#     name: str
#