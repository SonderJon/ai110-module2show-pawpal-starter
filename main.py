from pawpal_system import Task, Pet, Owner, Schedule

print("== PawPal Test ==")

owner = Owner(name="Jordan")
owner.add_pet(
    Pet(name = "Nyan", species = "cat", age_years = 3)
)
owner.add_pet(
    Pet(name = "Rex", species = "dog", age_years = 5)
)

print(f"Created owner {owner.name} with pets: {', '.join(p.name for p in owner.pets)}")

owner.get_pet("Nyan").add_task(
    Task(
        title="Feed Nyan",
        description="Give Nyan her breakfast",
        priority="high",
        duration_minutes=10)
)
owner.get_pet("Nyan").add_task(
    Task(
        title="Play with Nyan",
        description="Spend some time playing with Nyan",
        priority="medium",
        duration_minutes=30)
)
owner.get_pet("Rex").add_task(
    Task(
        title="Walk Rex",
        description="Take Rex for a walk around the block",
        priority="high",
        duration_minutes=20)
)

print ("Added tasks to pets")

print("---")
print("Today's Schedules")
sched_1 = Schedule(owner.get_pet("Nyan"))
sched_1.generate()
print(sched_1.get_summary())

sched_2 = Schedule(owner.get_pet("Rex"))
sched_2.generate()
print(sched_2.get_summary())