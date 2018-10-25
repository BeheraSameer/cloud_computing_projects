import os
import operator
from models.machine import Machine
from models.task import Task
import csv
from constants import *
import copy

def get_google_cluster_machines():
    machine_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cleaned_data', 'machine_events', 'part-00000-of-00001.csv')
    #os.path.join(os.getcwd(), 'clusterdata-2011-2\machine_events\part-00000-of-00001.csv')

    #region Machine Attribute Indexes

    MACHINE_ID = 1
    EVENT_TYPE = 2
    CPU = 4
    MEMORY = 5

    #endregion

    list_of_machines = {}

    with open(machine_file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if int(row[EVENT_TYPE].strip()) == 0:
                if row[CPU].strip() and row[MEMORY].strip():
                    machine_id = row[MACHINE_ID].strip()
                    max_cpu_cores = float(row[CPU].strip()) * CPU_TRANSFORM_MULTIPLIER_VALUE # google nomalized the values so I am transforming it here so it make sense.
                    max_mem = float(row[MEMORY].strip()) * MEMORY_TRANSFORM_MULTIPLIER_VALUE # google nomalized the values so I am transforming it here so it make sense.
                    list_of_machines[machine_id] = Machine(machine_id, max_cpu_cores, max_mem)

    #print('Number of Machines: ' + str(len(list_of_machines)))
    list_of_machines = list(list_of_machines.values())
    list_of_machines = sorted(list_of_machines, key=operator.attrgetter('id'))
    return list_of_machines

def parse_google_cluster_tasks(num_of_files_to_parse):

    #region Task Attribute Indexes

    TIME = 0
    MISSING_INFO = 1
    JOB_ID = 2
    TASK_INDEX = 3
    EVENT_TYPE = 5
    PRIORITY = 8
    CPU_REQUEST = 9
    MEMORY_REQUEST = 10

    #endregion

    list_of_tasks = {}

    final_tasks = {}

    for i in range(num_of_files_to_parse):
        file_no = str(i).zfill(5)
        task_file_path = os.path.join(os.getcwd(), r'clusterdata-2011-2', 'task_events', 'part-' + file_no + '-of-00500.csv')
        #print('File: ' + str(i))
        with open(task_file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                missing_info = row[MISSING_INFO].strip()
                if missing_info == '':
                    event_type = row[EVENT_TYPE].strip()
                    time = int((int(row[TIME].strip())/1000000) - 600)
                    if time > 0: # ignore tasks before th 600 seconds start window.
                        job_id = row[JOB_ID].strip()
                        task_index = row[TASK_INDEX].strip()
                        priority = row[PRIORITY].strip()
                        cpu_requested = float(row[CPU_REQUEST].strip()) * CPU_TRANSFORM_MULTIPLIER_VALUE
                        memory_request = float(row[MEMORY_REQUEST].strip()) * MEMORY_TRANSFORM_MULTIPLIER_VALUE
                        task_id = job_id + '-' + task_index
                        pred_exec_time = 0
                        #print('Event type: ', event_type, 'Task id: ', task_id)
                        if int(event_type) == 0:  # when a task became available
                            list_of_tasks[task_id] = Task(task_id, time, priority, cpu_requested, memory_request, pred_exec_time)
                        elif int(event_type) == 1 and task_id in list_of_tasks:
                            list_of_tasks[task_id].pred_exec_time = time
                        elif int(event_type) == 4 and task_id in list_of_tasks:
                            final_tasks[task_id] = copy.copy(list_of_tasks[task_id])
                            final_tasks[task_id].update_pred_exec_time(time - list_of_tasks[task_id].pred_exec_time)
                            #pred_exec_time = time - list_of_tasks[task_id].pred_exec_time

    print('Total number of tasks parsed: ' + str(len(list_of_tasks)))
    print('Total number of tasks with time: ' + str(len(final_tasks)))

    file_path_to_store = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cleaned_data', 'task.csv')
    with open(file_path_to_store, 'w', newline='') as file:
        row_writer = csv.writer(file)
        for key, task in final_tasks.items():
            row_data = []
            row_data.append(task.id)
            row_data.append(task.arrival_time)
            row_data.append(task.priority)
            row_data.append(task.cpu_requested)
            row_data.append(task.mem_requested)
            row_data.append(task.pred_exec_time)
            row_writer.writerow(row_data)

    return True

def get_google_cluster_tasks():

    #region GOOGLE CLEANED TASK INDEXES

    TASK_ID = 0
    ARRIVAL_TIME = 1
    PRIORITY = 2
    CPU_REQUEST = 3
    MEMORY_REQUEST = 4
    PRED_EXEC_TIME = 5

    #endregion

    list_of_tasks = []

    file_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cleaned_data', 'task.csv')
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            task_id = row[TASK_ID].strip()
            arrival_time = row[ARRIVAL_TIME].strip()
            priority = row[PRIORITY].strip()
            cpu_requested = row[CPU_REQUEST].strip()
            mem_requested = row[MEMORY_REQUEST].strip()
            pred_exec_time = row[PRED_EXEC_TIME].strip()
            task = Task(task_id, arrival_time, priority, cpu_requested, mem_requested, pred_exec_time)
            list_of_tasks.append(task)

    list_of_tasks = sorted(list_of_tasks, key=operator.attrgetter('arrival_time'))

    #print('Total number of tasks: ' + str(len(list_of_tasks)))
    return list_of_tasks

