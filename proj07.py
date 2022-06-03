###############################################################################
#   Project 7
#
# First I use open_file to open the file, and try-except to check error
#  use for-in to find the 1,4,9,10,11 columns, if-in to delete unqualified rows
#   and use replace to delete error characters
#    next,I use if to find denied,approved,settled, and calculate total average
#     call the operator. Itemgetter to find the maximum and name,
#      after that, I use display_data function to set the format
#        then, plot the graph in the plot function
#           in main(), I call the above function 
#             Finally, I use if!= no to check if user wants plot.
#         
############################################################################### 

import pylab   # needed for plotting
from operator import itemgetter

STATUS = ['Approved','Denied','Settled'] 

def open_file():
    '''
    This function is asked user to enter filename, open and return the file. 
    If the file is not found, ask the filename again.
    '''
    file_name = input("Please enter a file name: ")
    while True:# input document
        try:
            fp = open(file_name,"r") #try to open the file
            return fp #read document
        except: #check if can not find the file
            file_name = input("File not found. Please enter a valid file name: ")          

def read_file(fp):
    '''
    Extract the column (1, 4, 9, 10, 11) from the file, 
    remove the blank column, and remove the extra characters,
    and returns data as a tuple.
    '''
    counter = 0
    place = [1,4,9,10,11] 
    all_tuple = [] 
    for i in fp: 
        if counter > 0: 
            temp = []
            value = i.split(',') # divide them with commas
            for p in place: # find the 1,4,9,10,11 columns
                temp.append(value[p])
            if '' in temp:
                continue
             #delete columns of black data
             
            if  not (int(temp[0][-2:]) <=9 and int(temp[0][-2:]) >= 2):
                continue
            # delete columns except for 2002-2009
            
            temp[2] = temp[2][1:]
            temp[2] = float(temp[2].replace(';',''))
            temp[4] = temp[4][1:]
            temp[4] = float(temp[4].replace(';',''))
            # delete "$" and ";" in datas
            
            temp = tuple(temp)
            all_tuple.append(temp)
            # into a tuple form
            
        else:
            counter+=1
            
    return all_tuple #return the tuple

