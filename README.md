project-switcher
==============================

projeden projeye gecerken, yada makineyi kapatip actigimizda, logout oldugumuzda.
- iterm ac
- python manage.py server calistir
- baska bir iterm penceresi ac
- celery worker calistir
- baska bir iterm penceresi ac
- redis serveri calistir
- browserda yeni bir tab ac, localhost:8080 e git
- pycharm da projeyi ac
vs. vs.

bir ton is yapiyoruz. projenin amaci basit bir yaml dosyasi verip bu isi otomatize etmek.

ornegin:
```
chroma:
    start:
        # this is for pycharm
        - iterm: |
            cd /Users/aybarsbadur/projects/hipo/chroma/api/
            pyc `pwd`
        - iterm: |
            cd /Users/aybarsbadur/projects/hipo/chroma/api/
            source ./env/bin/activate
            python app.py
        - iterm: |
            cd /Users/aybarsbadur/Downloads/neo4j-enterprise-2.3.1
            ./bin/neo4j console
        - iterm: |
            cd /Users/aybarsbadur/Downloads/elasticsearch-2.1.0
            ./bin/elasticsearch
        - chrome:
            open: http://localhost:8080/
        - itermocil:
            windows:
              - name: sample-two-panes
                root: /Users/aybarsbadur/projects/hipo/chroma/api
                layout: even-horizontal
                panes:
                  - source env/bin/activate && STORM_SETTINGS_MODULE="chroma.settings" PYTHONPATH=`pwd` kuyruk -m kuyruk_config worker
                  - echo "hello"

pswitcher:
    start:
        - iterm: |
            cd /Users/aybarsbadur/projects/project-switcher
            source env/bin/activate
        - iterm: |
            pyc `pwd`

```

installation
----------------------------
you can install it from pypi as expected.
```
virtualenv env
source env/bin/activate
pip install swproject
```
now create a yaml file like the above
```
swproject projects.yml projectname
```


pypi
---------------------------
https://pypi.python.org/pypi/swproject/0.1.1



demo
-----------------------------
[mp4](https://github.com/ybrs/project-switcher/blob/master/demo.mp4?raw=true)



hassle free project switching
-----------------------------
everytime you switch from a project to a project, we do a few things
like
- open an iterm window
- run python manage.
- open another iterm window
- run celery worker
- open another iterm window
- run redis server
etc. etc.

or

- vagrant up
- vagrant ssh
- run manage.py
- split iterm window
- vagrant ssh
- run celery worker


well project switcher tries to automate this process, using a simple yaml file.

usage
------------------------------
project-switcher sample.yml

installation
------------------------------
pip install project-switcher

notable projects
------------------------------
https://github.com/TomAnthony/itermocil opens different layouts in iterm. you can embed itermocil's yml in project-switcher.

https://github.com/remiprev/teamocil same thing with tmux.
