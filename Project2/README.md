<h1>Cloud Computing Project 2<h1>

<h2>Brief Description of Project:</h2>

Cloud technologies have marked a difference in the computing world.
We see how important the scheduling of computing resources is now, more than ever.
It has to be done efficiently to be able to not impact the applications hosted in the cloud.
Our project team will research, and analyze the different techniques and algorithms that are
proposed to solve the problem of task and resource scheduling in the cloud.


<h2>Members:</h2>

Johana Rueda UIN: 625007802 <br />
Denishkumar Patel UIN: 522001683 <br />
Sameer Kumar Behera UIN: 526004296 <br />
Vishakh Shukla UIN: 221004930 <br />

<h2>Requirements:</h2>

Python 3.4.3 (used for dev and testing, untested on other versions)

<h2>Instructions to run code:</h2>

- clone the project and retain the structure.
- download python https://www.python.org/downloads/release/python-343/
- instructions to set path on windows: https://docs.python.org/3/using/windows.html (if using windows to set the python path correctly.)
- navigate to root directory '689-18-a-P2'
- you might have to do export PYTHONPATH=. (if using linux to set the python path correctly.)
- it's important that you set the python path to the root of '689-18-a-P2' else the import statements will be out of sync.
- you must run code from 689-18-a-P2 directory and not any sub directory.
- the command to run is as follows:<br /><br />
        python simulator/run.py <algorithm_name> <number_of_machines> <number_of_tasks><br /><br />
        <algorithm_name> = RR (this is round robin), PJS (this is priority job), MCT (this is minimum completion time), FCFS (this is first come first serve)<br /><br />
        <number_of_machines> = this could be in the range 1 - 12555<br /><br />
        <number_of_tasks> = this could be in the range 1 - 116000<br /><br />
        example of command:<br /><br />
                python simulator/run.py FCFS 500 50000<br /><br />
                 - this command is for first come first serve for 500 machines and 50000 tasks.

<h2>DataSet:</h2> <br/>
Link: https://github.com/google/cluster-data

Tasks from the dataset are already passed and pushed with this repo inside of dataset_parser/cleaned_data/

if you want to parse more tasks that 116000 than there is s method inside of dataset_parser/cleaned_data/parser.py
'parse_google_cluster_tasks' which takes number of files as a arguments.

- you have to download the dataset from above link first and put it in the main directory '689-18-b'
- name the directory 'clusterdata-2011-2'
- make sure you have the following directories inside of 'clusterdata-2011-2':
    'machine_events', 'task_events'
- unzip all the file in that directory. (very important) do not change any names.
- now use a python interpretor and run parse_google_cluster_tasks(num_of_files)
    num_of_files can be 1 - 500.
- eveything will get parsed correctly and you will than just need to follow instructions to run main code.

<h2>Git flow:</h2>

When ready to make a pull request to these locally first:


- commit your changes on your branch first
- git checkout master
- git pull
- git checkout [your branch]
- git merge master
- git status (if any merge conflicts than go through each file and fix them) and commit them
- git push (git status should not have any uncommited changes at this point)
- make pull request

