# Source: https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parents

import pathlib

print("""
Dada una ruta, imprime la ruta completa hasta el nivel deseado
La ruta es:  ./a/b/c/d
El nivel es: 3/2/1/0/_ <-- El ultimo no esta por que es la ruta completa
""")

p = pathlib.PurePosixPath('./a/b/c/d')

for n in reversed(range(0, 4)):
  print(str(n) + ' - ' + str(p.parents[n]))

# Output:
# 3 - .
# 2 - a
# 1 - a/b
# 0 - a/b/c