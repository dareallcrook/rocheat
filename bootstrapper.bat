@echo off
:: Create the folder rocheat if it doesn't exist
if not exist "rocheat" (
    mkdir rocheat
)

:: Ask for input
set /p userInput=Enter the path to save: 

:: Save input to path.txt inside the rocheat folder
echo %userInput% > rocheat\path.txt

:: Download the file main.py to the rocheat folder
echo Downloading main.py...
powershell -Command "Invoke-WebRequest -Uri https://github.com/dareallcrook/rocheat/releases/download/rocheat/main.py -OutFile rocheat\main.py"

:: Check if the download was successful
if exist "rocheat\main.py" (
    echo Download successful! File saved to rocheat\main.py
) else (
    echo Failed to download main.py. Please check your internet connection or the URL.
)

:: Delete this batch script after execution
echo Deleting the batch script...
del "%~f0"

:: Done
pause
