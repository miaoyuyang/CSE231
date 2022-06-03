###############################################################################
#   Project 08
#
# First I use open_file to open the file, and try-except to check error
#  and I will creat a new dictionary. It have three keys(region,country,age).
#   My method is to use if-in to check if the key is in dic,
#    if yes, it will continue to check if the next key exists in the dic.
#     if not, it will create a new one. Also, use if-else to check every lines.
#      next, I use three for-loop to sort out a country-key dic, value is key's 
#       total of diabetics and population based on the data from the last func. 
#        and than, I will prepare the data for plot, its a dic, the key is age,
#         the value is the number of male and female with diabetes, I will use
#          for loop the cal them. Later, I use the prepared_data to plot.
#           in main(), I call the above function. The user will input the code,
#            I use if-in to check them, if not in REGIONS, it will show error.
#
#         
############################################################################### 
import pylab 
#from operator import itemgetter # optional, if you use itemgetter when sorting

REGIONS = {'MENA':'Middle East and North Africa','EUR':'Europe',\
               'AFR':'Africa','NAC':'North America and Caribbean',\
               'SACA':'South and Central America',\
               'WP':'Western Pacific','SEA':'South East Asia'}

def open_file():
    '''
    This function is asked user to enter filename, open and return the file. 
    If the file is not found, ask the filename again.
    '''
    file_name = input("Please enter a file name: ")
    while True:# input document
        try:
            fp = open(file_name,encoding = "windows-1252")#try to open the file
            return fp #read document
        except: #check if can not find the file
            file_name = input("File not found. Please enter a valid file name: ")    
            # test.   diabetes_data_tiny.csv
    
def create_dictionary(fp):
    '''
    In this fuction, I need to get a file from the open_file, and return a dic
    that is a dictionary of dictionaries of dictionaries of lists of tup.
    At first, I creat a dic and a counter, I will skip the header of the file.
    Scecond, I get them by the position of the information in each line,
    Because I need to return a dictionary that contains three dictionaries, 
    I decide to one by one to check whether these exist in the key of each dic, 
    if there exists continue to check the next level of the dictionary, 
    and if there is not exists create a new one.
    '''
    counter = 0 
    dic_region = {} # create a dictionary
    
    for i in fp: # pick up the file
        
        if counter > 0: # read the file from the second line
            
            value = i.split(',') # split them
            
            # Extract the information I need
            country = value[1]
            region = value[2]
            age_group = value[3]
            gender = value[4]
            geographic_area = value[5]
            diabetes = int(float(value[6])*1000) 
            population = int(float(value[7])*1000)
    
            #Create a tuple that includes gender,are,diabetes,population 
            tup = (gender, geographic_area, diabetes, population)
         
            if region in dic_region.keys():
            # if region exists in dic_region keys,
            # if yes, continue to check if country in dic_region[region] keys,
                
                if country in dic_region[region].keys():
                # if country existis in the second dic, 
                # if yes, continue to check if age in the third dic    
                    
                    # to check if age in dic_region[region][country].keys
                    # if yes, append tuple to the dic
                    # if not, creat a new one that key is this new age group
                    if age_group in dic_region[region][country].keys():
                    # to check if age in dic_region[region][country].keys
                    # if yes, append tuple to the dic
                        dic_region[region][country][age_group].append(tup)
                    else:
                        dic_region[region][country][age_group] = []
                        dic_region[region][country][age_group].append(tup)
                else:
                # if not,creat a new one that key is country
                    dic_region[region][country] = {}
                    dic_region[region][country][age_group] = []
                    dic_region[region][country][age_group].append(tup)
            else:
            # if not, creat a blank dictionary that key is region
                dic_region[region] = {}
                dic_region[region][country] = {}
                dic_region[region][country][age_group] = []
                dic_region[region][country][age_group].append(tup)
            
        else:
            counter +=1 #continue to read the next line
            
    return dic_region

def get_country_total(data):
    '''
    I will get the data from the func above, and return a new dic, that key is 
    region, and value is the sum of diabetics and popula in the same country.
    '''
    dic_total = {}
    lst = data.items()
    lst = sorted(lst) 
    for k,v in lst:
        country_bp = [] # creat a list
        total_b = 0 #counter
        total_p = 0 
        
        for v1 in v.values():
            for tup in v1: # Get the outermost key in the dictionary
                total_b += tup[2] #cal the total of diabetics
                total_p += tup[3] #cal the total of population
        country_bp.append(total_b) #
        country_bp.append(total_p)
        dic_total[k] = tuple(country_bp) #transfer to tuples
    return dic_total        

