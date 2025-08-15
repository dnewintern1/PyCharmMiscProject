#package
from setuptools import setup
setup(
    name = 'calculator',
    version = '1.0',
    description= 'mypython module',
    author = 'radhe',
    author_email = 'anonymous@loonycorn.com',
    url = 'loonycorn.com',
    py_modules = ['calculator']
)


#module


def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mult(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
#%%
#creating a distriburable package

# js-shell: mkdir modulles
# js-shell: mkdir modules
# mkdir: cannot create directory ‘modules’: File exists
# js-shell: cd modules
# js-shell: pwd
# /drive/modules
# js-shell: mkdircalculator
# Error: 'mkdircalculator': command not found
# js-shell: mkdri calculator
# Error: 'mkdri': command not found
# js-shell: mkdir calculator
# js-shell: cd calculator
# js-shell: vim calculator.py
# js-shell: ls
# calculator.py
# js-shell: vim setup.py
# js-shell: ls
# calculator.py  setup.py
# js-shell: python setup.py sdist
# Error: 'python': command not found
# js-shell: setup.py sdist
# Error: 'setup.py': command not found
# js-shell: python setup.py sdist
# Error: 'python': command not found
# js-shell: pwd
# /drive/modules/calculator
# js-shell: ls
# calculator.py  setup.py
# js-shell: help(Modules)
# Error: 'help(Modules)': command not found
# js-shell: help("modules")
# Error: 'help(modules)': command not found
# js-shell:
