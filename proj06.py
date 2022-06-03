###############################################################################
#   Project 6
#
# First I use open_file to open the file, and try-except to check error
#   Then I use if-else to define find_index, if not in list, return None
#     I return the value we need by calculating 2016 population.
#      After that, I calculate them based on those values,
#       I've listed four values in 2000 function, and return them
#        in main(), I print out the result and call plot_data
#          Finally, I use if!= no to check that he wants plot.
#         
###############################################################################   

import pylab   # for plotting
from operator import itemgetter  # useful for sorting

def open_file():
    '''
    
    '''
    while True:# input document
        file_name = input("Enter a file name: ")
        try:
            fp = open(file_name,"r")
            return fp#read document
        except: #check error
            print("Error. Please try again.")
            file_name = input("Enter a file name: ")
            fp = open(file_name,"r")

def find_index(header_lst,s):

    if s in header_lst:
        return header_lst.index(s)
    else:
        return None

def read_2016_file(fp):

    with fp as f:
        header = fp.readline()
        header_lst = header.split(",")
        name_lst = ["EST_VC197","EST_VC201","EST_VC211"]
        col_lst = [find_index(header_lst,col) for col in name_lst]
        
        next(f)
        lst = []
        for line in f:
            line_lst = line.split(",")
            value_lst = [int(line_lst[col]) for col in col_lst]
            lst.append([line_lst[2],value_lst])
       
        o_lst = []
        for value_lst in lst:
            v1,v2,v3 = value_lst[1]
            total_123 = sum(value_lst[1])
            t_2 = v2 / total_123
            t_3 = v3 / total_123
            o_lst.append((value_lst[0],v1,v2,t_2,v3,t_3))
    return sorted(o_lst,key=itemgetter(5))

def read_2000_file(fp2):
    
    lines=fp2.readlines()
    total_pop=int(lines[2].split(",")[find_index(lines[0].split(","),"HC01_VC02")])
    #total population
    nb=int(lines[2].split(",")[find_index(lines[0].split(","),"HC01_VC03")])
    #native-born
    nz=int(lines[2].split(",")[find_index(lines[0].split(","),"HC01_VC05")])
    #naturalized citizens
    nc=int(lines[2].split(",")[find_index(lines[0].split(","),"HC01_VC06")])
    #noncitizens
    return total_pop,nb,nz,nc

def calc_totals(data_sorted):
    totals_lst = [[],[],[]]
    for d in data_sorted:
        totals_lst[0].append(d[1])
        totals_lst[1].append(d[2])
        totals_lst[2].append(d[4])
    cal_sum_lst = [sum(list) for list in totals_lst]
    result_2 = tuple(cal_sum_lst) + tuple([sum(cal_sum_lst)])
    return result_2

def make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016):

    return tuple([[native_2000,native_2016],[naturalized_2000,naturalized_2016],[non_citizen_2000,non_citizen_2016]])
    
def plot_data(native_list, naturalized_list, non_citizen_list):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(2)   # create 2 containers to hold the data for graphing
    # assign each list's values to the 3 items to be graphed, include a color and a label
    pylab.bar(X, native_list, color = 'b', width = 0.25, label="native")
    pylab.bar(X + 0.25, naturalized_list, color = 'g', width = 0.25, label="naturalized")
    pylab.bar(X + 0.50, non_citizen_list, color = 'r', width = 0.25,label="non-citizen")

    pylab.title("US Population")
    # label the y axis
    pylab.ylabel('Population (hundred millions)')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2000","2016"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    #pylab.savefig("plot.png")

def main():    
    '''Insert DocString here.'''
    fp = open_file()
    fp1 = read_2016_file(fp)
    fp2 = open_file()
    print("2016 Population: Native, Naturalized, Non-Citizen")
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("State","Native","Naturalized","Percent Naturalized", "Non-Citizen","Percent Non-Citizen"))
    
    for l in fp1:
        print("{:<20s}{:>15,d}{:>17,d}".format(l[0],l[1],l[2]),end='')
        print("{:>21.1f}%".format(l[3]*100), end='')
        print("{:>16,d}".format(l[4]), end='')
        print("{:>21.1f}%".format(l[5]*100))
    
    t1 = calc_totals(fp1)
    t2 = read_2000_file(fp2)
   
    print("="*112)
    print("{:<20s}{:>15,d}{:>17,d}".format("Total 2016",t1[0],t1[1]),end='')
    print("{:>21.1f}%".format(t1[1]/t1[3]*100), end='')
    print("{:>16,d}".format(t1[2]), end='')
    print("{:>21.1f}%".format(t1[2]*100/t1[3]))
    print("{:<20s}{:>15,d}{:>17,d}".format("Total 2000",t2[1],t2[2]),end='')
    print("{:>21.1f}%".format(t2[2]*100/t2[0]), end='')
    print("{:>16,d}".format(t2[3]), end='')
    print("{:>21.1f}%".format(t2[3]*100/t2[0]))
    
    if input("Do you want to plot? ").lower() != 'no':
        l = make_lists_for_plot(t2[1],t2[2],t2[3],t1[0],t1[1],t1[2])
        plot_data(l[0],l[1],l[2])

    
if __name__ == "__main__":
    main()
