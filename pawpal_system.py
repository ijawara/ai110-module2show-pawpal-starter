from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time
from typing import Dict, List, Optional


@dataclass
class Task:
    title: str
    time_duration: int  # minutes
    priority: str
    frequency: str
    pet_id: Optional[str] = None
    completed: bool = False

    def mark_completed(self) -> None:
        pass

    def update_priority(self, priority: str) -> None:
        pass

    def reschedule(self, new_time: time) -> None:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    weight: float
    age: int
    needs: Optional[PetNeed] = None

    def update_weight(self, weight: float) -> None:
        pass

    def update_age(self, age: int) -> None:
        pass

    def assign_needs(self, needs: PetNeed) -> None:
        pass


class PetNeed:
    def __init__(
        self,
        medications: Optional[List[str]] = None,
        desired_walks_per_day: int = 0,
        feeding_intervals: Optional[List[time]] = None,
        extra_needs: Optional[List[str]] = None,
    ) -> None:
        self.medications: List[str] = medications or []
        self.desired_walks_per_day: int = desired_walks_per_day
        self.feeding_intervals: List[time] = feeding_intervals or []
        self.extra_needs: List[str] = extra_needs or []

    def add_medication(self, medication: str) -> None:
        pass

    def set_desired_walks(self, count: int) -> None:
        pass

    def add_feeding_interval(self, interval: time) -> None:
        pass

    def add_need(self, need: str) -> None:
        pass


class Calendar:
    def __init__(
        self,
        date: Optional[date] = None,
    ) -> None:
        self.date: date = date or datetime.now().date()
        self.agenda_entries: List[str] = []

    def add_entry(self, timeslot: time, activity: str) -> None:
        pass

    def generate_daily_schedule(self, owner: Owner, pet: Pet, day: date) -> None:
        pass

    def get_agenda(self) -> List[str]:
        pass


class Owner:
    def __init__(
        self,
        owner_id: str,
        name: str,
        contact_info: str,
        pets: Optional[List[Pet]] = None,
        tasks: Optional[List[Task]] = None,
    ) -> None:
        self.owner_id: str = owner_id
        self.name: str = name
        self.contact_info: str = contact_info
        self.pets: List[Pet] = pets or []
        self.tasks: List[Task] = tasks or []
        self.availability: Dict[date, str] = {}

    def add_pet(self, pet: Pet) -> None:
        pass

    def add_task(
        self,
        name: str,
        time_duration: int,
        priority: str,
        frequency: str,
        pet_id: Optional[str] = None,
    ) -> None:
        pass

    def get_pet_schedule(self, day: date) -> List[str]:
        pass

    def set_availability(self, day: date, time_range: str) -> None:
        pass
