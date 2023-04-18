# using import and dynamic HTML
# pip install Jinja2
from jinja2 import Template

name = "Abir"

skeleton_html = "<h1>Hello {{ name }}!</h1>"

t = Template(skeleton_html)

with open("a.html", "w") as f:
    f.write(t.render(name=name))


# assignment: input a number n and print pattern...
