:: Add drivers to path
set PATH=%PATH%;%cd%\drivers\windows\chrome\chromedriver.exe;%cd%\drivers\windows\firefox\geckodriver.exe;%cd%\drivers\windows\edge\msedgedriver.exe

:: Creates virtual env to isolate from your python instalation
python -m venv venv

:: Activate the env
call venv\Scripts\activate.bat

:: Installs dependencies on the virtual env only
pip install -r requirements.txt

:: Runs the tests
python3 pytest --html=report.html

:: Keep the terminal open
pause