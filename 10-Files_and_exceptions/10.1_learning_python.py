archivo = "learning_python.txt"
#Reading the entire file
with open(archivo) as archivo_obj:
    complete_arch = archivo_obj.read()
    print(complete_arch)

#Line by line inside of with block
with open(archivo) as archivo_obj:
        for line in archivo_obj:
            print(line.rstrip())

#Line by line outside of with block
with open(archivo)  as archivo_obj:
    archive = archivo_obj.readlines()
      
for line in archive:
    print(line.rstrip())
        