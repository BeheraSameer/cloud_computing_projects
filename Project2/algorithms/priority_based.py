import operator

def schedule_task_PJS(task_cue,global_timer,cluster):
    task_cue = sorted(task_cue, key=operator.attrgetter('priority'), reverse=True)
    for x in range(len(task_cue)):
        if task_cue[x].get_started_time() == -1:
            for i in range(len(cluster)):
                if cluster[i].check_mem_available() >= task_cue[x].get_mem_requested():
                    if cluster[i].check_cpu_available() >= task_cue[x].get_cpu_requested():
                        cluster[i].allocate_mem(task_cue[x].get_mem_requested())
                        cluster[i].allocate_cpu(task_cue[x].get_cpu_requested())
                        cluster[i].add_task(task_cue[x])
                        task_cue[x].update_started_time(global_timer)
                        task_cue[x].update_remaining_time()
                        break
    #print("Finished going over received tasks")