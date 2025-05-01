full_name = "Muhammad Rubaz Khan"
age = 25
height = 5.9
city = "Okara"
isProgrammer = True
skills = ["Python", "Dart", "Machine Learning", "C/C++"]
coordinates = (31.5657, 74.3142)

print(full_name)
print(age)
print(height)
print(city)
print(isProgrammer)
print(skills)
print(coordinates)

profile = {
    "name": full_name,
    "age": age,
    "height": height,
    "city": city,
    "isProgrammer": isProgrammer,
    "skills": skills,
    "coordinates": coordinates,
}
print(
    f"""
    Hello, my name is {full_name}. I am {age} years old. I live in {city} city. And my height is {height} feet.
    My top skill goal is: {skills[2]}
    My location is {coordinates}
    """
)
