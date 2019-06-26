Jupyter Notebook for Python3
============================
> Jupyter Notebook offers a command shell for interactive computing as a web application. The tool can be used with several languages, including Python. It is often used for working with data, statistical modeling, and machine learning.


Step 1 -- Installing the Jupyter Notebook
-----------------------------------------
* Prerequisite: Python
    - install virtualenv and virtualenvwrapper 
    - $ sudo -H python3 -m pip install virtualenv virtualenvwrapper 
    - $ sudo rm -rf ~/.cache/pip 
    - update our ~/.profile file(similar to .bashrc or )
    - Using a terminal text editor such as vi/ vim or nano, add the following lines to your ~/.profile 
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
    - $ source ~/.zshrc 
* Installing Jupyter with pip 
    - $ source JupyterNotebook  # Activate the Python3 programming environment
    - $ python3 -m pip install --upgrade pip  # ensure that pip is upgraded to the most recent version 
    - $ python3 -m pip install jupyter # Install Jupyter Notebook 
    - $ workon JupyterNotebook  # source verify 
    - Congratulations, you have installed Jupyter Notebook! To run the notebook, run the following command at the Terminal(Mac/Linux) or Command Prompt(Windows):

Step 2 -- Running Jupyter Notebook
----------------------------------
> The Jupyter notebook web application is based on a server-client structure. The notebook server uses a two-process kernel architecture based on ZeroMQ, as well as Tornado for serving HTTP requests.
```
    - Generate Notebook Password -- sha1 password 
    $ python 
    >>> from notebook.auth import passwd 
    >>> passwd() 
    
    - Generate Jupyter Notebook Config file
    $ jupyter notebook --generate-config 
    $ vim ~/.jupyter/jupyter_notebook_config.py 
        c.NotebookApp.ip = '*'
        c.NotebookApp.port = 80 
        c.NotebookApp.open_browser = False 
        c.NotebookApp.password = sha1 
        c.NotebookApp.allow_root = True
        c.NotebookApp.notebook_dir = '~/JupyterNotebook'

    - Create a runner file to make it easier to pull in the right environment variables,. before launching the notebook.
        $ sudo vim ~/bin/launch_jupter.sh 
            #!/bin/bash 

            source /home/chyi/.virtualenvs/JupyterNotebook/bin/activate
            /home/chyi/.virtualenvs/JupyterNotebook/bin/jupyter notebook 

        $ sudo chmod 750 ~/bin/launch_jupyter.sh

    - Create jupyter-notebook.service 
        [Unit]
        Description=Jupyter Notebook Server 

        [Service]
        Type=simple 
        Restart=on-failure 
        ExecStart=/bin/bash -c 'exec ~/bin/launch_jupyter.sh &> /home/chyi/logs/jupyter/jupyter_notebook.log'
        
        [Install]
        WantedBy=multi-user.target 

    $ sudo chmod a+rw jupyter-notebook.service 
    $ sudo systemctl daemon-reload 
    $ sudo systemctl enable jupyter-notebook 
    $ sudo systemctl restart jupyter-notebook 
    $ sudo systemctl status jupyter-notebook 

    - By default, a notebook server runs locally at 127.0.0.1:8888 and is accessible only from localhost.You may access the notebook server from the browser using http://127.0.0.1:8888
    - $ jupyter noetbook --generate-config # This command will create the jupyter folder if necessary,and create notebook configuration file.jupyter_notebook_config.py.
    - $ jupyter notebook password # This can be used to reset a lost password; or if you belive your credentials have been leaked and desire to change your password.Changing your password will invalidate all logged-in sessions after a server restart.
``` 
