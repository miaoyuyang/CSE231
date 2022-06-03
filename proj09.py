###############################################################################
#   Project 09
#
# First I use open_file to open the file, and try-except to check error
#  then, read the file of stopword, I use 'replace' and lower() to add them to
#   a set. Next, I will check validata words, it will return True or False.
#    And, I will check lyrics, in this function, I need to check punctuation,
#     trans to lower, strip words, the result is return a set.
#      in read_data function, I will get a dic, it contain singer, song name, 
#       and words. I use if-not in to check, if they not in dic, I will creat
#        a new one. If singer not in dic, the song_name also not in dic.
#         later, I updata this dic's data in updata_dictionary this function.
#          then, I will cal the number of average words, I use for loop to get
#           the length of number of songs and words. And I divide the two and 
#            get the average. Also, I use for loop to get the words of all the 
#             songs of a singer, it will return a dic. Later, I print out the
#               firts ten from big to small. And in next function, I will get
#                a plot about the number of song and vocbulary size. I creat a
#                 function make_data_plot, the purpose is help to draw the plot
#                   In the func of research_song, I will get a list, through
#                    words, I will get the singer and song name. Last one, its
#                     main(), I will check if file can find, and ask the user
#                       if they want a plot, and search kyrics by words, it'll 
#                        print the first five's singer and song name. If the
#                         user input 'enter', it will done.
############################################################################### 
import csv
import string
import pylab
from operator import itemgetter

def open_file(message):
    '''
    This function is asked user to enter filename, open and return the file. 
    If the file is not found, return 'error'.
    '''
    try:
        fp = open(message,"r") # open the file
        return fp 
    except: #check if can not find the file    
        return 'error'

def read_stopwords(fp_sw):
    '''
    This function is to read the file of stopwords, and return a set. I will 
    use replace to delete blank and convert all words to lowercase.
    '''
    set_words = set() # set a 'set', it doesn't have duplicate data
    for i in fp_sw:
        # transfer to lower word, and use''to replace the enter
        set_words.add(i.replace('\n','').lower())
    return set_words

def validate_word(word, stopwords):
    '''
    This function is to check validata words, and return True/False.
    If the word in the file(stopwords.txt) and they are not a alpha, it will
    return False. Else, it will return True.
    '''
    if ( word in stopwords ) or ( not word.isalpha() ):
        # check if word in stopwords or words are not alpha, it will False
        return False
    else:
        # else, the result is True
        return True 

def process_lyrics(lyrics, stopwords):
    '''
    This function is receive a string and return a set. In this function, I
    need to transfer all words to lower, and delete the punction, use black to
    strip all words.
    '''
    set_process = set() # set a 'set'
    lst = lyrics.split() 
    for word in lst:
        word = word.lower() #transfer to lower words
        word = word.strip() #use black to strip the words
        word = word.strip(string.punctuation) # check the punctuation
        if validate_word(word,stopwords) == True:
            set_process.add(word) #add words into the set
    return set_process
        
def read_data(fp, stopwords):
    '''
    This function will collate the song data, and it will return a dic. This 
    dictionary is made up of two dictionaries, the outermost key is 'singer', 
    the second key is the name_song, and the value is a set about words.
    '''
    dt = {}
    reader = csv.reader(fp) #read the file
    next(reader) #skip the first line
    for row in reader: # row is a list, i.e. you do not need split()
        singer = row[0]
        song_name = row[1]
        lyrics = row[2]
        #if 'singer' not in dic, the song_name also not in dic.
        if singer not in dt:
            dt[singer] = {} # if singer not in, I will set a new dic.
            dt[singer][song_name] = process_lyrics(lyrics,stopwords)
        else: #if singer in dic, I will continue to check if song_name (not)in
            if song_name not in dt[singer]:
                #if song_name not in, I will set a new one.
                dt[singer][song_name] = process_lyrics(lyrics,stopwords)
    return dt

def update_dictionary(data_dict, singer, song, words):
    '''
    The purpose of this function is to update the dictionary. I will reveive 
    the last function.
    '''
    if singer not in data_dict: #check if singer not in dic
        data_dict[singer] = {} # if yes, I will set a new one.
        data_dict[singer][song] = words
    else:
        if song not in data_dict[singer]: #continue to check if song not in dic
            data_dict[singer][song] = words #if yes, add words.
        
def calculate_average_word_count(data_dict):
    '''
    In this function, I will calculate the average number of words per singer,
    and I will return a dic, the key is singer and value is average_number.
    '''
    dic_ave = {}
    lst = data_dict.items() #read the dic of data_dict
    for k,v in lst: # k is singer, v is song_name
        num_song = len(v) #get the number of song_name
        num_word = 0
        for v1 in v.values(): #v1 is words, v is song_name
            num_word += len(v1) 
        ave_word = num_word / num_song #average number = word / number of song
        dic_ave[k] = ave_word # make avrage number is this dic's value
    return dic_ave #return the dic

