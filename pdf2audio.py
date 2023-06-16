import pyttsx3
import PyPDF2


# change the code above so that I can puase and unpause the audio and adjust the reeading speed
def pdf2audio2(pdf_file, start_page, speed=150):
    # open the pdf file
    book = open(pdf_file, 'rb')
    # create a pdf reader object
    pdfReader = PyPDF2.PdfReader(book)
    # get the number of pages
    pages = len(pdfReader.pages)
    # create a speaker object
    speaker = pyttsx3.init()

    # configure the speaker speed
    speaker.setProperty('rate', speed)

    # create a global variable to store the current playback state
    global paused
    paused = False

    # loop through all the pages and convert them to audio
    for num in range(start_page, pages):
        page = pdfReader.pages[num]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

    # create a function to handle the spacebar key press
    def on_spacebar_pressed():
        # if the spacebar is pressed, toggle the playback state
        global paused
        if paused:
            speaker.resume()
            paused = False
        else:
            speaker.pause()
            paused = True

    # create a keyboard listener object
    listener = pyttsx3.KbdListener()

    # add a listener for the spacebar key
    listener.add_handler(on_spacebar_pressed)

    # start listening for key presses
    listener.start()

    # play the audio
    speaker.resume()


# call the pdf2audio function
pdf2audio2(
    "D:\Lester\Practice\Books\Python\OOP\Dusty Phillips - Python 3 Object-Oriented Programming - (2018) - libgen.li.pdf",
    183)
