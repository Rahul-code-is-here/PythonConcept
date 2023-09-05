from pathlib import Path

#absolute path
#c:\Program Files\Microsoft
#Relative path

#path=Path("ecoomerce")
#print(path.exists())

#path=Path("emais")
#print(path.mkdir()) #emails  directory banavi deshe
#print(path.rmdir())  #directory remove kari deshe

path=Path()
for file in path.glob('*.py'):
    print(file)
