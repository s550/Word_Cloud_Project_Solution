!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():
    
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
   
    # A list of punctuations and commonly used words to process the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Dictionary for storing the individual words and their counts
    word_count = {}
    
    # case insensitive list of words from the file contents.
    word_list = file_contents.lower().split(" ")
    clean_list =[]
    
    # loops through the list of words filtering out words without punctuation attached
    # adding them to the clean list as well as stripping punctuation from left over 
    # words and adding them to the list
    for word in word_list:
        if word.isalpha():
            clean_list.append(word)
        else:
            for char in punctuations:
                if word.find(char) >= 0:
                    clean_list.append(word.replace(char,""))
    
    # Checks the clean list for any words that got past the first filter such as
    # numbers and commonly used words and removes them. 
    for word in clean_list:
        if word.isnumeric():
            clean_list.remove(word)
        elif word in uninteresting_words:
            while word in clean_list:
                clean_list.remove(word)
    
    # Counts word occurences in the cleaned list and adds them to the word count
    # dictionary 
    for word in clean_list:
        count = clean_list.count(word)
        if word in word_count.keys():
            continue
        else:
            word_count.update({word:count})
    
    # Generates word cloud from the word_count dictionary 
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    return cloud.to_array()

# Creates the word cloud image 
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
 
 
 
 
 
 
 
 
 
 
 
 word_count = {}
    word_list = file_contents['text'].lower().split(" ")
    clean_list = []
    
    for word in word_list:
      if word.isalpha():
        clean_list.append(word)
      else:
        for char in punctuations:
          if word.find(char) >= 0:
            clean_list.append(word.replace(char,""))
    
    for word in clean_list: 
      if word.isnumeric():
        clean_list.remove(word)
      elif word in uninteresting_words:
        while word in clean_list:
          clean_list.remove(word)
    
    # print(clean_list)
    
    for word in clean_list:
      count = clean_list.count(word)
      if word in word_count.keys():
        continue
      else:
        word_count.update({word : count})
        
        
    print(word_count)