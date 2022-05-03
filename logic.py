import re
from templates import temps,temps_list

print("\nTemplates available: \n")
for i in temps_list:
    print(i)
strg = temps[input("\n\nEnter Template name: ")]
pattern = "\[(.*?)\]"
y = re.findall(pattern,strg)
for i in y:
    txt = input(f"{i}: ")
    strg = strg.replace(f"[{i}]", txt)

print(strg)