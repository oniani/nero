"""
Testing module

David Oniani
Licensed under GNU General Public License v3.0
"""


import pytest

from nero.engine import Core
from nero.interactions import Information, InteractiveHelp, Function


def test_Core():
    """Testing 'Core' class"""
    # Creating the 'Core' class instance
    test_tasks = Core('test_tasks.csv')

    # Testing 'get_titles()' method
    assert test_tasks.get_titles() ==\
        ["Title",
         "Zeroth task", "First task", "Second task",
         "Third task", "Fourth task", "Fifth task",
         "Sixth task", "Seventh task", "Eight task",
         "Ninth task", "Tenth task", "Eleventh task",
         "Twelfth task"]

    # Testing 'get_deadlines()' method
    assert test_tasks.get_deadlines() ==\
        ["Deadline",
         "00/00/2018", "01/01/2018", "02/02/2018",
         "03/03/2018", "04/04/2018", "05/05/2018",
         "06/06/2018", "07/07/2018", "08/08/2018",
         "09/09/2018", "10/10/2018", "11/11/2018",
         "12/12/2018"]

    # Testing '__len__' method
    assert len(test_tasks) == 14

    # Testing '__getitem__' method
    assert test_tasks[10] == 'Ninth task'

    # Testing '__iter__ method
    count = 0
    for _ in test_tasks:
        count += 1
    assert count == 14

    # Testing '__str__' method
    assert str(test_tasks[1]) == "Zeroth task"

    # Testing 'get_titles()' method
    assert test_tasks.get_titles() ==\
        ["Title",
         "Zeroth task", "First task", "Second task",
         "Third task", "Fourth task", "Fifth task",
         "Sixth task", "Seventh task", "Eight task",
         "Ninth task", "Tenth task", "Eleventh task",
         "Twelfth task"]

    # Testing 'get_deadlines()' method
    assert test_tasks.get_deadlines() ==\
        ["Deadline",
         "00/00/2018", "01/01/2018", "02/02/2018",
         "03/03/2018", "04/04/2018", "05/05/2018",
         "06/06/2018", "07/07/2018", "08/08/2018",
         "09/09/2018", "10/10/2018", "11/11/2018",
         "12/12/2018"]

    # Testing 'add_task' method
    test_tasks.add_task("Thirteenth Task", "13/13/2018")
    assert test_tasks._titles ==\
        test_tasks.get_titles() ==\
        ["Title",
         "Zeroth task", "First task", "Second task",
         "Third task", "Fourth task", "Fifth task",
         "Sixth task", "Seventh task", "Eight task",
         "Ninth task", "Tenth task", "Eleventh task",
         "Twelfth task", "Thirteenth Task"]

    assert test_tasks._deadlines ==\
        test_tasks.get_deadlines() ==\
        ["Deadline",
         "00/00/2018", "01/01/2018", "02/02/2018",
         "03/03/2018", "04/04/2018", "05/05/2018",
         "06/06/2018", "07/07/2018", "08/08/2018",
         "09/09/2018", "10/10/2018", "11/11/2018",
         "12/12/2018", "13/13/2018"]

    # Testing 'remove_task' method
    test_tasks.remove_task(13)
    assert test_tasks._titles ==\
        test_tasks.get_titles() ==\
        ["Title",
         "Zeroth task", "First task", "Second task",
         "Third task", "Fourth task", "Fifth task",
         "Sixth task", "Seventh task", "Eight task",
         "Ninth task", "Tenth task", "Eleventh task",
         "Twelfth task"]

    assert test_tasks._deadlines ==\
        test_tasks.get_deadlines() ==\
        ["Deadline",
         "00/00/2018", "01/01/2018", "02/02/2018",
         "03/03/2018", "04/04/2018", "05/05/2018",
         "06/06/2018", "07/07/2018", "08/08/2018",
         "09/09/2018", "10/10/2018", "11/11/2018",
         "12/12/2018"]


def test_Information(capfd):
    """Testing 'Information' class"""
    # Creating 'Information' class instance
    test_Information = Information()

    # Testing 'info' method
    test_Information.info()
    out, err = capfd.readouterr()
    assert out == "Nero by David Oniani\n"\
                  "Licensed under GNU General Public License v3.0\n"\
                  "Copyright (c) 2018 David Oniani\n"\
                  "Type 'help' or 'license' for more information\n"
