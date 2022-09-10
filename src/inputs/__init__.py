import os
from src.config import Person
from typing import List
from yaml import load, CLoader


def get_people() -> List[Person]:
    """
    Returns the list of people initiated through people.yml file

    :return: list of working people
    """
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'people.yml'), 'r') as people_cfg_file:
        people_config = load(people_cfg_file.read(), Loader=CLoader)

    return [Person(**p) for p in people_config]
