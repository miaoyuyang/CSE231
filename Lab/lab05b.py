def BMI(weight,height):
    BMI = (weight/(height**2))
    return BMI

file = open("data.txt","r")

#head = file.readline().strip()+ "  BMI"
print(file.readline().strip()+ "  BMI         ")

height_max = 0
height_min = 10**6
weight_max = 0
weight_min = 10**6
total_height = 0
total_weight = 0
total_BMI = 0
BMI_min = 10**6
BMI_max = 0
num = 0

for line in file:
    line = line.strip()
    name = line[:6]
    height = float(line[12:16])
    weight = float(line[24:29])
    bmi = BMI(weight,height)
    
    if height_max < height:
        height_max = height
        
    if weight_max < weight:
        weight_max = weight
    
    if BMI_max < bmi:
        BMI_max = bmi
        
    if height_min > height:
        height_min = height
        
    if weight_min > weight:
        weight_min = weight
        
    if BMI_min > bmi:
        BMI_min = bmi

        
    num += 1
    total_height += height
    total_weight += weight
    total_BMI += bmi
    
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name,height,weight,bmi))
    
height_ave = total_height/num
weight_ave = total_weight/num
BMI_ave = total_BMI/num

print()
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",height_ave,weight_ave,BMI_ave))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",height_max,weight_max,BMI_max))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",height_min,weight_min,BMI_min))

outfile = open("output.txt","w") 
print()
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",height_ave,weight_ave,BMI_ave),file = outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",height_max,weight_max,BMI_max),file = outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",height_min,weight_min,BMI_min),file = outfile)

outfile.close()