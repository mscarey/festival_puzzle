import pytest

import festival

ANSWER_CHOICES = {
    "A": festival.WeekendSchedule(
        thursday=("Limelight", "Harvest"), friday=("Limelight",), saturday=("Harvest",)
    ),
    "B": festival.WeekendSchedule(
        thursday=("Harvest",),
        friday=("Greed", "Limelight"),
        saturday=("Limelight", "Greed"),
    ),
    "C": festival.WeekendSchedule(
        thursday=("Harvest",), friday=("Limelight",), saturday=("Limelight", "Greed")
    ),
    "D": festival.WeekendSchedule(
        thursday=("Greed", "Harvest", "Limelight"),
        friday=("Limelight",),
        saturday=("Greed",),
    ),
    "E": festival.WeekendSchedule(
        thursday=("Greed", "Harvest"),
        friday=("Limelight", "Harvest"),
        saturday=("Harvest",),
    ),
    "same movie all day": festival.WeekendSchedule(
        thursday=("Harvest", "Harvest"),
        friday=("Greed", "Greed"),
        saturday=("Limelight",),
    ),
    "no movies": festival.WeekendSchedule(thursday=(), friday=(), saturday=()),
}


@pytest.mark.parametrize(
    "answer_choice, expected",
    [
        ("A", True),
        ("B", True),
        ("C", True),
        ("D", True),
        ("E", True),
        ("same movie all day", False),
        ("no movies", False),
    ],
)
def test_schedules_are_orders_of_available_movies(answer_choice, expected):
    """
    Checks whether all of the WeekendSchedule's daily schedules
    are orderings of the available movies, of length at least 1,
    without repeating any movies on the same day.
    """
    assert ANSWER_CHOICES[answer_choice].valid_day_schedules == expected


@pytest.mark.parametrize(
    "answer_choice, expected",
    [
        ("A", True),
        ("B", True),
        ("C", True),
        ("D", False),
        ("E", True),
        ("same movie all day", True),
        ("no movies", False),
    ],
)
def test_thursday_rule(answer_choice, expected):
    assert ANSWER_CHOICES[answer_choice].thursday_rule == expected


@pytest.mark.parametrize(
    "answer_choice, expected",
    [
        ("A", True),
        ("B", False),
        ("C", True),
        ("D", True),
        ("E", False),
        ("same movie all day", True),
        ("no movies", False),
    ],
)
def test_friday_rule(answer_choice, expected):
    assert ANSWER_CHOICES[answer_choice].friday_rule == expected


@pytest.mark.parametrize(
    "answer_choice, expected",
    [
        ("A", True),
        ("B", True),
        ("C", True),
        ("D", True),
        ("E", True),
        ("same movie all day", False),
        ("no movies", False),
    ],
)
def test_saturday_rule(answer_choice, expected):
    assert ANSWER_CHOICES[answer_choice].saturday_rule == expected


@pytest.mark.parametrize(
    "answer_choice, expected",
    [
        ("A", False),
        ("B", False),
        ("C", True),
        ("D", False),
        ("E", False),
        ("same movie all day", False),
        ("no movies", False),
    ],
)
def test_get_correct_answer(answer_choice, expected):
    """
    Checks whether the WeekendSchedule satisfies all the rules
    in the logic puzzle.
    """
    assert ANSWER_CHOICES[answer_choice].valid_weekend_schedule == expected
