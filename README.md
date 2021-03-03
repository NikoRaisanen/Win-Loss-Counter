# Win-Loss-Counter
### Why was this project created?
Python application for keep track of your win/loss ratio. This project was created because manually going into OBS settings and changing the win/loss record is far too time consuming, especially with the abundance of distractions that come with streaming.


### How does it work?
The application changes the contents of the "record.txt" file based on user input and resets when the program is restarted. This tool can be leveraged by content creators to include a visible win/loss record on their stream by pointing to "record.txt."

![](winlossPOC.gif)

Notice how the Record on the right side of the screen is dynamically updated, eliminating the extra keystrokes needed to update the file manually.


### How do I use this program?
1.) Download a recent version of Python (3.1+) from https://www.python.org/downloads/

2.) Download the WinLoss.pyw file

3.) Double click the WinLoss.pyw file and click a few buttons (this will create the record.txt file)

4.) Open OBS and create a new "Text (GDI+)" source and point it to record.txt
