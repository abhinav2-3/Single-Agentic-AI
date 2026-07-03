def greet(name:str):
    return f"Hello {name}"


print(greet("Abhinav"))


def greet2(name:str, role:str="Software Developer"):
    return f"Hii, I'm {name} & I'm a {role}"


print(greet2("Abhinav"))
print(greet2("Abhinav", "Backend Engineer"))


def total(*numbers:int):
    return sum(numbers)


print(total(1, 2, 3, 4, 5, 6))


def user_info(**details):
    for key, value in details.items():
        print(f"{key} : {value}")


user_info(name="Abhinav", age=25, role="dev")

multiply = lambda a:int, b:int ->int: a * b
print(multiply(5, 10))
