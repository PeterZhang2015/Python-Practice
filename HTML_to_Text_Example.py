import html2text
import os

#filename="MME-1_MME_AUT_Testing.fftc.html"
#folder= "C:\Users\Peter Zhang\Downloads"
#html_file = open(os.path.join(folder, filename), "r")
filename="C:\Users\Peter Zhang\Downloads\MME-1_MME_AUT_Testing.fftc.html"
html_file = open(filename, "r")

f = html_file.read()

text_file=html2text.html2text(f)
print text_file

w = open("C:\Users\Peter Zhang\Downloads\out.txt", "w")
w.write(html2text.html2text(f).encode('utf-8'))
html_file.close()
w.close()
html_file.close()