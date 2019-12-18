# ProgramInVoice
Dictate your python code by speech!


  PIV(PythonInVoice) is a package which allows you to dictate python code by speech. It's basically realized using baidu-aip speech recognation API. Of course some more interesting and convenient features were added as well.
  Let's start dictation using PIV.

## Installation
### Dependency
  Three packages are needed before you're going to use PIV. **numpy**, **Pyaudio** and **baidu-aip**. **numpy** provides vector and array tools for text analysis in **preProcess.py**. **Pyaudio** is used to allow python to connect your microphone. And **baidu-aip** is a package including speech recognition API with a great accuracy developed by Baidu,China.
  These packages will be installed simutaneously when you setup PIV, if your environment lacks of them.
### Install PIV
  To install PIV, you just need to download ZIP from github to your local file folder whose path is like xxx/PIV. Then cd to this path 
(e.g.: `cd xxx/PIV` in **cmd**,Windows). And run `pip install -e .` to install PIV to your python environment.

## Usage
