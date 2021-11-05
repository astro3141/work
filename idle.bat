@echo off
rem Start IDLE using the appropriate Python interpreter
set CURRDIR=%~dp0
start "IDLE" "C:\Users\admin\AppData\Local\Programs\Python\Python38\Lib\idlelib\..\..\pythonw.exe" "C:\Users\admin\AppData\Local\Programs\Python\Python38\Lib\idlelib\idle.pyw" %1 %2 %3 %4 %5 %6 %7 %8 %9
