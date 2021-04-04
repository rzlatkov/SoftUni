class ExercisePlan:
    next_id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.next_id
        ExercisePlan.next_id += 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.next_id
