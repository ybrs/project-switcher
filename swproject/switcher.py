import os
import sys
import yaml

def run(fname, projectname):
    f = open(fname)
    d = yaml.load(f.read())
    print "-----"
    print d
    print "// "
    commands = d[projectname]['start']

    for cmd in commands:
        for k, v in cmd.items():
            if k == 'iterm':
                lines = v.split("\n")
                for ln in lines:
                    if ln:
                        print ">>>", ln


if __name__ == '__main__':
    fname = sys.argv[1]
    print "opening fname", fname
    run(fname, sys.argv[2])