@echo off

rem This script is taken from the https://pypi.org/project/virtualenvwrapper-win/ project
rem and modified to the cos CLI needs



if not defined COS_VENV_DIR (
    set "COS_VENV_DIR=%USERPROFILE%\cos_venvs"
)

if not defined VIRTUALENVWRAPPER_PROJECT_FILENAME (
    set VIRTUALENVWRAPPER_PROJECT_FILENAME=.project
)

if [%1]==[] goto LIST
goto WORKON

:LIST
echo.
echo Pass a name to activate one of the following virtualenvs:
echo ==============================================================================
dir /b /ad "%COS_VENV_DIR%"
goto END

:WORKON

set "VENV=%~1"
shift

:LOOP
if not "%1"=="" (
    if "%1"=="-c" (
        SET CHANGEDIR=1
        shift
    )
    shift
    goto :LOOP
)

rem checks whethe a venv already exists or not
if defined VIRTUAL_ENV (
    call "%VIRTUAL_ENV%\Scripts\deactivate.bat"
)

rem checks whether the workon home exists or not
pushd "%COS_VENV_DIR%" 2>NUL && popd
if errorlevel 1 (
    mkdir "%COS_VENV_DIR%"
)

rem if the venv does not exist in COS_VENV_DIR then as the user to create one
pushd "%COS_VENV_DIR%\%VENV%" 2>NUL && popd
if errorlevel 1 (
    echo.
    echo.    virtualenv "%VENV%" does not exist.
    echo.    Create it with "cos venv new %1"
    goto END
)

if not exist "%COS_VENV_DIR%\%VENV%\Scripts\activate.bat" (
    echo.
    echo.    %COS_VENV_DIR%\%VENV%
    echo.    doesn't contain a virtualenv ^(yet^).
    echo.    Create it with "cos venv new %VENV%"
    goto END
)

call "%COS_VENV_DIR%\%VENV%\Scripts\activate.bat"
if defined WORKON_OLDTITLE (
    title %1 ^(VirtualEnv^)
)

if exist "%COS_VENV_DIR%\%VENV%\%VIRTUALENVWRAPPER_PROJECT_FILENAME%" (
    call cdproject.bat
) else (
    if "%CHANGEDIR%"=="1" (
        cd /d "%COS_VENV_DIR%\%VENV%"
    )
)

:END
