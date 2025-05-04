EBasic Interpreter
EBasic is a custom interpreter with Turkish keywords like ENV (if), EGER (while), and EGLENCE (function). It supports variables, conditionals, loops, and functions, designed for educational purposes.
Installation
To install the EBasic package:
pip install --user .

Usage
Interactive Shell
Run the interactive shell to test EBasic commands:
python shell.py

Example commands:
basic > VAR x = 5
5
basic > ENV x > 3 THEN 10 ELSE 20
10
basic > EGLENCE topla(a, b) -> a + b
<function topla>
basic > topla(2, 3)
5

Programmatic Use
Use EBasic in your Python projects:
from EBasic import run

program = """
VAR x = 5
ENV x > 3 THEN 10 ELSE 20
"""

result, error = run('<test>', program)
if error:
    print(error.as_string())
else:
    print(f"Result: {result}")

Output:
Result: 10

Grammar
The grammar rules for the EBasic language are documented in the grammar.txt file.
Project Structure
EBasic/
├── EBasic/
│   ├── __init__.py
│   ├── EBasic.py
│   ├── strings_with_arrows.py
├── setup.py
├── shell.py
├── README.md
├── LICENSE
├── .gitignore
├── grammar.txt

License
This project is licensed under the MIT License - see the LICENSE file for details.
