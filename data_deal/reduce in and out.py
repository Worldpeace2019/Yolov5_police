from pathlib import Path
import numpy as np
# count=np.zeros()
path = './labels/labels/'
items = Path(path).iterdir()

for item in items:
    lines_str=''
    start_flag=0
    itme_path = Path(path+item.name)
    contant = itme_path.read_text()
    print(item.name)
    class_lines = contant.splitlines()
    for class_line in class_lines:
        # print(class_line)
        print(len(class_line))
        if len(class_line)==0:
            continue
        car_class = class_line.split(' ')[0]
        car_contant = ' '.join(class_line.split(' ')[1:])
        if car_class == '0' :
            car_class='0'
        elif car_class == '1' :
            car_class='1'
        elif car_class == '2' :
            car_class='0'
        elif car_class == '3' :
            car_class='1'
        elif car_class == '4' :
            car_class='2'
        elif car_class == '5' :
            car_class='3'
        elif car_class == '6' :
            car_class='2'
        elif car_class == '7' :
            car_class='3'
        elif car_class == '8' :
            car_class='4'
        elif car_class == '9' :
            car_class='4'
        elif car_class == '10' :
            car_class='5'
        elif car_class == '11' :
            car_class='5'
        elif car_class == '12' :
            car_class='6'
        elif car_class == '13' :
            car_class='6'
        elif car_class == '14' :
            car_class='7'
        elif car_class == '15' :
            car_class='7'
        elif car_class == '16' :
            car_class='8'
        elif car_class == '17' :
            car_class='8'
        elif car_class == '18' :
            car_class='9'
        elif car_class == '19' :
            car_class='9'
        elif car_class == '20' :
            car_class='0'
        elif car_class == '21' :
            car_class='1'
        elif car_class == '22' :
            car_class='2'
        elif car_class == '23' :
            car_class='3'
        elif car_class == '24' :
            car_class='4'
        elif car_class == '25' :
            car_class='5'
        elif car_class == '26' :
            car_class='6'
        elif car_class == '27' :
            car_class='7'
        elif car_class == '28' :
            car_class='8'
        elif car_class == '29' :
            car_class='9'
        line_contant = car_class + ' ' + car_contant
        if  not start_flag:
            lines_str = line_contant
            start_flag=1
            continue
        if start_flag:
            lines_str = lines_str + '\n' +line_contant
    item.write_text(lines_str)