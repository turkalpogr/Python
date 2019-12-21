x = 'globalecho "# Python" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/turkalpogr/Python.git
git push -u origin master
'

def func():
    x = 'local x'
    print(x)

func()
print(x)

