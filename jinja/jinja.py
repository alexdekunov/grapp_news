from jinja2 import Template

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# per = Person("Федор", 33)


per = {
    "name": "Федор",
    "age": 28
}

tm = Template("Мне {{ p['age'] }} лет и зовут меня {{ p['name'] }}")
# tm = Template("Мне {{ p.age*2 }} лет и зовут меня {{ p.name.upper() }}")
msg = tm.render(p=per)

print(msg)
