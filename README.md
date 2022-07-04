# BetterPyShell
BetterPyShell - The Python shell, but more customizable and enhanced.

(I only have the Linux pre-compiled binary, compile it yourself using Pyinstaller if you are on Windows / Mac or just use it directly from the .py file)

### What is BetterPyShell?

Do you know the python shell? The prompt that appears when you type "python" or "python3" in your terminal/cmd?
This is python shell, but enhanced. With customizable features, like custom error messages, welcome messages and a lot more. Plus formatting.

I got the idea from Oh-my-zsh, which is basically bash but customizable. So I tried making something like that with python.

There are binaries compiled with Pyinstaller. I didn't tested, but I think they work like a portable python. Not sure.

### How can I customize it?

You need to download 2 files (or clone the repository):
  pyshell.py
  config.txt

If you just wanna use it, just download the compiled binary and dont forget config.txt (The compiled binary still needs confi.txt and can be tweaked too!)
All the configs are in the config.txt file and I put some little comments and the formatting you can use at the bottom of the file for easier tweaking.

### How do I modify it? (How to modify the source code)

Clone the repo or download pyshell.py and config.txt, edit pyshell.py just like you want. Also dont forget to tweak config.txt, there are loads of customization settings there!

### How do I compile to a binary?

Use pyinstaller. Open your terminal, run pip install pyinstaller and then cd to the folder where the .py file is located.
Run "pyinstaller --onefile pyshell.py" where **pyshell** is the name of your py file. And don't forget that compiled binaries still need the config.txt file. Have fun!
