
class Note:
    def __init__(self, id, pet_name, commands, pet_type, pet_class, timestamp):
        self.id = id
        self.pet_name = pet_name
        self.commands = commands
        self.pet_type = pet_type
        self.pet_class = pet_class
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "pet_name": self.pet_name,
            "pet_class": self.pet_class,
            "commands": self.commands,
            "pet_type": self.pet_type,
            "timestamp": self.timestamp
        }
