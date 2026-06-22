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
        """Mark this task as completed."""
        self.is_completed = True

    def mark_incomplete(self) -> None:
        """Mark this task as not completed."""
        self.is_completed = False


@dataclass
class Pet:
    name: str
    species: str
    age_years: int
    task_list: list[Task] = field(default_factory=list)
    pet_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def add_task(self, task: Task) -> None:
        """Append a task to this pet's task list."""
        self.task_list.append(task)

    def remove_task(self, task_id: str) -> None:
        """Remove the task matching the given task_id from this pet's task list."""
        self.task_list.remove(next(task for task in self.task_list if task.task_id == task_id))

    def get_pending_tasks(self) -> list[Task]:
        """Return all tasks in this pet's task list that are not yet completed."""
        new_list = []
        for task in self.task_list:
            if not task.is_completed:
                new_list.append(task)
        return new_list


class Owner:
    def __init__(self, name: str) -> None:
        """Initialize an Owner with a unique ID, a name, and an empty pet roster."""
        self.owner_id: str = str(uuid.uuid4())
        self.name: str = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's roster."""
        self.pets.append(pet)

    def remove_pet(self, pet_id: str) -> None:
        """Remove the pet matching the given pet_id from this owner's roster."""
        self.pets.remove(next(p for p in self.pets if p.pet_id == pet_id))

    def get_pet(self, pet_name: str) -> Pet | None:
        """Return the first pet with the given name, or None if not found."""
        return next((p for p in self.pets if p.name == pet_name), None)


class Schedule:
    def __init__(self, pet: Pet) -> None:
        """Initialize a Schedule for a pet, seeding ordered_tasks from the pet's task list."""
        self.schedule_id: str = str(uuid.uuid4())
        self.pet: Pet = pet
        self.ordered_tasks: list[Task] = pet.task_list
        self.reasoning: str = ""

    def generate(self) -> None:
        """Sort pending tasks by priority then duration and record the ordering rationale."""
        PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
        pending = [t for t in self.ordered_tasks if not t.is_completed]
        pending.sort(key=lambda t: t.duration_minutes)
        pending.sort(key=lambda t: PRIORITY_ORDER[t.priority])
        self.ordered_tasks = pending
        self.reasoning = (
            "Tasks are ordered by priority (high first, then medium, then low). "
            "Within the same priority level, shorter tasks come first to get quick wins done early."
        )

    def sort_by_duration(self) -> None:
        """Re-order the task list from shortest to longest duration."""
        self.ordered_tasks.sort(key=lambda t: t.duration_minutes)

    def sort_by_priority(self) -> None:
        """Re-order the task list from highest to lowest priority."""
        PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
        self.ordered_tasks.sort(key=lambda t: PRIORITY_ORDER[t.priority])

    def get_total_duration(self) -> int:
        """Return the sum of duration_minutes across all ordered tasks."""
        return sum(t.duration_minutes for t in self.ordered_tasks)

    def get_summary(self) -> str:
        """Return a formatted multi-line string summarising the schedule's tasks and total duration."""
        lines = [
            f"Schedule for: {self.pet.name}",
            f"  Total tasks: {len(self.ordered_tasks)}",
            f"  Total duration: {self.get_total_duration()} min",
            "  Tasks:",
        ]
        for task in self.ordered_tasks:
            lines.append(f"    - {task.title} [{task.priority}] — {task.duration_minutes} min")
        return "\n".join(lines)

    def explain_reasoning(self) -> str:
        """Return the human-readable explanation of why tasks were ordered as they were."""
        return self.reasoning
