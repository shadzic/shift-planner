from src.inputs import get_people


def test_end_to_end():
    people = get_people()
    people_name = [p.name for p in people]
    people_contract_hours = [p.contract_hours for p in people]

    assert len(people) == 2
    assert 'jenny' in people_name
    assert 'marc' in people_name
