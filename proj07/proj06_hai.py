###########################################################
#  Computer Project #6
#
#  Algorithm
#    open 2016 file
#    open 2010 file
#    print headers
#    process 2016 data
#    process 2000 data
#	 for loop:
#		print formated lines in 2016 data
#	 print '-------'
#	 calculate total of 2016 data
#	 calculate percentage and print out formated 2016 total
#	 calculate percentage and print out formated 2000 total
#	 ask user if plot, if yes then
#		 convert 2010 and 2016 total to plot format
#		 call plot function to plot 
###########################################################
	
import pylab   # for plotting
from operator import itemgetter  # useful for sorting

def open_file():
    '''
	This function asks user for filename, opens it and return the file pointer. 
	Error will be raised if file can not be found and keep asking until find.
	'''
    file_name = input("Enter a file name: ")
    while True:
        try: #try to open a file
            file = open(file_name,"r")
            return file
        except: # raise error if can not find the file
            print('Error.')
            file_name = input("Enter a file name: ")

def find_index(header_lst,s):
    '''
	This function takes a list and a string, find index of the string in the list and return it.
	Return None if can not find.
	'''
    if s not in header_lst: # check if the string is in the list
        return None
    else:
        idx = header_lst.index(s)
        return idx

def read_2016_file(fp):
    '''
	Input 2016 file pointer, process, sort then output a list or tuples.
	'''
    c=0
    lst = []
    for i in fp:
        if c ==0:
			# use the first row to find index of those values
            pos1 = find_index(i.split(','),'EST_VC197') 
            pos2 = find_index(i.split(','),'EST_VC201')
            pos3 = find_index(i.split(','),'EST_VC211')
        if c >=2:
			#ignore the second row, find all three values by previous indexes
            line_list = i.split(',')
            name = line_list[2]
            citizen = int(line_list[int(pos1)])
            nature = int(line_list[int(pos2)])
            non = int(line_list[int(pos3)])
			#calculate the two percent by previous found three values
            perc_nature = nature/(citizen+nature+non)
            perc_non = non/(citizen+nature+non)
            lst.append( (name,citizen,nature,perc_nature,non,perc_non) )
        c+=1 #update c
    lst.sort(key=itemgetter(-1)) # sort lst by last item in tuples
    return lst

	
def read_2000_file(fp2):
    '''
	Input 2000 file pointer, process then output a tuple.
	'''
    c=0
    for i in fp2:
        if c ==0:
			# use the first row to find index of those information
            line1 = i
            pos1 = find_index(line1.split(','),'HC01_VC02')
            pos2 = find_index(line1.split(','),'HC01_VC03')
            pos3 = find_index(line1.split(','),'HC01_VC05')
            pos4 = find_index(line1.split(','),'HC01_VC06')
        if c ==2:
			#ignore the second row, find all four values by previous indexes
            line3 = i
            line_list = line3.split(',')
            total = int(line_list[int(pos1)])
            citizen = int(line_list[int(pos2)])
            nature = int(line_list[int(pos3)])
            non = int(line_list[int(pos4)])
            return ((total,citizen,nature,non)) # return a tuple of the four values
        c+=1
                            
            
def calc_totals(data_sorted):
    '''
	Input the output of function read_2016_file then output a calculated total in form of list
	'''
    result = [0,0,0] #initialize a list with all zeros
    for d in data_sorted:
		# add all the values under three conditions
        result[0] += d[1]
        result[1] += d[2]
        result[2] += d[4]
    
    total = result[0] + result[1] + result[2] #calculate total
    result.append(total) # append total to the list
    result = tuple(result) # convert to tuple
    return result
           

def make_lists_for_plot(native_2000,naturalized_2000,non_citizen_2000,native_2016,naturalized_2016,non_citizen_2016):
    '''
	Take 6 values then output in form of tuple of lists
	'''
    output = ([native_2000,native_2016],[naturalized_2000,naturalized_2016],[non_citizen_2000,non_citizen_2016])
    return output

    
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
    '''
	Organize all functions to print desired form
	'''
    file = open_file() # open 2016 file
    file2 = open_file() # open 2000 file
    #file = open('ACS_16_1YR_S0201_with_ann.csv')
    #file2 = open('DEC_00_SF4_QTP14_with_ann.csv')
	
	# print head and title
    title = "2016 Population: Native, Naturalized, Non-Citizen"
    header = "{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("State","Native","Naturalized","Percent Naturalized", "Non-Citizen","Percent Non-Citizen")
    print(title)
    print(header)
    
	

    content_of_table = read_2016_file(file) #    process 2016 data
    content_of_2000 = read_2000_file(file2) #    process 2000 data

    for i in content_of_table:
        l = "{:<20s}{:>15,d}{:>17,d}{:>21.1f}%{:>16,d}{:>21.1f}%".format(i[0],i[1],i[2],i[3]*100,i[4],i[5]*100) 
        print(l) # print formated lines in 2016 data


    print("-"*112)


    total_16 = calc_totals(content_of_table) #calculate total of 2016 data
	#calculate nature and non of 2016 
    perc_nature_16 = total_16[1]/total_16[3] 
    perc_non_16 = total_16[2]/total_16[3] 

    line = "{:<20s}{:>15,d}{:>17,d}{:>21.1f}%{:>16,d}{:>21.1f}%".format('Total 2016',total_16[0],total_16[1],perc_nature_16*100,total_16[2],perc_non_16*100) # format line
    print(line)

	#calculate nature and non of 2000 
    perc_nature_00 = content_of_2000[1]/content_of_2000[0] 
    perc_non_00 = content_of_2000[3]/content_of_2000[0]
    line = "{:<20s}{:>15,d}{:>17,d}{:>21.1f}%{:>16,d}{:>21.1f}%".format('Total 2000',content_of_2000[1],content_of_2000[2],perc_nature_00*100,content_of_2000[3],perc_non_00*100) # format line
    print(line)

    a = input('Do you want to plot?')
    if a == 'yes':
        for_plot = make_lists_for_plot(content_of_2000[1],content_of_2000[2],content_of_2000[3],content_of_table[0],content_of_table[1],content_of_table[2]) # make data for plot
        
        plot_data(for_plot[0],for_plot[1],for_plot[2])
        
        







    
    
    
    

    
    
    
if __name__ == "__main__":
    main()
