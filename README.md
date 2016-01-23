project-switcher
------------------------------
hassle free project switching

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

installation
------------------------------
pip install project-switcher

notable projects
------------------------------
https://github.com/TomAnthony/itermocil opens different layouts in iterm. you can embed itermocil's yml in project-switcher.

https://github.com/remiprev/teamocil same thing with tmux.
