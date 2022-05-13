import pendulum

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
    shifts: list(Shift)

    def __init__(
            self,
            name: str,
            contract_hours: float,
            runner: bool,
            coatchecker: bool,
            shifts: list(Shift)
    ):
        self.name = name
        self.contract_hours = contract_hours
        self.runner = runner
        self.contract_hours = coatchecker
        self.shifts = shifts

class Shift:
    """
    Shift holds the variables that specify:
    - date and times for the shift
    - type of the shift (runner or coatcheck)
    - whether the shift is assigned or not
    - who was assigned to take this shift
    """
    datetime_start: pendulum.datetime.DateTime
    datetime_end: pendulum.datetime.DateTime
    type: str
    assigned: bool
    assigned_to: Person
    
    def __init__(
            self, 
            datetime_start: pendulum.datetime.DateTime, 
            datetime_end: pendulum.datetime.DateTime, 
            type: str, 
            assigned: bool, 
            assigned_to: Person
    ):
        """

        @type assigned_to: Person
        """
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.type = type
        self.assigned = assigned
        self.assigned_to = assigned_to        
