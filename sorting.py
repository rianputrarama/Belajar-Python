colors = ["red","green","blue","orange"]

colors.sort(reverse=True)

print(colors)
print(sorted(colors), ' \n')

emp = [
  {'desc': 'Software Enginer', 'year': 2015},
  {'desc': 'Project Manager', 'year': 2010},
  {'desc': 'Tech Lead', 'year': 2018},
  {'desc': 'Dev Ops', 'year': 2019}
]
# based on the year
def byYear(e):
    return e['year']

emp.sort(key=byYear)

for employees in emp:
    print(employees)

