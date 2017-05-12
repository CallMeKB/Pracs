"""
CP1404 - Prac07
console program to test programming language class
"""

from prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    language_list = [ruby, python, vb]
    print("The dynamically typed languages are:")
    for language in language_list:
        if language.typing == "Dynamic":
            print(language.name)

main()
