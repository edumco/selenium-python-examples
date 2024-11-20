# Selenium Python Examples

Some examples of web testing automation using Selenium with Python.

## Features

This repo contains a complete structure to create a test suit for functional test cases for a web page.

It contains examples of:

- Finding and interact with elements using its id, name, CSS selector, tag name, XPATH ...
- How to get the contents of an element and parse it into lists
- Test parametrization (to reuse tests with different inputs)
- How to use test fixtures to simplefy configuration
- Automatic configuration based on suytem information

## Before you start

We gonna need some software pre installed:

1. [Python 3.12 - Follow the instructions for your system](https://www.python.org/downloads/)

2. Pip
2.1 [Pip on Linux](https://www.tecmint.com/install-pip-in-linux/)
2.2 [Pip on Mac](https://phoenixnap.com/kb/install-pip-mac)
2.3 [Pip on Windows](https://phoenixnap.com/kb/install-pip-windows)

3. Virtual env
3.1 [Venv on Linux](https://virtualenv.pypa.io/en/latest/installation.html)
3.2 [Venv on Mac](https://www.deadbear.io/how-to-install-virtualenv-on-mac-os/)
3.3 [Venv on Windows](https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59)

4. One of the following browsers
4.1 Firefox (recommended)
4.2 Microsof Edge
4.3 ~~Google Chrome~~ (Not stable yet)

### If you think you're ready lets start

#### 1. Install Python on your computer

- [Download from official site](https://www.python.org/downloads/release/python-3123/)
- [Install from AppStore on MacOS](https://apps.apple.com/br/app/python-3/id1262850648)
- [Install from Windows Store](https://apps.microsoft.com/detail/9ncvdn91xzqp?hl=en-us&gl=US) or [Chocolatey](https://community.chocolatey.org/packages/python312)
- [Ubuntu Snaps](https://snapcraft.io/python3-alt) or [using the package manager from you linux distro](https://wiki.python.org/moin/BeginnersGuide/Download)

#### 2. Install or update your browser

- Edge: [Install](https://www.microsoft.com/en-us/edge/download?form=MA13FJ) or [update](https://support.microsoft.com/en-us/topic/microsoft-edge-update-settings-af8aaca2-1b69-4870-94fe-18822dbb7ef1)
- Firefox: [Install](https://www.mozilla.org/en-US/firefox/new/) or [update](https://support.mozilla.org/en-US/kb/update-firefox-latest-release)
- Chrome: [Install](https://www.google.com/chrome/) or [update](https://support.google.com/chrome/answer/95414?hl=EN&co=GENIE.Platform%3DDesktop)

#### 3. Download and uncompress this project on your machine

1. [Download ZIP file 📂](https://github.com/edumco/selenium-python-examples/archive/refs/heads/main.zip) or clone the project

1. Navigate to the main folder and [open your terminal or command prompt](https://www.lifewire.com/open-command-prompt-in-folder-8681085)

1. [Change the file permitions](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac) so you can execute one of the following files:

    - `run_on_linux_or_mac.sh`
    - `run_on_windows.bat`

### What's going to happen?

These files will:

1. Create a Python Virtual Enviroment that isolates this project from the rest of your computer;
1. Activate this new enviroment
1. Install the Python Dependencies inside this enviroment using the pip installer
1. Start the test execution
1. Pause the terminal after execution so you can see the results

## Project overview

Heres a simple overview from this source code:

```
selenium-python-examples/
├── config/
├── drivers/
├── pages/
├── tests/
└ ...
```

The most important file is the config.py

```
├── config/
│   ├── config.py
```

It keeps all the configurations together so you dont need to search the entire project when something changes

On the `drivers` folder are located the files Selenium necessary to comunicate with the browser

Another very important file is the conftest.py

```
├── tests/
│   ├── conftest.py
```

It provides the fixtures so the test resources can be easily initialized and released

On the `pages` folder you get the page object pattern implemented by representing each website with a different class

And finally on the `tests` folder you find the actual tests that glue together all the parts:

1. Use the configurations from config.py
2. Receive resources from the fixtures
3. Use the methods form the page objects

Hope you enjoy!

## License

This project is licensed [Creative Commons Zero v1.0 Universal](LICENSE) so you can use it anyway you want.

You are free tho change the license on your own project to any license you want.

Visit <https://choosealicense.com/> and learn how to choose the right license to your project.
