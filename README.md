# LING521
Portland State University LING 521: Applied English grammar code repo for winter term 2019.

#### Running the Scripts:
Click on the Jupyter Notebooks below to load a demo of the script.  

* [Dependency Test](https://github.com/steve3p0/LING521/blob/master/textmsg_analysis/test_dependencies.ipynb)<br>
<sub><sup>- Run above Jupyter Notebook in [mybinder](https://hub-binder.mybinder.ovh/user/steve3p0-ling521-fr3ttoni/notebooks/textmsg_analysis/test_dependencies.ipynb) if it doesn't load. </sup></sub><br>
* [Assignment 1: Text Messages (2007) Analysis Script](https://github.com/steve3p0/LING521/blob/master/textmsg_analysis/text_analysis.ipynb)<br>
<sub><sup>- Run above Jupyter Notebook in [mybinder](https://hub-binder.mybinder.ovh/user/steve3p0-ling521-fr3ttoni/notebooks/textmsg_analysis/text_analysis.ipynb) if it doesn't load. </sup></sub><br>
* Assignment 2:
* Assignment 3:

<B>NOTE:</B> There are some issues with loading Jupyter Notebooks.  Possible solutions and/or workarounds are being investigated.</sup></sub><br>
- If your Jupyter Notebook is having issues, you can copy and paste the URL from Github to:
    - [NB Viewer](http://nbviewer.jupyter.org/)
    - [My Binder](https://mybinder.org/) <sub><sup>Update 11/7/2019: * This seems to work best</sup></sub>
- [Working with Jupyter Notebook files on GitHub](https://help.github.com/en/github/managing-files-in-a-repository/working-with-jupyter-notebook-files-on-github)

#### Software Dependencies:<br>
To run the python scripts in this repository, <I>on your local machine</I>, the following dependencies must be met:

NOTE: These instructions are for Windows 10 (Instructor's OS)

- Install python 3.7 (https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64-webinstall.exe()
- update Environment variables:
    - Follow these instructions: 
        - https://phoenixnap.com/kb/how-to-install-python-3-windows
        - C:\Users\USER\AppData\Local\Programs\Python\Python37    
- Install Graphing/Plotting Package (matplotlib)
    - on windows 10, requires Microsoft Visual C++ 14.0 Build Tools:
    https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16
    https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019
    - pip3 install -U matplotlib
- Install Python Natural Langauge Toolkit
    - pip3 install nltk
- Install Jypyter Notebook support
    - pip3 install jupyterlab
- Install DataTable Support for Jupyter Notebooks
    - pip3 install jupyter-datatables
- Enable DataTable Support for Jupyter Notebooks
    - jupyter nbextension install --sys-prefix --py jupyter_require
    - jupyter nbextension enable jupyter-require/extension
    - ??jupyter nbextension enable jupyter_require --py --sys-prefix
    
#### Optional Installs:
- Register and Install Github Desktop (Optional)
    - Register on GitHub
    - Install GitHub Desktop
        - https://help.github.com/en/desktop/getting-started-with-github-desktop/installing-github-desktop
- Install PyCharm IDE (Optional)
    - Download and install: 
    https://www.jetbrains.com/pycharm/download/#section=windows
    
    
    