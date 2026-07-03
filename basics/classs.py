class User:
    def __init__(self, name: str, age: int, role: str = "SDE") -> None:
        self.name = name
        self.age = age
        self.role = role

    def greet(self) -> str:
        return f"Hii, I'm {self.name}, and I'm a {self.role}"

    def get_info(self) -> dict:
        return {"name": self.name, "age": self.age, "role": self.role}


class Admin(User):
    def __init__(self, name: str, age: int, permissions: list[str]) -> None:
        super().__init__(name, age, role="admin")
        self.permissions = permissions

    def get_info(self) -> dict:
        info = super().get_info()
        info["permissions"] = self.permissions
        return info


user = User("Abhinav", 22)
print(user.greet())
print(user.get_info())


admin = Admin("Abhishek", 22, ["read", "write", "delete"])
print(admin.greet())
print(admin.get_info())