def process(data):
    '''
    Check the data line by line, adding 1 if they satisfy the condition,
    calculate the total, average, 2002-2009 settled and denied,
    organize the data and arrange them into list,
    call the operator. Itemgetter to find the maximum and name,
    and return theses datas as a tuple.
    '''
    num_approved = 0 # total number of approved in the file
    num_settled = 0  # total number of settled
    num_denied = 0 # total number of denied
    num_zero = 0 # total number of zero
    
    num_settled_02 = 0
    num_denied_02 = 0 # in 2002, number of settled and denied
    
    num_settled_03 = 0 # in 2003
    num_denied_03 = 0
    
    num_settled_04 = 0 # in 2004
    num_denied_04 = 0
    
    num_settled_05 = 0 # in 2005
    num_denied_05 = 0
    
    num_settled_06 = 0 # in 2006
    num_denied_06 = 0
    
    num_settled_07 = 0 # in 2007
    num_denied_07 = 0
    
    num_settled_08 = 0 # in 2008
    num_denied_08 = 0
    
    num_settled_09 = 0 # in 2009
    num_denied_09 = 0
    
    #Calculate the total
    for line in data:
        if line[3] == "Approved":
            num_approved += 1
        if line[3] == "Settled":
            num_settled += 1
        if line[3] == "Denied":
            num_denied += 1
         # use if to find the number of "Approved","Settled","Denied"
         # if they exist, add 1
         
    total = num_approved + num_settled + num_denied #cal the total
    
    total_amount = 0
    #Calculate the average
    for line in data:
        if line[4] != 0.0 and (line[3] == 'Approved' or line[3] == 'Settled'):
            num_zero += 1 # find the number equal to 0
            total_amount+=line[4]
                
    average = total_amount/(num_zero) # cal the average
    
    for line in data:
        #Calculate the settled, denied each year
        if line[0][-2:] == "02": # use 'if' to find information for 2002
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_02 += 1
                #settled and approved are in the same situation
            elif line[3] == 'Denied':
                num_denied_02 += 1
            
        if line[0][-2:] == "03": # similar to the one above for 2003
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_03 += 1
            elif line[3] == 'Denied':
                num_denied_03 += 1
            
        if line[0][-2:] == "04": # 2004
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_04 += 1
            elif line[3] == 'Denied':
                num_denied_04 += 1
        
        if line[0][-2:] == "05": # 2005
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_05 += 1
            elif line[3] == 'Denied':
                num_denied_05 += 1

        if line[0][-2:] == "06": # 2006
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_06 += 1
            elif line[3] == 'Denied':
                num_denied_06 += 1
            
        if line[0][-2:] == "07": #2007
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_07 += 1
            elif line[3] == 'Denied':
                num_denied_07 += 1
            
        if line[0][-2:] == "08": #2008
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_08 += 1
            elif line[3] == 'Denied':
                num_denied_08 += 1
            
        if line[0][-2:] == "09": #2009
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_09 += 1
            elif line[3] == 'Denied':
                num_denied_09 += 1
        
    #calculate the total number of each year separately
    total_02 = num_settled_02 + num_denied_02
    total_03 = num_settled_03 + num_denied_03
    total_04 = num_settled_04 + num_denied_04
    total_05 = num_settled_05 + num_denied_05
    total_06 = num_settled_06 + num_denied_06
    total_07 = num_settled_07 + num_denied_07
    total_08 = num_settled_08 + num_denied_08
    total_09 = num_settled_09 + num_denied_09
    
    #to arrange the data into a list
    list1 = [total_02,total_03,total_04,total_05,total_06,total_07,total_08,total_09]
    list2 = [num_settled_02,num_settled_03,num_settled_04,num_settled_05,num_settled_06,num_settled_07,num_settled_08,num_settled_09]
    list3 = [num_denied_02,num_denied_03,num_denied_04,num_denied_05,num_denied_06,num_denied_07,num_denied_08,num_denied_09]
    
    #find the max claim and max airport
    data.sort(key=itemgetter(2), reverse = True)
    max_claim = data[0][2]
    max_claim_airport = data[0][1] 
    #the name of the airport with the maximum claim value
    return (list1,list2,list3,total,average,max_claim,max_claim_airport)

def display_data(tup):   
    '''
    Prints in the specified format
    '''    
    print("TSA Claims Data: 2002 - 2009")
    print("")
    total = tup[3]
    print("N = {:<10,d}".format(total))
    print("")
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ",'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'))
    list1 = tup[0]
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Total",list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7]))
    list2 = tup[1]
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Settled",list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7]))
    list3 = tup[2] 
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Denied",list3[0],list3[1],list3[2],list3[3],list3[4],list3[5],list3[6],list3[7]))
    print("")
    average = tup[4]
    print("Average settlement: ${:<10,.2f}".format(average))
    max_claim = tup[5]
    max_claim_airport = tup[6]
    print("The maximum claim was ${:,.2f}".format(max_claim) + " at " + max_claim_airport + " Airport")
    
def plot_data(accepted_data, settled_data, denied_data):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(8)   # create 8 items to hold the data for graphing
    # assign each list's values to the 8 items to be graphed, include a color and a label
    pylab.bar(X, accepted_data, color = 'b', width = 0.25, label="total")
    pylab.bar(X + 0.25, settled_data, color = 'g', width = 0.25, label="settled")
    pylab.bar(X + 0.50, denied_data, color = 'r', width = 0.25,label="denied")

    # label the y axis
    pylab.ylabel('Number of cases')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2002","2003","2004","2005","2006","2007","2008","2009"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")
    
def main():
    '''
    Run the above function and ask the user if they want plot data
    '''
    fp = open_file() # open the file
    data = read_file(fp) #read the file
    tup = process(data) # cal the data
    display_data(tup) #format
    if input("Plot data (yes/no): ").lower() != 'no':
        plot_data(tup[0],tup[1],tup[2])
    #ask the user if they want plot data

if __name__ == "__main__":
    main()