def display_table(data, region):
    '''
    This funciton for prints datas in the specified format. 
    In particular, I'll need to use a for loop to compute the sum.
    If the country's words has more than 25, I need to omit the letter after 25.
    '''
    print("     Diabetes Prevalence in ",region)
    print("{:<25s}{:>20s}{:>16s}".format(
            'Country Name',
          'Diabetes Prevalence',
          'Population'))
    print()
    total_dia = 0
    total_pop = 0 #counter
    for k,v in data.items():
        # use for loop to cal the total number
        total_dia += v[0] # total number of people with diabetes in the file
        total_pop += v[1] # # total number of population in the file
        print("{:<25s}{:>20,d}{:>16,d}".format(k[:25],v[0],v[1]))
    print()
    print("{:<25s}{:>20,d}{:>16,d}".format('TOTAL',total_dia,total_pop))

def prepare_plot(data):
    '''
    This function is to prepare the data for the plot, and it will return a dic
    whose keys are the age_group and value are tuples, which is the sum of the 
    number of male with diabetes and the number of remale with diabetes.
    '''
    
    dic_age_result = {} #creat a dic
    
    for k,v in data.items(): # key is countryname
        for k2,v2 in v.items(): #key is age group
            if k2 not in dic_age_result:
                dic_age_result[k2]={'MALE':0,'FEMALE':0}
            for tup in v2:
                # use the for-loop to calculate the sum
                if tup[0] == 'Female':
                    dic_age_result[k2]['FEMALE']+=tup[2]
                elif tup[0] == 'Male':
                    dic_age_result[k2]['MALE']+=tup[2]
                    
    return dic_age_result
                     

def plot_data(plot_type,data,title):
    '''
        This function plots the data. 
            1) Bar plot: Plots the diabetes prevalence of various age groups in
                         a specific region.
            2) Pie chart: Plots the diabetes prevalence by gender. 
    
        Parameters:
            plot_type (string): Indicates what plotting function is used.
            data (dict): Contains the dibetes prevalence of all the contries 
                         within a specific region.
            title (string): Plot title
            
        Returns: 
            None     
    '''
    
    plot_type = plot_type.upper()
    
    categories = data.keys() # Have the list of age groups
    gender = ['FEMALE','MALE'] # List of the genders used in this dataset
    
    if plot_type == 'BAR':
        
        # List of population with diabetes per age group and gender
        female = [data[x][gender[0]] for x in categories]
        male = [data[x][gender[1]] for x in categories] 
        
        # Make the bar plots
        width = 0.35
        p1 = pylab.bar([x for x in range(len(categories))], female, width = width)
        p2 = pylab.bar([x + width for x in range(len(categories))], male, width = width)
        pylab.legend((p1[0],p2[0]),gender)
    
        pylab.title(title)
        pylab.xlabel('Age Group')
        pylab.ylabel('Population with Diabetes')
        
        # Place the tick between both bar plots
        pylab.xticks([x + width/2 for x in range(len(categories))], categories, rotation='vertical')
        pylab.show()
        #optionally save the plot to a file;file extension determines file type
        #pylab.savefig("plot_bar.png")
        
        
    elif plot_type == 'PIE':
        
        # total population with diabetes per gender
        male = sum([data[x][gender[1]] for x in categories])
        female = sum([data[x][gender[0]] for x in categories])
        
        pylab.title(title)
        pylab.pie([female,male],labels=gender,autopct='%1.1f%%')
        pylab.show()
        #optionally save the plot to a file;file extension determines file type
        #pylab.savefig("plot_pie.png")

def main():
    '''
    Run the above function and ask the user if they want to quit
    '''
    fp = open_file() #open the file
    file = create_dictionary(fp) #creat a dictionary
    
    "\nDiabetes Prevalence Data in 2017"
    MENU = \
    '''
                Region Codes
    MENA: Middle East and North Africa
    EUR: Europe
    AFR: Africa
    NAC: North America and Caribbean
    SACA: South and Central America
    WP: Western Pacific
    SEA: South East Asia
    '''
    
    "Enter region code ('quit' to terminate): "
    "Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: "
    "Error with the region key! Try another region"
    "Incorrect Input! Try Again!"
    
    while True:
        print(MENU)
        code = input("Enter region code ('quit' to terminate): ")
        #input the code
        
        if code.lower() == 'quit':
            break
        # if input 'quit', it will break
        
        if code.upper() in REGIONS:
            total = get_country_total(file[code.upper()])
            display_table(total,REGIONS[code.upper()])
            # Get the full name of the country
        else: 
            print("Error with the region key! Try another region")
            continue
            #if code not in regions, it will show error.
        
        ans = input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: ")
        if ans.lower() == 'yes':
            # if answer is yes
            plot_da = prepare_plot(file[code.upper()]) 
            # draw a pie chart
            plot_data("PIE",plot_da,"Diabetes Prevalence in "+REGIONS[code.upper()]+"by Age Group and Gender")
            # draw a bar chart
            plot_data("BAR",plot_da,"Diabetes Prevalence in "+REGIONS[code.upper()]+"by Age Group and Gender")
        
        
    
###### Main Code ######
if __name__ == "__main__":
    main()
