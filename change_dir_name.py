import os

dir_list = os.listdir('.')
for dir_name in dir_list:
    if "FPS_KHP" in dir_name:
        afir_str = dir_name[dir_name.rfind('A'):]
        new_name = afir_str[1]+'-'+afir_str[4]+'-'+afir_str[7]+'-'+afir_str[10]
        print("RENAMED", dir_name, "to", new_name)
        os.rename(dir_name, new_name)
