###############################################################################
#   Project 5
#
# First I use open_file to open the file, and try-except to check error
#   Then output the headers with the correct spaces
#    Next, calculate the delta. I calculated the result for each row in the file
#     Then rearrange them and output the maximum value per line
#      After that, I still need to output the largest delta value of the previous value
#       I used for to check it and then output the maximum delta
#        Finally, I use “main” to close the file
#         
###############################################################################   

def open_file():
    while True:# input document
        file_name = input("Enter a file name: ")
        try:
            file = open(file_name,"r")
            return file#read document
        except: #check error
            print("Error. Please try again.")
            file_name = input("Enter a file name: ")
            file = open(file_name,"r")

def print_headers():#print header
    print("\n     Maximum Population Change by Continent")
    print("      ")
    print("{:<26s}{:>9s}{:>10s}".format("Continent","Years","Delta"))

def calc_delta(line,col):#Calculate the biggest change each year
    
    l = ""
    for i in line:
        continent = line[:15]
        y1750 = str(line[15:21].strip())
        y1800 = str(line[21:27].strip())
        y1850 = str(line[27:33].strip())
        y1900 = str(line[33:39].strip())
        y1950 = str(line[39:45].strip())
        y2000 = str(line[45:51].strip())
        y2050 = str(line[51:57].strip())
        l = (continent,y1750,y1800,y1850,y1900,y1950,y2000,y2050)
        delta = float(int(l[col+1].strip())-int(l[col].strip()))/float(l[col].strip())
    return delta

def format_display_line(continent,year,delta):
    year_1 = year - 50
    str_year = str(year_1)+"-"+str(year)
    string = ("{:<26s}{:>9s}{:>10s}".format(continent,str_year,str(round(delta*100))+"%"))
    return string

def main():
    file = open_file()
    print_headers()
    file.readline()
    file.readline()
    max_delta2 = 0
    max_year2 = 0
    for line in file:
        max_delta = 0
        max_name = line[:15].strip()
        max_year = 0
        for col in range(1,7):
            delta = calc_delta(line,col)
            if delta > max_delta:
                max_delta = delta
                max_year = 1750 + col*50
                if max_delta>max_delta2:
                     max_delta2 = delta
                     max_year2 = 1750 + col*50
                     max_name2 = max_name
                     
        print(format_display_line(max_name,max_year,max_delta))
    print("")
    print("Maximum of all continents:")
    print(format_display_line(max_name2,max_year2,max_delta2))
#output max
#end
if __name__ == "__main__":
    main()