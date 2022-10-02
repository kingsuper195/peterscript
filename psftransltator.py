#!/usr/bin/env python

from logging import error, log
import sys

def loadProgram(filename):
    f = open(filename)
    lines = f.readlines()
    return lines

if(len(sys.argv) > 1):
    lines = loadProgram(sys.argv[1])
else:
    lines = loadProgram("test.pst")

def do_write(line):
    output = line.removeprefix("(write-").removesuffix(")")
    output = output.replace('-'," ")
    print(output)
    #print("alert('{output}');".format(output=output))

def do_repeat(line):
    line = line.removeprefix("|Repeat-").removesuffix("|")
    parts = line.split("(")
    count = int(parts.pop(0))
    #print("for(var i=0; i<{count};i+++){{".format(count=count))
    for x in range(count):
        for part in parts:
            command = "(" + part
            do_command(command)
    #print("}")

def do_command(line):
    # Test if the line is a (write-message)
    if (line.startswith("(write-") and line.endswith(")")):
        do_write(line)
        return
    # |Repeat-<count>(<command>)|
    if(line.startswith("|Repeat-") and line.endswith("|")):
        do_repeat(line)
        return

    print("err: '{line}'".format(line=line))


for line in lines:
    line = line.strip()

    # Test if the line is a blank line
    if (line == ""):
        continue

    # Test if the line is a comment
    if (line.startswith("#")):
        continue

    # Do all the other commands
    do_command(line)
