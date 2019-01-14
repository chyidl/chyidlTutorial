Jupyter Notebook
================

Installing the Jupyter Notebook
------------------------------
    - Prerequisite: Python
    - Installing Jupyter with pip 
        $ python3 -m pip install --upgrade pip 
        $ python3 -m pip install jupyter 
    - Congratulations, you have installed Jupyter Notebook! To run the notebook, run the following command at the Terminal(Mac/Linux) or Command Prompt(Windows):
        $ jupyter notebook 

Running a notebook server
-------------------------

The Jupyter notebook web application is based on a server-client structure. The notebook server uses a two-process kernel architecture based on ZeroMQ, as well as Tornado for serving HTTP requests.

    - By default, a notebook server runs locally at 127.0.0.1:8888 and is accessible only from localhost.You may access the notebook server from the browser using http://127.0.0.1:8888
    - $ jupyter noetbook --generate-config # This command will create the jupyter folder if necessary,and create notebook configuration file.jupyter_notebook_config.py.
    - $ jupyter notebook password # This can be used to reset a lost password; or if you belive your credentials have been leaked and desire to change your password.Changing your password will invalidate all logged-in sessions after a server restart.
    