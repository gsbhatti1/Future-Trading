@echo off
cd /d C:\Users\gsbha\qwen-dev\Future-Trading
git add .
git commit -m "auto push %date% %time%"
git push
echo.
echo Pushed to GitHub!
pause