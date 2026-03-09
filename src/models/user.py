import re

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_info(self):
        return "Пользователь: " + self.name + ", Email: " + self.email


    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_email: str) -> None:
        pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        if re.fullmatch(pattern, new_email):
            self.email = new_email
            return
        raise ValueError('Неверный формат email')