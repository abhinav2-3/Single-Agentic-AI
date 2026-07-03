skills = ["Python", "Node", "React", "Python", "Neon"]
numbers = [1, 2, 3, 4, 5, 6]

for skill in skills:
    print(skill)

print("----")

for i in range(10):
    print(i)

print("-----")

for i in range(5):
    print(i * 5)

print("---------")

count = 0
while count <= 3:
    print(f"Count : {count}")
    count += 1

print("-------")

for index, skill in enumerate(skills):
    print(f"{index} : {skill}")


print("-------")

user = {"name": "Abhinav", "work": "Software Engineer", "age": "22"}

for key, value in user.items():
    print(f"{key} : {value}")

upper = [s.upper() for s in skills]
print("Upper ", upper)

even = [n for n in numbers if n % 2 == 0]
print("Even : ", even)
