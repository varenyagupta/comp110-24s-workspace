"""Unit test writing practice."""

__author__ = "730567934"

import pytest

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_case_1():
    """Test the invert function with a case where the dictionary has unique values."""
    test_values = {'b': 'ball', 'c': 'cat'}
    assert invert(test_values) == {'ball': 'b', 'cat': 'c'}


def test_invert_case_2():
    """Test the invert function with an empty dictionary."""
    test_values = {}
    assert invert(test_values) == {}


def test_invert_case_3():
    """Test the invert function with a dictionary that has same values."""
    test_values = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError):
        invert(test_values)


def test_favorite_color_case_1():
    """Test the favorite_color function with a different favorite colors."""
    test_values = {'Varenya': 'white', 'Jake': 'blue', 'Mitchelle': 'yellow'}
    assert favorite_color(test_values) == 'white'


def test_favorite_color_empty_dict():
    """Test the favorite_color function with an empty dictionary."""
    test_values = {}
    assert favorite_color(test_values) == ""


def test_favorite_color_tie():
    """Test the favorite_color function with a case with same favorite colors."""
    test_values = {'Varenya': 'white', 'Jake': 'white', 'Mitchelle': 'yellow'}
    assert favorite_color(test_values) in ['white', 'yellow']


def test_count_same_elements():
    """Test the count function in which the list contains multiple same fruits."""
    test_values = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    assert count(test_values) == {'apple': 3, 'banana': 2, 'orange': 1}


def test_count_empty_list():
    """Test the count function with an empty list."""
    test_values = [] 
    assert count(test_values) == {}


def test_count_single_element_list():
    """Test the count function in which the list has different element."""
    test_values = ['apple', 'banana', 'orange']
    assert count(test_values) == {'apple': 1, 'banana': 1, 'orange': 1}


def test_alphabetizer_multiple_same_letter_words():
    """Test the alphabetizer function with words with same starting letters."""
    test_values = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test_values) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_empty_list():
    """Test the alphabetizer function with an empty list."""
    test_values = []
    assert alphabetizer(test_values) == {}


def test_alphabetize_multiple_words():
    """Test the alphabetizer function with different starting letters."""
    test_values = ("Python", "sugar", "Turtle")
    assert alphabetizer(test_values) == {'p': ['Python'], 's': ['sugar'], 't': ['Turtle']}


def test_update_attendance_multiple_updates():
    """Test the update_attendance function with multiple updates to the attendance log."""
    attendance_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    update_attendance(attendance_log, "Wednesday", "Kaleb")
    assert attendance_log == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_update_attendance_existing_day_new_attendee():
    """Test the update_attendance function with an existing day and a new person."""
    attendance_record = {'Monday': ['Vrinda', 'Kaleb']}
    update_attendance(attendance_record, 'Monday', 'Alyssa')
    assert attendance_record == {'Monday': ['Vrinda', 'Kaleb', 'Alyssa']}


def test_update_attendance_existing_day_existing_attendee():
    """Test the update_attendance function with an existing day and an existing attendee."""
    attendance_record = {'Monday': ['Alyssa', 'Vrinda']}
    update_attendance(attendance_record, 'Monday', 'Jack')
    assert attendance_record == {'Monday': ['Alyssa', 'Vrinda', 'Jack']}
