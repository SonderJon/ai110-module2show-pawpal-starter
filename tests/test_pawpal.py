import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Pet, Task


def test_mark_complete_sets_is_completed_true():
    task = Task(title="Feed", description="Morning feed", priority="high", duration_minutes=10)
    task.mark_complete()
    assert task.is_completed is True


def test_add_task_appends_to_task_list():
    pet = Pet(name="Mochi", species="cat", age_years=3)
    task = Task(title="Groom", description="Brush coat", priority="low", duration_minutes=15)
    pet.add_task(task)
    assert len(pet.task_list) == 1
