def schedule_task_RR(task_cue,global_timer,cluster):

    for x in range(len(task_cue)):
        if task_cue[x].get_started() == False:
            #if task is not started
            for i in range(len(cluster)):
                #go through every machine
                if cluster[i].check_mem_available() >= task_cue[x].get_mem_requested():
                    if cluster[i].check_cpu_available() >= task_cue[x].get_cpu_requested():
                        cluster[i].allocate_mem(task_cue[x].get_mem_requested())
                        cluster[i].allocate_cpu(task_cue[x].get_cpu_requested())
                        cluster[i].add_task(task_cue[x])
                        if task_cue[x].started_time == -1:
                            task_cue[x].update_started_time(global_timer)
                        task_cue[x].update_remaining_time()
                        task_cue[x].update_time_run()
                        task_cue[x].update_to_started()
                        break