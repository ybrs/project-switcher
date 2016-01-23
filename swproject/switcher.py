import os
import sys
import yaml
import subprocess


def run_chrome(url):
    myscript = """
        osascript <<-EOF
            tell application "Google Chrome"
                activate
                open location "{url}"
                delay 1
                activate
            end tell
        EOF
    """.format(url=url)
    print myscript
    proc = subprocess.Popen(myscript,
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    (output, error) = proc.communicate()
    print output

def run_iterm(lines):
    ll = [ln for ln in lines if ln.strip()]
    myscript = """
        osascript <<-EOF
        tell application "iTerm"
            activate
            make new terminal
            tell the current terminal
                activate current session
                launch session "Default Session"
                tell the last session
                    write text "{lines}"
                end tell
            end tell
        end tell
        EOF
    """.format(lines=' && '.join(ll))
    print myscript
    proc = subprocess.Popen(myscript,
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    (output, error) = proc.communicate()
    print output

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
                run_iterm(lines)
            if k == 'chrome':
                run_chrome(v['open'])


if __name__ == '__main__':
    fname = sys.argv[1]
    print "opening fname", fname
    run(fname, sys.argv[2])