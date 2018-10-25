from models.machine import *
from models.task import *

def cluster_init():
    # id, max_cpu_cores, max_mem
    cluster=[]
    cluster.append(Machine(1,6,50))
    cluster.append(Machine(2,4,25))
    cluster.append(Machine(3,2,15))
    cluster.append(Machine(4,2,15))
    cluster.append(Machine(5,4,50))
    cluster.append(Machine(6,2,15))

    return cluster
def task_list_init():
    #id, arrival_time, priority, cpu_requested, mem_requested,pred_exec_time
    task_list=[]
    task_list.append(Task(1, 0, 0, 1, 50, 6))
    task_list.append(Task(2, 0, 1, 1, 6, 8))
    task_list.append(Task(3, 1, 2, 1, 20, 10))
    task_list.append(Task(4, 4, 2, 1, 3, 10))
    task_list.append(Task(5, 6, 1, 1, 6, 7))
    task_list.append(Task(6, 6, 0, 1, 10, 4))

    return task_list

def update_machine(machine_x, finished_tasks, global_timer):
    if machine_x.get_current_tasks() != []:
        temp_array_of_tasks= machine_x.get_current_tasks()
        for y in range(len(temp_array_of_tasks)):
            if temp_array_of_tasks[y].get_remaining_time()== 0:
                if temp_array_of_tasks[y].get_status() == False:
                    machine_x.deallocate_mem(temp_array_of_tasks[y].get_mem_requested())
                    machine_x.deallocate_cpu(temp_array_of_tasks[y].get_cpu_requested())
                    temp_array_of_tasks[y].update_to_finished(global_timer)
                    finished_tasks.append(temp_array_of_tasks[y])
                    machine_x.number_of_finished += 1
            else:
                temp_array_of_tasks[y].update_remaining_time()
                temp_array_of_tasks[y].update_time_run()

    machine_x.current_tasks = [ task for task in machine_x.current_tasks
                                if task.get_status() == False ]

def update_machine_RR(machine_x, finished_tasks, task_cue, global_timer):
    quanta = 15
    if machine_x.get_current_tasks() != []:
        temp_array_of_tasks = machine_x.get_current_tasks()
        for y in range(len(temp_array_of_tasks)):
            if temp_array_of_tasks[y].get_remaining_time() == 0 and \
                temp_array_of_tasks[y].get_status() == False:
                # if not finished but there is no remaining time, update to finished
                machine_x.deallocate_mem(temp_array_of_tasks[y].get_mem_requested())
                machine_x.deallocate_cpu(temp_array_of_tasks[y].get_cpu_requested())
                temp_array_of_tasks[y].update_to_finished(global_timer)
                finished_tasks.append(temp_array_of_tasks[y])
                machine_x.number_of_finished += 1
            elif temp_array_of_tasks[y].get_time_run() == quanta:
                machine_x.deallocate_mem(temp_array_of_tasks[y].get_mem_requested())
                machine_x.deallocate_cpu(temp_array_of_tasks[y].get_cpu_requested())
                temp_array_of_tasks[y].reset_time_run()
                temp_array_of_tasks[y].update_to_started_false()
                task_cue.append(temp_array_of_tasks[y])
            else:
                #if time is not up and not finished update remaining time and time run
                temp_array_of_tasks[y].update_remaining_time()
                temp_array_of_tasks[y].update_time_run()
        machine_x.current_tasks = [ task for task in machine_x.current_tasks
                                    if task.get_started() == True and task.get_status() == False ]
    else:
        pass