def find_singers_vocab(data_dict):
    '''
    I will receive the dic of data_dict, and I will return a dic, its key is 
    singer and value are all words. 
    '''
    dic_vocab = {} #set a dic
    for k,v in data_dict.items():#k is singer, v is song name
        dic_total_vocab = [] # set a list
        for v1 in v.values(): # v1 is words(song)
            dic_total_vocab.extend(list(v1)) #org singer's all words to a list
            dic_vocab[k] = set(dic_total_vocab) #use 'set' to remove duplicates
    return dic_vocab # return a dic
            

def display_singers(combined_list):
    '''
    This funciton for prints datas in the specified format. 
    I only need to print out the first ten, From the largest to the lowest.
    '''
    print("{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)
    
    combined_list.sort(key=itemgetter(1,3), reverse = True) 
    # sort them, from big to small
    for i in range(10): #get the first ten
        singer = combined_list[i][0] 
        awc = combined_list[i][1]
        vs = combined_list[i][2]
        nos =combined_list[i][3]
        print("{:<20s}{:>20.2f}{:>20d}{:>20d}".format(singer,awc,vs,nos) ) 


def vocab_average_plot(num_songs, vocab_counts):
    '''
    '''
    """
    Plot vocab. size vs number of songs graph
    num_songs: number of songs belong to singers (list)
    vocab_counts: vocabulary size of singers (list)
        
    """       
    pylab.scatter(num_songs, vocab_counts)
    pylab.ylabel('Vocabulary Size')
    pylab.xlabel('Number of Songs')
    pylab.title('Vocabulary Size vs Number of Songs')
    pylab.show()

def search_songs(data_dict, words):
    '''
    I will receive the dic of data_doc and words, and I will return a list.
    By searching the lyrics, I will get the singer and the title of the song 
    that contains the lyrics.
    '''
    search_lst = [] # set a list
    
    for k,v in data_dict.items(): # k is singer, v is song name
        for song,w in v.items(): #song is song name, w is words
            if words.issubset(w) == True: # if all words are in w
                search_lst.append( (k,song) ) 
                # singer and song name org to the tuple and than append to list
    search_lst.sort() # sort them
    return search_lst #return a list

def make_data_plot(all_data,vocab_size):
    '''
    This function is used to help draw the plot and it will return two list.
    '''
    num_songs = [] # this list about the number of songs
    vocab_sz = [] # set a list about vocabulary size
    for singer in all_data: 
        num_songs.append(len(all_data[singer])) 
        vocab_sz.append(len(vocab_size[singer]))
    return num_songs,vocab_sz
    
def check(x,stopwords):
    '''
    This function is check if all words are in stopwords, it will return F/T.
    '''
    results = [] # set a list about True or False
    for i in x:
        result = validate_word(i,stopwords)
        results.append(result) # append the result into list
    # if results had one false, the result false
    # if results had all True, the result is true
    if False in results:
        return False 
    if False not in results:
        return True

def main():
    '''
    Run the above function ,ask the user if they want plot data,and research 
    the words.
    '''
    
    while True: # open_file function 
        
        name_sw = input('Enter a filename for the stopwords: ')#input stopwords
        fp_sw = open_file(name_sw)
        if fp_sw == 'error':
            print("File is not found! Try Again!")
            continue # if cann't find the file, continue to ask
        else:
            break # if can find, continue to next while loop.
    while True: 
        name_song = input('Enter a filename for the song data: ')
        fp_song = open_file(name_song) #read the file of song data
        if fp_song == 'error': # if cann't find the file, continue to ask
            print("File is not found! Try Again!")
            continue
        else:
            break
#    fp_sw = open_file('stopwords.txt')
#    fp_song = open_file('songdata_small.csv')
        # call the above function
    set_words = read_stopwords(fp_sw)
    data = read_data(fp_song,set_words)
    avera = calculate_average_word_count(data)
    vocab = find_singers_vocab(data)
    combined_list=[]
    # this step is to set a combined_list, I will use it in display_ function
    for name in data.keys():
        awc = avera[name]
        nos = len(data[name]) # number of song
        vs = len(vocab[name])  # voca size
        combined_list.append((name,awc,vs,nos)) # orgazation them
    display_singers(combined_list) 
    
    # ask the user if they want to get plot
    if input('Do you want to plot (yes/no)?: ').lower() != 'no':
    # if the answer not is no, it will show the plot
        n_songs,vb_sz = make_data_plot(data,vocab)
        vocab_average_plot(n_songs, vb_sz)
    
    print("Search Lyrics by Words") #print the header
 
    while True: # ask the user which words they want to resarch
        words = input("Input a set of words (space separated), press enter to exit: ")
        words = words.lower() #tranfer them to lower
        if words != '': #if the input not a 'enter'
            x = set(words.split()) #use black to split them
            result = check(x,set_words) # run the function of check()
            if result == True: # if the reslut is true
                    y = search_songs(data, x) 
                    print("There are",len(y),"songs containing the given words!")
                    if len(y) >0:
                        print("{:<20s}{:<s}".format('Singer','Song'))
                        for song in y[:5]: # print the fist five
                            print("{:<20s}{:<s}".format(song[0], song[1]))
            else: #if the result is False
                print("Error in words!")
                print("1-) Words should not have any digit or punctuation")
                print("2-) Word list should not include any stop-word")
        else:
            break #end
            
if __name__ == '__main__':
    main()           
