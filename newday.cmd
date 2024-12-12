:: Create new day files for Advent of Code, 2-digit day number as argument
:: test if file(s) exist before creating them
if exist Day%1a.txt goto fileexists
copy DayXX.txt Day%1a.txt
if exist Day%1b.txt goto fileexists
copy DayXX.txt Day%1atest.txt
if exist Day%1a.py goto fileexists
copy DayXX.py  Day%1a.py
:fileexists
dir Day%1*.*
