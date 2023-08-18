import uuid


class IdGenerator:

    @staticmethod
    def generate_uuid():
        return uuid.uuid4()
