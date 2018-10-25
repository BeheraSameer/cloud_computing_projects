
class CompletionTime:
    def __init__(self, completionTime, machine):
        self.completionTime=completionTime
        self.machine=machine

def get_min_comp_machine(task, cluster):
    if task.get_started_time() == -1:
        min_comp_machine = None
        min_comp_time = 0
        for machine in cluster:
            ready_time = machine.get_ready_time(task)
            if min_comp_machine is None and ready_time is not None:
                min_comp_machine = machine
                min_comp_time = ready_time + task.pred_exec_time
            elif ready_time is not None:
                comp_time = ready_time + task.pred_exec_time
                if comp_time < min_comp_time:
                    min_comp_machine = machine
                    min_comp_time = comp_time

    return min_comp_time, min_comp_machine

def schedule_task_MCT(task_cue,global_timer,cluster):

    num_unschedule_task = len(task_cue)
    unschedule_tasks = task_cue
    cant_schedule = 0
    cant_schedule_ids = []
    while (num_unschedule_task - cant_schedule) != 0:
        task_min_comp = {}
        unschedule_tasks = [ task for task in unschedule_tasks if (task.scheduled == False and task.id not in cant_schedule_ids) ]
        for unschedule_task in unschedule_tasks:

            min_comp_time, min_comp_machine = get_min_comp_machine(unschedule_task, cluster)
            task_min_comp[unschedule_task.id] = (min_comp_time, min_comp_machine)

        task_min_comp_tuples = list(task_min_comp.items())
        task_min_comp_tuples.sort(key=lambda x:x[1][0])
        task_p_id = task_min_comp_tuples[0][0]
        machine = task_min_comp_tuples[0][1][1]
        task_to_schedule = None
        for task in unschedule_tasks:
            if task.id == task_p_id:
                task_to_schedule = task
                break
        if machine.check_mem_available() >= task_to_schedule.get_mem_requested() and \
                        machine.check_cpu_available() >= task_to_schedule.get_cpu_requested():
            machine.allocate_mem(task_to_schedule.get_mem_requested())
            machine.allocate_cpu(task_to_schedule.get_cpu_requested())
            task_to_schedule.update_started_time(global_timer)
            task_to_schedule.update_remaining_time()
            task_to_schedule.scheduled = True
            num_unschedule_task -= 1
            machine.add_task(task_to_schedule)
        else:
            cant_schedule += 1
            cant_schedule_ids.append(task_to_schedule.id)

