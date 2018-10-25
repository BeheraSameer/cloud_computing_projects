from algorithms.minimum_completion import *
from algorithms.first_come_first_serve import *
from algorithms.priority_based import *
from algorithms.round_robin import *
from simulator.helper_methods import *
from dataset_parser.parser import *
import sys


def main():
    if len(sys.argv) <  4 or len(sys.argv) > 4:
        print('INVALID COMMAND: please try again.')
        exit()

    ALGORITHM = sys.argv[1]

    if ALGORITHM not in ['MCT', 'FCFS', 'PJS', 'RR']:
        print('INVALID COMMAND: invalid algorithm name, must be MCT, FCFS, PJS, or RR')
        exit()

    cluster = get_google_cluster_machines()
    task_list = get_google_cluster_tasks()

    num_of_machines = int(sys.argv[2])
    num_of_tasks = int(sys.argv[3])

    if num_of_machines > len(cluster) or num_of_machines < 1 or \
        num_of_tasks > len(task_list) or num_of_tasks < 1:
        print('INVALID RANGE FOR TASK OR MACHINE.')
        exit()

    cluster = cluster[:num_of_machines]
    task_list = task_list[:num_of_tasks]

    print('Number of Machines: ' + str(num_of_machines))
    print('Number of Tasks: ' + str(num_of_tasks))
    task_cue = []
    global_timer = 0
    finished_tasks = []

    print('Running algorithm ' + ALGORITHM + '....... (This might take several minutes.)')
    while len(finished_tasks) != len(task_list):
        for i in range (len(cluster)):
            if ALGORITHM == 'RR':
                update_machine_RR(cluster[i], finished_tasks, task_cue, global_timer)
            else:
                update_machine(cluster[i], finished_tasks, global_timer) # update machines if task is finished
        for x in range(len(task_list)):
            if task_list[x].arrival_time == global_timer: # if a task arrives try to schedule it
                task_cue.append(task_list[x])
        if ALGORITHM == 'FCFS':
            schedule_task_FCFS(task_cue, global_timer, cluster)
        elif ALGORITHM == 'MCT':
            schedule_task_MCT(task_cue, global_timer, cluster)
        elif ALGORITHM == 'PJS':
            schedule_task_PJS(task_cue, global_timer, cluster)
        if ALGORITHM == 'RR':
            schedule_task_RR(task_cue, global_timer, cluster)

        if ALGORITHM == 'RR':
            new_task_cue = []
            for task in task_cue:
                if task.get_started() == False:
                    new_task_cue.append(task)
            task_cue = new_task_cue
        elif ALGORITHM == 'MCT':
            new_task_cue = []
            for task in task_cue:
                if task.scheduled == False:
                    new_task_cue.append(task)
            task_cue = new_task_cue
        else:
            new_task_cue = []
            for task in task_cue:
                if task.get_started_time() == -1:
                    new_task_cue.append(task)
            task_cue = new_task_cue
        global_timer = global_timer + 1
        if global_timer % 1000 == 0:
            print("Finished " + str(global_timer) + " iterations so far.")
            print("     Finished " + str(len(finished_tasks)) + " tasks so far.")

    print('Tasks finished by each Machine: ')
    machine_number = 1
    for machine in cluster:
        print('Machine #' + str(machine_number) + ', ' + str(machine.number_of_finished))
        machine_number += 1

    print("\n\nTotal iterations to finish all tasks: " + str(global_timer))
    timing_per_task = {}
    for task in finished_tasks:
        timing_per_task[task.id] = {}
        timing_per_task[task.id]['turnaround_time'] = task.finished_time - task.arrival_time
        timing_per_task[task.id]['wait_time'] = timing_per_task[task.id]['turnaround_time'] - task.pred_exec_time

    total_wait_time = 0
    total_turn_around_time = 0
    for task_id, timing in timing_per_task.items():
        total_wait_time += timing['wait_time']
        total_turn_around_time += timing['turnaround_time']

    print('Average turnaround time for a single task: ' + str(total_turn_around_time/ len(finished_tasks)))
    print('Average wait time for a single task: ' + str(total_wait_time/len(finished_tasks)))
    print('Average task completed per iter: ' + str(len(finished_tasks)/(global_timer +1)))

if __name__== "__main__":
    main()