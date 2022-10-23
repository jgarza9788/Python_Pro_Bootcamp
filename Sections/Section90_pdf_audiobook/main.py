#https://www.geeksforgeeks.org/convert-text-speech-python/


import os

# import pdftotext
import PyPDF2 
# import pdf2text
from gtts import gTTS


DIR = os.path.dirname(os.path.abspath(__file__))


def main(pdf_path=None,language="en",save_path=None,save_text =True):

    if pdf_path == None:
        print('you need to provide a pdf file')
    
    if os.path.exists(pdf_path) == False:
        print('unable to find the pdf file')
    
    if save_path == None:
        n = pdf_path.split('\\')[-1] + '.mp3'
        save_path = os.path.join(DIR,n)
        print('save_path was None, your file will be saved to:\n',save_path)

    # pdf_text = ''
    # with open(pdf_path,'rb') as pdf:
    #     pdf_text = pdftotext.PDF(pdf,"secret")
    # pdf_text = " ".join(pdf_text)
    # print(pdf_text)
    
    pdf_text = ''
    with open(pdf_path, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        for i in range(pdf_reader.numPages):
            pdf_text += pdf_reader.getPage(i).extractText()
    # print(pdf_text)

    if save_text:
        n = pdf_path.split('\\')[-1] + '.txt'
        n = os.path.join(DIR,n)
        with open(n, 'w',encoding='utf-8') as txt:
            txt.write(pdf_text)
            print('file saved:',n)

    
    #known error ... large pdf will cause an API error 
    # >> gtts.tts.gTTSError: 429 (Too Many Requests) from TTS API. Probable cause: Unknown
    audio = gTTS(text=pdf_text, lang=language, slow=False)
    audio.save(save_path)
    print('file saved:', save_path)



if __name__ == '__main__':
    # pdf = os.path.join(DIR,'The_Fourth_Turning_1997.pdf')
    pdf = os.path.join(DIR,'Brave_New_World_Aldous_Huxley.pdf')
    main(pdf_path=pdf)

