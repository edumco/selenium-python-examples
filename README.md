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

Before you start, you NEED to know 3 informations:

__Your operational system__: It's the software that you use to run your applications! This software works on:

    1. Windows = The most common, almost everybody uses
    2. MacOs = Comes only with computers from Apple
    3. Linux = A free and secure alternative

__Your browser__: That little window you use to view websites. This software works with:

    1. Google Chrome (and Chromium on linux)
    2. Microsof Edge (that is very similar to Chrome)
    2. Firefox (a diferent engine)

__If you have Python on your machine__: It can be download for free but you gonna need administrative permitions to install.

### If you think you're ready lets start

#### 1. Install Python on your computer

- [Download from official site](https://www.python.org/downloads/release/python-3123/)
- [Install from AppStore on MacOS](https://apps.apple.com/br/app/python-3/id1262850648)
- [Install from Windows Store](https://apps.microsoft.com/detail/9ncvdn91xzqp?hl=en-us&gl=US) or [Chocolatey](https://community.chocolatey.org/packages/python312)
- [Ubuntu Snaps](https://snapcraft.io/python3-alt) or [using the package manager from you linux distro](https://wiki.python.org/moin/BeginnersGuide/Download)

#### 2. Install or update your browser

- Chrome: [Install](https://www.google.com/chrome/) or [update](https://support.google.com/chrome/answer/95414?hl=EN&co=GENIE.Platform%3DDesktop)
- Edge: [Install](https://www.microsoft.com/en-us/edge/download?form=MA13FJ) or [update](https://support.microsoft.com/en-us/topic/microsoft-edge-update-settings-af8aaca2-1b69-4870-94fe-18822dbb7ef1)
- Firefox: - [Install](https://www.mozilla.org/en-US/firefox/new/) or [update](https://support.mozilla.org/en-US/kb/update-firefox-latest-release)

#### 3. Download and uncompress this project on your machine

__[Arquivo ZIP 📂](https://github.com/edumco/selenium-python-examples/archive/refs/heads/main.zip)__

After uncompress navigate to the main folder and click on one of the runners: `run_on_windows.bat` or `run_on_linux_or_mac.sh`

If it does not open try calling [via terminal](https://www.lifewire.com/open-command-prompt-in-folder-8681085) or [change the file permitions](https://support.apple.com/guide/mac-help/change-permissions-for-files-folders-or-disks-mchlp1203/mac)

## Project overview

Heres a simple overview from this source code:

selenium-python-examples/
├── config/
├── drivers/
├── pages/
├── tests/
└ ...

The most important file is the config.py
├── config/
│   ├── config.py

It keeps all the configurations together so you dont need to search the entire project when something changes

On the `drivers` folder are located the files Selenium necessary to comunicate with the browser

Another very important file is the conftest.py
├── tests/
│   ├── conftest.py

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
