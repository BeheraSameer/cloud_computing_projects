Instructions for Task2:

For Details Kindly Read Task2 Report.docx

Instructions to Install MongoDB:
https://docs.mongodb.com/manual/administration/install-community/ 

Instructions to Install Redis:
Install Redis from: https://redis.io/download
Installing redis-py: $ sudo pip install redis

Instructions to Install Python
a. Install Python 2.7.13 from: https://www.python.org/downloads/ 
b. Run Python and Install pymongo from: http://api.mongodb.com/python/current/installation.html 

Command to Start Redis Server before Running Application
In Cloud9: $ sudo service redis-server start    (redis comes pre-installed in Cloud9)
In Ubuntu(Linux): redis-4.0.8/src/redis-server  (after installing redis-4.0.8 in Ubuntu)

Command to Run Application
$ python message_boards.py


The following instructions/operations are supported in the prototype:

(i) Select Message Board: select <board_name>
•	Here a User Selects a Message Board/Chat Channel.

(ii) Read: read
•	If No Board is Selected, then an Error Message is displayed.
•	If a Board is Selected, then a document with all messages in the board gets displayed in an array.

(iii) Write: write <message>
•	If No Board is Selected, then an Error Message is displayed.
•	If a Board is Selected, then either a new document (i.e. new board_name) gets created with the message stored in an array or an old document board (i.e. existing board_name) gets updated with the message appended to the existing array.
•	Also, on every successful insertion/updation of the document, a real-time message gets published in real-time to the subscribers, i.e. listeners of the board.

(iv) Listen to Updates: listen
•	If No Board is Selected, then an Error Message is displayed.
•	If a Board is Selected, then a User gets subscribed to the board and is ready to receive any real-time updates on the channel.

(v) Stop Listening to Updates: <Ctrl-C>
•	A User can come out of Listening Mode by Keyboard Interrupt <Ctrl-C>

(vi) Reset Application: reset
•	The board/channel gets reset, i.e. set to null

(vii) Clean Message Board/Clear RAM: flush
•	If No Board is Selected, then an Error Message is displayed.
•	If a Board is Selected, then on flush, the document of the selected board/channel with all its fields and records gets removed and also the RAM is cleared.

(viii) Quit Application: quit
•	The User Exits from the Application.



-Submitted By
Sameer Kumar Behera
CSE Dept, Texas A&M University
UIN: 526004296