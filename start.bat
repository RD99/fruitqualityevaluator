@ECHO OFF
ECHO setting variables
call D:\BE_Project\env\Scripts\activate
set FLASK_APP=app
set FLASK_ENV=development
set FLASK_DEBUG=1
ECHO variables set
::start cmd /k start_front.bat
flask run
PAUSE