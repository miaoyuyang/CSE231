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
    set_words = set()
    for i in fp_sw:
        set_words.add(i.replace('\n','').lower())
    return set_words

def validate_word(word, stopwords):
    '''
    This function is to check validata words, and return True/False.
    If the word in the file(stopwords.txt) and they are not a alpha, it will
    return False. Else, it will return True.
    '''
    if ( word in stopwords ) or ( not word.isalpha() ):
        return False
    else:
        return True 

def process_lyrics(lyrics, stopwords):
    '''
    This function is receive a string and return a set.
    '''
    set_process = set()
    lst = lyrics.split()
    for word in lst:
        word = word.lower()
        word = word.strip()
        word = word.strip(string.punctuation)
        if validate_word(word,stopwords) == True:
            set_process.add(word)
    return set_process
        
def read_data(fp, stopwords):
    '''
    '''
    dt = {}
    reader = csv.reader(fp)
    next(reader)
    for row in reader: # row is a list, i.e. you do not need split()
        singer = row[0]
        song_name = row[1]
        lyrics = row[2]
        if singer not in dt:
            dt[singer] = {}
            dt[singer][song_name] = process_lyrics(lyrics,stopwords)
        else:
            if song_name not in dt[singer]:
                dt[singer][song_name] = process_lyrics(lyrics,stopwords)
    return dt
        
    

def update_dictionary(data_dict, singer, song, words):
    if singer not in data_dict:
        data_dict[singer] = {}
        data_dict[singer][song] = words
    else:
        if song not in data_dict[singer]:
            data_dict[singer][song] = words             
        
def calculate_average_word_count(data_dict):
    dic_ave = {}
    lst = data_dict.items()
    for k,v in lst:
        num_song = len(v)
        num_word = 0
        for v1 in v.values():
            num_word += len(v1)
        ave_word = num_word / num_song
        dic_ave[k] = ave_word
    return dic_ave

def find_singers_vocab(data_dict):
    dic_vocab = {}
    for k,v in data_dict.items():
        dic_total_vocab = []
        for v1 in v.values():
            dic_total_vocab.extend(list(v1))
            dic_vocab[k] = set(dic_total_vocab)
    return dic_vocab
            

def display_singers(combined_list):
    print("{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)
    
    combined_list.sort(key=itemgetter(1,3), reverse = True)
    for i in range(10):
        singer = combined_list[i][0]
        awc = combined_list[i][1]
        vs = combined_list[i][2]
        nos =combined_list[i][3]
        print("{:<20s}{:>20.2f}{:>20d}{:>20d}".format(singer,awc,vs,nos) ) 


def vocab_average_plot(num_songs, vocab_counts):
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
    search_lst = []
    
    for k,v in data_dict.items():
        for song,w in v.items():
            if words.issubset(w) == True:
                search_lst.append( (k,song) ) 
    search_lst.sort()
    return search_lst

def make_data_plot(all_data,vocab_size):
    num_songs = []
    vocab_sz = []
    for singer in all_data:
        num_songs.append(len(all_data[singer]))
        vocab_sz.append(len(vocab_size[singer]))
    return num_songs,vocab_sz
    
def check(x,stopwords):
    results = []
    for i in x:
        result = validate_word(i,stopwords)
        results.append(result)
    # if results had one false, the result  false
    # if results had all True, the result is true
    if False in results:
        return False
    else:
        return True
    
    

def main():    

    while True:
        name_sw = input('Enter a filename for the stopwords: ')
        fp_sw = open_file(name_sw)
        if fp_sw == 'error':
            print("File is not found! Try Again!")
            continue
        else:
            break
    while True:
        name_song = input('Enter a filename for the song data: ')
        fp_song = open_file(name_song)
        if fp_song == 'error':
            print("File is not found! Try Again!")
            continue
        else:
            break
    # fp_sw = open_file('stopwords.txt')
    # fp_song = open_file('songdata_small.csv')
    set_words = read_stopwords(fp_sw)
    
    data = read_data(fp_song,set_words)
    avera = calculate_average_word_count(data)
    vocab = find_singers_vocab(data)
    combined_list=[]
    for name in data.keys():
        awc = avera[name]
        nos = len(data[name])
        vs = len(vocab[name])
        combined_list.append((name,awc,vs,nos))
    display_singers(combined_list)
    
#    ans = input('Do you want to plot (yes/no)?: ')
    if input('Do you want to plot (yes/no)?: ').lower() != 'no':
        n_songs,vb_sz = make_data_plot(data,vocab)
        vocab_average_plot(n_songs, vb_sz)
#        if input("Plot data (yes/no): ").lower() != 'no':
#        plot_data(tup[0],tup[1],tup[2])
    
    
    print("Search Lyrics by Words")
    
    while True:
        words = input("Input a set of words (space separated), press enter to exit: ")
        if words.lower() != '':
            x = set(words.split())
            result = check(x,set_words)
            if result == True:
                    y = search_songs(data, x)
                    print("There are",len(y),"songs containing the given words!")
                    if len(y) >0:
                        print("{:<20s}{:<s}".format('Singer','Song'))
                        for song in y[:5]:
                            print("{:<20s}{:<s}".format(song[0], song[1]))
            else:
                print("Error in words!")
                print("1-) Words should not have any digit or punctuation")
                print("2-) Word list should not include any stop-word")
        else:
            break
            
#        
#        
#        
#        
#        
#        y = search_songs(data, set(x))
#            
#        print("There are",len(y),"songs containing the given words!")
#        print("{:<20s}{:<s}".format('Singer','Song'))
#        for song in y[:5]:
#    #        words = input("Input a set of words (space separated), press enter to exit: ")
#    #        x = set(words.split())
#    #        y = search_songs(data, x)
##                    print("{:<20s}{:<s}".format('Singer','Song'))
#            print("{:<20s}{:<s}".format(song[0], song[1]))
#            continue
#    else:
#        print("Error in words!")
#        print("1-) Words should not have any digit or punctuation")
#        print("2-) Word list should not include any stop-word")
##        else:
#            break
                    
     
    #'Do you want to plot (yes/no)?: '

#    RULES = """1-) Words should not have any digit or punctuation
#2-) Word list should not include any stop-word"""
                
#    print("Search Lyrics by Words")
#    words = input("Input a set of words (space separated), press enter to exit: ")
    #'Error in words!'
    #"There are {} songs containing the given words!"
    #"{:<20s} {:<s}"

if __name__ == '__main__':
    main()           
