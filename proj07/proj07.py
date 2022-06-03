'''Introductory information goes here.'''

import pylab   # needed for plotting
from operator import itemgetter

STATUS = ['Approved','Denied','Settled'] 

def open_file():    
    
    while True:# input document
        file_name = input("Please enter a file name: ")
        try:
            fp = open(file_name,"r")
            return fp#read document
        except: #check error
            print("File not found. Please enter a valid file name: ")
            file_name = input("Please enter a file name: ")
            fp = open(file_name,"r")

def read_file(fp):
    '''Docstring goes here.'''
    counter = 0
    place = [1,4,9,10,11]
    all_tuple = []
    for i in fp:
        if counter > 0:
            temp = []
            value = i.split(',')
            for p in place:
                temp.append(value[p])
            if '' in temp:
                continue
            if  not (int(temp[0][-2:]) <=9 and int(temp[0][-2:]) >= 2):
                continue
            
            temp[2] = temp[2][1:]
            temp[2] = float(temp[2].replace(';',''))
            temp[4] = temp[4][1:]
            temp[4] = float(temp[4].replace(';',''))
            
            temp = tuple(temp)
            all_tuple.append(temp)
            
        else:
            counter+=1
    return all_tuple

def process(data):
    num_approved = 0
    num_settled = 0
    num_denied = 0
    num_zero = 0
    
    num_settled_02 = 0
    num_denied_02 = 0
    
    num_settled_03 = 0
    num_denied_03 = 0
    
    num_settled_04 = 0
    num_denied_04 = 0
    
    num_settled_05 = 0
    num_denied_05 = 0
    
    num_settled_06 = 0
    num_denied_06 = 0
    
    num_settled_07 = 0
    num_denied_07 = 0
    
    num_settled_08 = 0
    num_denied_08 = 0
    
    num_settled_09 = 0
    num_denied_09 = 0
    
    for line in data:
        if line[3] == "Approved":
            num_approved += 1
        if line[3] == "Settled":
            num_settled += 1
        if line[3] == "Denied":
            num_denied += 1
    total = num_approved + num_settled + num_denied
    
    total_amount = 0
    for line in data:
        if line[4] == 0.0 and (line[3] == 'Approved' and line[3] == 'Settled'):
            num_zero += 1
        total_amount+=line[4]
                
    average = total_amount/(num_approved + num_settled - num_zero)
    
    for line in data:
        
        if line[0][-2:] == "02":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_02 += 1
            elif line[3] == 'Denied':
                num_denied_02 += 1
            
        if line[0][-2:] == "03":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_03 += 1
            elif line[3] == 'Denied':
                num_denied_03 += 1
            
        if line[0][-2:] == "04":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_04 += 1
            elif line[3] == 'Denied':
                num_denied_04 += 1
        
        if line[0][-2:] == "05":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_05 += 1
            elif line[3] == 'Denied':
                num_denied_05 += 1

        if line[0][-2:] == "06":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_06 += 1
            elif line[3] == 'Denied':
                num_denied_06 += 1
            
        if line[0][-2:] == "07":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_07 += 1
            elif line[3] == 'Denied':
                num_denied_07 += 1
            
        if line[0][-2:] == "08":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_08 += 1
            elif line[3] == 'Denied':
                num_denied_08 += 1
            
        if line[0][-2:] == "09":
            if line[3] == "Settled" or line[3] == 'Approved':
                num_settled_09 += 1
            elif line[3] == 'Denied':
                num_denied_09 += 1
        
    total_02 = num_settled_02 + num_denied_02
    total_03 = num_settled_03 + num_denied_03
    total_04 = num_settled_04 + num_denied_04
    total_05 = num_settled_05 + num_denied_05
    total_06 = num_settled_06 + num_denied_06
    total_07 = num_settled_07 + num_denied_07
    total_08 = num_settled_08 + num_denied_08
    total_09 = num_settled_09 + num_denied_09
    list1 = [total_02,total_03,total_04,total_05,total_06,total_07,total_08,total_09]
    list2 = [num_settled_02,num_settled_03,num_settled_04,num_settled_05,num_settled_06,num_settled_07,num_settled_08,num_settled_09]
    list3 = [num_denied_02,num_denied_03,num_denied_04,num_denied_05,num_denied_06,num_denied_07,num_denied_08,num_denied_09]
    
    data.sort(key=itemgetter(2), reverse = True)
    max_claim = data[0][2]
    max_claim_airport = data[0][1]
    return (list1,list2,list3,total,average,max_claim,max_claim_airport)

def display_data(tup):

    print("TSA Claims Data: 2002 - 2009")
    print("")
    total = tup[3]
    print("N = ",total)
    print("")
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ",'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'))
    list1 = tup[0]
    print("{:<8s}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}".format("Total",list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7]))
    list2 = tup[1]
    print("{:<8s}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}".format("Settled",list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7]))
    list3 = tup[2] 
    print("{:<8s}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}{:>8d}".format("Denied",list3[0],list3[1],list3[2],list3[3],list3[4],list3[5],list3[6],list3[7]))
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
    #f = open_file()
    f = open('tsa_claims_small.csv')
    data = read_file(f)
    tup = process(data)
    display_data(tup)
    if input("Plot data (yes/no): ").lower() != 'no':
        plot_data(tup[0],tup[1],tup[2])
        
    

if __name__ == "__main__":
    main()
