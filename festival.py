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
from typing import NamedTuple, Sequence, Set

movies = ["Greed", "Harvest", "Limelight"]


def valid_day_schedule(day_schedule: Sequence[str]):
    """
    Checks if day_schedule is an ordering of available movies,
    of length at least 1, without repeating any movies.
    """
    return day_schedule and day_schedule in permutations(movies, r=len(day_schedule))


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

    @property
    def valid_day_schedules(self):
        """
        Checks if all day schedules are orderings of available movies,
        of length at least 1, without repeating any movies,
        but not whether they meet the special requirements for
        particular days of the week.
        """
        return all(
            valid_day_schedule(day)
            for day in (self.thursday, self.friday, self.saturday)
        )

    @property
    def thursday_rule(self):
        """
        On Thursday Harvest is shown, and no film is shown after it on that day.
        """
        return self.thursday[-1:] == ("Harvest",)

    @property
    def friday_rule(self):
        """
        On Friday either Greed or Limelight, but not both, is shown,
        and no film is shown after it on that day.
        """
        return self.friday[-1:] in [("Greed",), ("Limelight",)] and not (
            "Greed" in self.friday and "Limelight" in self.friday
        )

    @property
    def saturday_rule(self):
        """
        On Saturday either Greed or Harvest, but not both, is shown,
        and no film is shown after it on that day.
        """
        return self.saturday[-1:] in [("Greed",), ("Harvest",)] and not (
            "Greed" in self.saturday and "Harvest" in self.saturday
        )

    @property
    def valid_weekend_schedule(self):
        """
        Checks to see if the schedule satisfies all the constraints
        in the logic problem.
        """
        return (
            self.valid_day_schedules
            and self.thursday_rule
            and self.friday_rule
            and self.saturday_rule
            and len(self.screened_movies) == 3
        )
