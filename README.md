# PEEPER
![alt text](https://user-images.githubusercontent.com/73806121/132998784-8a2cafce-bb54-4a9d-adb0-fc5889c76454.png)

This tool is intended to assist investigators dealing with large volumes of screenshots or document images. The tool reads text from images found in the source directory and searches the text for terms or information deemed relevant by the user.  It then creates a report containing images found to contain text, the raw OCR data, word list hits, and a link to the image file. Support for JPEG and PNG files.

PEEPER makes use of the open-source Tesseract engine for optical character recognition (OCR) and requires the user install Tesseract prior to using PEEPER.

To download Tesseract you can click on the 'Get Tesseract' hyperlink on the PEEPER control panel. After installation, Tesseract [MUST BE ADDED TO PATH](https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82).

Word lists are located in the root of the program in a directory labeled "WORD LISTS". 

Each list is a text file that can be changed to meet the needs of the investigator. Each row is treated as a seperate search term. Please take steps to remove empty rows or un-needed spaces from the lists to avoid false positive responses.

One-time searches can also be performed through input window on the tool's UI.

The comparison between word lists and recovered text is not case sensitive.

This public release does not have the "Child Exploitation", "Narcotics", or "Personal Identifiers" modules enabled. If you are a law enforcement official, you may request access to a restricted version which activates the CSAM and Narcotic related word lists.  The Personal Identifiers module identifies credit card numbers, passport numbers, social security numbers, US phone numbers, e-mail addresses, and other PII data.  Requests for access may be submitted here: http://www.northloopconsulting.com/contact-us.html.  Requests should include an official agency e-mail address for the requestor.

The OCR process used in the tool is not perfect and can be impacted by picture quality, image rotation, or other factors. Please review all output for accuracy.

(c) 2021 North Loop Consulting, LLC  No warranty or gurantee provided for use of this tool.
