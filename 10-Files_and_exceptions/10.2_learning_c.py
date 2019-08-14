archivo = "learning_python.txt"

with open(archivo) as archivo_obj:
    complete_arch = archivo_obj.read()
    complete_arch.replace("Python", "C")
    print(complete_arch)

#Line by line inside of with block
with open(archivo) as archivo_obj:
    for line in archivo_obj:
        line.replace("Python", "C")
        print(line.rstrip())
    
#Line by line outside of with block
with open(archivo)  as archivo_obj:
    archive = archivo_obj.readlines()    

for line in archive:
    line = line.rstrip()
    print(line.replace("Python", "C"))