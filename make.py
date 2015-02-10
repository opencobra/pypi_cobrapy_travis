#!/usr/bin/env python

import os

wheels = [i for i in os.listdir(".") if i.endswith(".whl")]
wheels.sort()

html_line = """<a href="%s">%s</a><br>\n"""

with open("index.html", "w") as outfile:
    for w in wheels:
        outfile.write(html_line % (w, w))

