'''Introductory information goes here.'''

import pylab   # needed for plotting
from operator import itemgetter

STATUS = ['Approved','Denied','Settled'] 

def open_file():
    file_name = input('Please enter a file name: ')
    while True:
        try:
            file = open(file_name,"r")
            return file
        except:
            print('File not found. Please enter a valid file name: ')
            file_name = input('Please enter a file name: ')

def read_file(opened_file):
    tuple_a=[]
    temp=[]
    column=0
    list_column=[1,4,9,10,11]
    for i in opened_file:
        if column != 0:
            d = i.split(',')
            for a in list_column:
                temp.append(d[a])
            if '' in temp:
                continue
            if not 2 <= int(temp[0][-2:]) <= 9:
                continue
            a = temp[2].replace('$','')
            a = temp[2].replace(';','')
            a = float(a)
            b = temp[4].replace('$','')
            b = temp[4].replace(';','')
            b = float(b)
            temp=tuple(temp)
            tuple_a.append(temp)
        else:
            column+=1     
    
    
def process(data):
    num_year = [2,3,4,5,6,7,8,9]
    dic_1={}
    dic_2={}
    dic_3={}
    list1=[]
    list2=[]
    list3=[]
    a=0
    acount=0
    total_all=0
    max_num=0
    amount=0
    for i in num_year:
        dic_1[str(i)]=0
        dic_2[str(i)]=0
        dic_3[str(i)]=0
        year=data[a][0][-1]
        if data[a][3] == 'Settled' or 'Approved' or 'Denied':
            acount+=1
            dic_1[str(year)]+=1
            if data[a][3] == 'Settled' or 'Approved':
                dic_2[str(year)]+=1
                if data[a][4]!=0:
                    total_all +=data[a][4]
                    amount+=1
            else:
                dic_3[str(year)]+=1
        a+=1
    average=total_all/amount
    for key in dic_1:
        list1.append(dic_1[key])
        list2.append(dic_2[key])
        list3.append(dic_3[key])
    data.sort(key=itemgetter(2), reverse = True)
    max_num = data[0][2]
    max_name = data[0][1] 
    return (list1,list2,list3,total_all,average,max_num,max_name)
                
        
    

def display_data(tup):
    list1=tup[0]
    list2=tup[1]
    list3=tup[2]
    total=tup[3]
    average=tup[4]
    max_claim=tup[5]
    max_name=tup[6]
    
    print('TSA Claims Data: 2002 - 2009 \n')

    print('N = {:<10,d}".format(total)\n')
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ",'2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009'))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Total",list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Settled",list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7]))
    print("{:<8s}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}{:>8,d}".format("Denied",list3[0],list3[1],list3[2],list3[3],list3[4],list3[5],list3[6],list3[7]))
    print('')
    print("Average settlement: ${:<10,.2f}".format(average))
    print("The maximum claim was ${:,.2f}".format(max_claim)+" at "+max_name+" Airport")
    
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
    opened_file = open_file()
    data = read_file(opened_file) 
    tup = process(data) 
    display_data(tup)
    a = input('Do you want to plot?')
    if a == 'yes':
        plot_data(tup[0],tup[1],tup[2])

if __name__ == "__main__":
    main()