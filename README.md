# Nero
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/oniani/Nero/blob/master/LICENSE/)
![python 3_+](https://img.shields.io/badge/python-3+-green.svg)

## WTF is this?
Terminal is the core app for the software development. In theory, one could do virtually anything using nothing other than a *UNIX terminal* or *Windows powershell*. We all have some tasks while programming or just doing things on computer. Most of people use apps like *Trello*, *Todoist*, etc. which help them manage tasks. Yet, these apps require opening browser or app store and installing them. Then one has to register and share his/her data with the company which created the app. Finally, none of them run in terminal and switching between windows is usually very discomforting which usually has a negative effect on productivity.
Not to mention the fact that all of them cost money.

**Nero** is a tiny app which runs in the terminal and helps organize tasks. It is copyright and cost free and is built using **Python** programming language.

## Nero philosophy
**Nero** is based on a simple philosophy: *where there is a task, there also is a deadline*.

## Installation and getting started
Installation is very simple and straightforward. There are two major ways to install **Nero** on your machine.

1. Through **Python** package installer 

    Run the command  `pip install nero` and you are good to go!

2. Through **GitHub** 

    Run the command `git clone https://github.com/oniani/nero` and once the repository is cloned, drop it in whatever directory you want. Then do `cd` in that directory and run `python3 setup.py` and **Nero** will start setting up its environment on your machine

Once **Nero** is set up, type `nero` in the **terminal** or **powershell** and the app will start running.

## Usage and functionality
**Nero** has a very simple interface which is just a list of tasks with corresponding deadlines.

This is the list of available functionalities:
- `help` - shows a manual for the commands
- `license` - shows the license for the app
- `ls` - list all tasks
- `ls --ttl` - list titles only
- `ls --ddl` - list deadlines only
- `add` - add a task
- `rm` - remove a task by its index
- `h` - show command history for the current session
- `clear` - clear the terminal window
- `q` - quit the app and save my edits

## How does it work?
**Nero** is also very simple in logic. Every task is stored in `.csv` file and the app either reads or writes to the file, depending on the command.

## License
[MIT](https://www.github.com/oniani/LICENSE)
