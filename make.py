#!/usr/bin/env python

import os

wheels = [i for i in os.listdir(".") if i.endswith(".whl")]
wheels.sort()

html_line = """<a href="%s">%s</a><br>\n"""

with open("index.html", "w") as outfile:
    outfile.write("<!DOCTYPE html>\n")
    outfile.write(r"<head><title>install dependencies</title></head>" + "\n")
    outfile.write("<body>\n")
    for w in wheels:
        outfile.write(html_line % (w, w))
    outfile.write(r"</body></html>")
