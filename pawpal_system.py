import uuid
from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    description: str
    priority: str  # one of "low", "medium", "high"
    duration_minutes: int
    is_completed: bool = False
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    pet_id: str | None = None  # scopes the task to a specific Pet; None means unassigned

    def mark_complete(self) -> None:
        # TODO: implement
        pass

    def mark_incomplete(self) -> None:
        # TODO: implement
        pass


@dataclass
class Pet:
    name: str
    species: str
    age_years: int
    task_list: list[Task] = field(default_factory=list)
    pet_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def add_task(self, task: Task) -> None:
        # TODO: implement
        pass

    def remove_task(self, task_id: str) -> None:
        # TODO: implement
        pass

    def get_tasks_by_priority(self) -> list[Task]:
        # TODO: implement
        pass

    def get_pending_tasks(self) -> list[Task]:
        # TODO: implement
        pass


class Owner:
    def __init__(self, name: str) -> None:
        self.owner_id: str = str(uuid.uuid4())
        self.name: str = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        # TODO: implement
        pass

    def remove_pet(self, pet_id: str) -> None:
        # TODO: implement
        pass

    def get_pets(self) -> list[Pet]:
        # TODO: implement
        pass


class Schedule:
    def __init__(self, pet: Pet) -> None:
        self.schedule_id: str = str(uuid.uuid4())
        self.pet: Pet = pet
        self.ordered_tasks: list[Task] = []
        self.reasoning: str = ""
        self.is_published: bool = False

    def generate(self, tasks: list[Task]) -> None:
        # TODO: implement
        pass

    def sort_by_duration(self) -> None:
        # TODO: implement
        pass

    def sort_by_priority(self) -> None:
        # TODO: implement
        pass

    def get_total_duration(self) -> int:
        # TODO: implement
        pass

    def get_summary(self) -> str:
        # TODO: implement
        pass

    def explain_reasoning(self) -> str:
        # TODO: implement
        pass
