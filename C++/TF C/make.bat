@echo off

echo EXPORTS > tensorflow.def
nm tensorflow.dll | grep ' T _' | sed 's/.* T _//' >> tensorflow.def
dlltool --def tensorflow.def --dllname tensorflow.dll --output-lib tensorflow.a



g++ bot.cpp -c -o bot.o
g++ bot.o tensorflow.dll -o bot.exe -static
pause
