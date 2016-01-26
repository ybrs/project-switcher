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
            set nterminal to (make new terminal)
            tell the current terminal
                activate current session
                launch session "Default Session"
                tell the last session
                    write text "{lines}"
                end tell
            end tell
        end tell
        return nterminal
        EOF
    """.format(lines=' && '.join(ll))
    print myscript
    proc = subprocess.Popen(myscript,
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    (output, error) = proc.communicate()
    print output
    print error

def run_itermocil(v):
    print "-------"
    s = yaml.dump(v)
    f = open('/tmp/project-switcher-itermocil.yml', 'w')
    f.write(s)
    f.close()
    print "-------"
    myscript = """
        /Users/aybarsbadur/projects/project-switcher/env/bin/itermocil --layout /tmp/project-switcher-itermocil.yml
    """

    proc = subprocess.Popen(myscript,
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    (output, error) = proc.communicate()


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
            if k == 'itermocil':
                run_itermocil(v)

def main():
    try:
        fname = sys.argv[1]
        run(fname, sys.argv[2])
    except:
        print """
        usage:
            swproject config.yml project_name
        """

if __name__ == '__main__':
    main()