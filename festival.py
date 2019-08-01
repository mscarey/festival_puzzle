"""
Solves an LSAT problem about a film festival.

Exactly three films — Greed, Harvest, and Limelight — are shown during a
film club’s festival held on Thursday, Friday, and Saturday.
Each film is shown at least once during the festival but never more than
once on a given day. On each day at least one film is shown. Films are
shown one at a time. The following conditions apply:

* On Thursday Harvest is shown, and no film is shown after it on that day.
* On Friday either Greed or Limelight, but not both, is shown,
    and no film is shown after it on that day.
* On Saturday either Greed or Harvest, but not both, is shown,
    and no film is shown after it on that day.
"""

from itertools import permutations
import pprint
from typing import NamedTuple, Sequence, Set

movies = ["Greed", "Harvest", "Limelight"]
day_schedules = (
    schedule
    for schedule_length in range(1, len(movies) + 1)
    for schedule in permutations(movies, r=schedule_length)
)


def thursday_rule(movies: Sequence[str]):
    """
    On Thursday Harvest is shown, and no film is shown after it on that day.
    """
    return movies[-1] == "Harvest"


def friday_rule(movies: Sequence[str]):
    """
    On Friday either Greed or Limelight, but not both, is shown,
    and no film is shown after it on that day.
    """
    return movies[-1] != "Harvest" and not ("Greed" in movies and "Limelight" in movies)


def saturday_rule(movies: Sequence[str]):
    """
    On Saturday either Greed or Harvest, but not both, is shown,
    and no film is shown after it on that day.
    """
    return movies[-1] != "Limelight" and not ("Greed" in movies and "Harvest" in movies)


class WeekendSchedule(NamedTuple):
    thursday: Sequence[str]
    friday: Sequence[str]
    saturday: Sequence[str]

    @property
    def screened_movies(self) -> Set:
        """
        Returns the set of names of movies that were shown at least
        once during the festival.
        """
        return {*self.thursday, *self.friday, *self.saturday}


every_weekend_schedule = (
    WeekendSchedule(thursday, friday, saturday)
    for thursday in filter(thursday_rule, day_schedules)
    for friday in filter(friday_rule, day_schedules)
    for saturday in filter(saturday_rule, day_schedules)
)

valid_weekend_schedules = filter(
    lambda schedule: len(schedule.screened_movies) == 3, every_weekend_schedule
)

answer_choices = [
    WeekendSchedule(
        thursday=("Limelight", "Harvest"), friday=("Limelight",), saturday=("Harvest",)
    ),
    WeekendSchedule(
        thursday=("Harvest",),
        friday=("Greed", "Limelight"),
        saturday=("Limelight", "Greed"),
    ),
    WeekendSchedule(
        thursday=("Harvest",), friday=("Limelight",), saturday=("Limelight", "Greed")
    ),
    WeekendSchedule(
        thursday=("Greed", "Harvest", "Limelight"),
        friday=("Limelight",),
        saturday=("Greed",),
    ),
    WeekendSchedule(
        thursday=("Greed", "Harvest"),
        friday=("Limelight", "Harvest"),
        saturday=("Harvest",),
    ),
]

correct_answer = [
    schedule
    for schedule in valid_weekend_schedules
    if any(schedule == answer_choice for answer_choice in answer_choices)
]
pprint.pprint(correct_answer)
