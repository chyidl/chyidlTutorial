:: This is My Last Script 
:: It is to be cherished
@echo off 
:: 切换当前编码方式为 UTF-8, 处理命令行窗口标题乱码问题
chcp 65001
title 批量压缩目录下文件
:: 切换回默认 GBK 编码, 处理命令行输出乱码问题
chcp 936 
echo ---------- START -------------

:: 实现一：遍历当前目录下 (不含子目录) 的文件, 压缩成当前文件同名的 7z 格式文件, 最后压缩文件存放在当前目录下新建的 7z 文件夹 
:: 7z.exe a -t7z ".\7z\%%~nF.7z" 
:: 7z.exe a -tzip ".\7z\%%~nF.zip"
:: for %%F in (*.pdf) do (echo "%%~nF" && "C:\Program Files\7-Zip\7z.exe" a -t7z ".\7z\%%~nF.7z" "%%F" )

:: 实现二：遍历当前目录下 (不含子目录) 的文件夹进行压缩，压缩成与当前文件夹同名的 7z 格式文件，最后压缩文件存放在目录下新建的 7z 文件夹
:: for /d %%F in (*) do (echo "%%~nF" && "C:\Program Files\7-Zip\7z.exe" a -t7z ".\7z\%%~nF.7z" "%%F" )

:: 实现三: 遍历当前目录下 (含子目录) 的pdf文件进行压缩， 压缩成与当前文件同名的 7z 格式文件, 最后压缩文件存放在目录下新建的 7z 文件夹 
:: for /r %%F in (*.pdf) do (echo "%%~nF" && "C:\Program Files\7-Zip\7z.exe" a -t7z ".\7z\%%~nF.7z" "%%F" )

:: 实现四: 遍历当前目录下 (含子目录) 的pdf文件进行压缩, 压缩成与当前文件同名的 7z 格式文件, 最后压缩文件存放在与当前文件同目录下  
:: for /r %%F in (*.pdf) do (echo "%%~nF" && "C:\Program Files\7-Zip\7z.exe" a -t7z "%%~dpnF.7z" "%%F" )

:: 实现五: 遍历当前目录下 (含子目录) 的pdf文件进行压缩, 打包到PDF.7z 压缩包内，最后压缩文件存放在当前目录下 
:: for /r %%F in (*.pdf) do (echo "%%~nF" && 7z a -t7z "PDF.7z" "%%F" )

echo ----------  END  -------------
pause