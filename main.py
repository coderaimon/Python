# This project is for lazy persons who didn't read the book :)

# this tow pakages are must for running code
import pyttsx3 as pt
import PyPDF2 as pd

# Provided the location to to read pdf 
book = open('./book.pdf', 'rb')

# to read pdf 
reader = pd.PdfFileReader(book)

# to speak the text from pdf
speaker = pt.init()

# for declare the number of pages from book what you provided
pages = reader.numPages

# Provide the number of pages to red 
# Note that python is take range starts from 0 and declare it as 1
for num in range(0, pages):
    # to get page from pdf you provided
    page = reader.getPage(num)
    # extracting the the text from the pdf 
    text = page.extractText()
    # reading the page from pdf listen
    speaker.say(text)
    speaker.runAndWait()