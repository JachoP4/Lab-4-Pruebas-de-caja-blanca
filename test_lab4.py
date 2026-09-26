import process_grades
import pytest

@pytest.mark.parametrize('students, expected', 
                         [
                             ([{'name': 'Ana', 'grades': [90, 90, 90]}], ['Ana'])
                             ]
                             ) #'students. expected', [({'names': 'Ana', 'grades': [90,90,90]})], 'passed', [({'names': 'Marcus', 'grades': [50,70,50]})], 'failed'
def test_procces_grades_passed_recovery(students, expected, capsys):
    result = process_grades.process_grades(students)
    assert result['passed'] == expected

@pytest.mark.parametrize('students, expected', 
                         [
                             ([{'name': 'Marcus', 'grades': [60, 60, 60]}], 'recovery')
                             ]
                             )
def test_procces_grades_passed_recovery(students, expected, capsys):
    process_grades.process_grades(students)
    captured = capsys.readouterr()
    assert expected in captured.out