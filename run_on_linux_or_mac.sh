#!/bin/bash

# Adds drivers to PATH
export PATH=$PATH:$(pwd)/drivers/linux/chrome/chromedriver:$(pwd)/drivers/linux/firefox/geckodriver:$(pwd)/drivers/linux/edge/msedgedriver

# creates virtual env
python3 -m venv venv

# Activate virtual env
source venv/bin/activate

# Install dependencies on virtual env
pip install -r requirements.txt

# Run tests
python3 -m pytest --html=report.html

# Prevent terminal from close 
echo "Press any key to close ..."
read -n 1 -s
