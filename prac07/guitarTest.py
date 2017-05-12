"""
CP1404 Prac 07 - test program to check guitar class methods
"""

from prac07.guitar import Guitar

L5 = Guitar("Gibson L-5 CES", 1922, 16035)
D45 = Guitar("Martin D-45", 1933, 8659)
print(L5)
print(L5.get_age())
print(L5.is_vintage())