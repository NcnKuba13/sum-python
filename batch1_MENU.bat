@echo off
cd %~dp0
:poczatek
cls
echo. "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
echo. "               CENTRALA                "
echo. "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
echo.
echo. "1 > Zarys idei programu"
echo. "2 > Uruchomienie programu"
echo. "3 > Generowanie raportu"
echo. "4 > Kasowanie raportow"
echo. "5 > WYJSCIE"
echo.

set /p wariant="Wybierz operacje do wykonania [1|2|3|4|5]: "
if %wariant%==1 goto wariant1
if %wariant%==2 goto wariant2
if %wariant%==3 goto wariant3
if %wariant%==4 goto wariant4
if %wariant%==5 exit
goto poczatek

:wariant1
cls
echo. "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
echo.
echo. "CZYM JEST CIAG JEDYNKOWY?"
echo. "Ciag liczb calkowitych, ktorego:"
echo. "- dwa dowolne sasiednie wyrazy roznia sie od siebie dokladnie o jeden;"
echo. "- pierwszy wyraz wynosi zero."
echo.
echo. "JAK DZIALA PROGRAM?"
echo. "Program pobiera od uzytkownika dwie liczby:"
echo. "- n - dlugosc ciagu"
echo. "- S - suma wszystkich elementow ciagu"
echo. "Nastepnie program generuje przykladowy ciag jedynkowy o zadanych parametrach"
echo. "albo stwierdza, iz ciag jedynkowy o takich wlasnosciach nie istnieje."
echo.
echo. "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
pause
goto poczatek

:wariant2
cls
call py1_SUM.py
pause
goto poczatek

:wariant3
cls
call py2_HTML.py
start %windir%\explorer.exe raporty
goto poczatek

:wariant4
cls
del /q raporty\*
goto poczatek