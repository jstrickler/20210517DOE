
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n" # r'''spam\n'''

print("The shrimp's on the barbie")
print('This is "Crocodile" Dundee')

s3 = '''The shrimp's on the "barbie"'''
print(s3)

query = """
select *
from log20210515
where spam = 'ham'
"""
