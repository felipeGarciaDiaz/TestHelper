import wikipedia
import time
from docx import Document


def run():
    
    doc = Document()
    doc.add_heading("Study Sheet",0)

    studyFile = input("What file would you like to use? >>")
    outputFile=input("Where would you like to save the file >>")
    num = input("Sentences to parse? >>")
    verboseMode = input("Would you like to use verbose mode? [Y/N]>>").lower()
    studyMat = open(studyFile).readlines()
    
    for i in range(len(studyMat)):
        
        try:

            if verboseMode == "y" or None:
                
                print(studyMat[i] + "\n" + wikipedia.summary(studyMat[i], sentences=num))

            else:
                
                pass

            doc.add_heading(studyMat[i], level=1)
            desc = doc.add_paragraph(wikipedia.summary(studyMat[i], sentences=num))
            time.sleep(5)

        except:

            print("There was an error reading " + studyMat[i] + " Ignoring for now")
            pass

    doc.add_page_break()
    doc.save(outputFile)

if __name__ == "__main__":
    
    run()