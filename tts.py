import pyttsx3
import PyPDF2
book = open('The Elements of Statistical Learning_ Data Mining, Inference, and Prediction, Second Edition (Springer Series in Statistics) ( PDFDrive.com ).pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(2,pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
