import pyttsx3    # Importing modules
import PyPDF2
book = open('OOP.pdf', 'rb')    # open a pdf file/ path of the pdf file
pdfReader = PyPDF2.PdfFileReader(book)     # creating an object PdfFileReader
pages = pdfReader.numPages         # get total no of pages
print(pages)
speaker = pyttsx3.init()
for num in range(6, pages):
    page = pdfReader.getPage(num)    # select the page to be read
    text = page.extractText()     # extract the text from the page
    speaker.say(text)             # reading the text
    speaker.runAndWait()
