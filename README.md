# Interpreted Programming Language
 Attempt to develop a Programming Language with interpretation in python by lexing the program and parsing tokens for execution.
 The Project attempts to understand the process of interpreters by creating a dummy language and performing parsing and lexing.
# Project Content
The project will include a source.py file which is the brain of the interpreter, it is programmed to run a text file passed as an argument to the code while exeuction. There exists a file named guidelines.txt explaining the token names and their operations which will be handy to refer while modifying the source.py file.<br>
Along with these, the project also includes a Test.rhg file which includes a simple program written in this new language which can be passed to source.py for execution.
# Dependencies
The system on which the program is going to run should have these installed:
- Python 3.6
# Features supported by Language
This is a basic attempt to replecate functionality of a programming language thus only includes:
- Variable Declaration (not DataType dependent)
- Outputing and Inputing to/from peripherals
- If/Else Conditions
- Loops
# How To Run
To execute the program written in this new language, the program must be written in a file say named 'file.rhg' which is in same directory as of the source.py, simply execute the command:<br>
```
python source.py file.rhg
```
or
```
python3 source.py file.rhg
```
