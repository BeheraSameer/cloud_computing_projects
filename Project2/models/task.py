class Task:

    def __init__(self, id, arrival_time, priority, cpu_requested, mem_requested, pred_exec_time):
        self.id = id
        self.arrival_time = int(arrival_time)
        self.priority = priority
        self.cpu_requested = int(cpu_requested) if int(cpu_requested) > 0 else 1
        self.mem_requested = float(mem_requested)
        self.pred_exec_time = int(pred_exec_time)
        self.remaining_time= int(pred_exec_time)
        self.started_time=-1
        self.finished = False
        self.finished_time = 0
        self.started = False
        self.scheduled = False
        self.expected_start_time=-1
        self.time_run = 0
        # print("created Task ID:",self.id)

    def __str__(self):
        return "{ id: " + str(self.id) + ", \t" + \
               "arrival: " + str(self.arrival_time) + ", \t" + \
               "cpu_requested: " + str(self.cpu_requested) + ", \t" + \
               "mem_requested: " + str(self.mem_requested) + ", \t" + \
               "priority: " + str(self.priority) + ", \t" + \
               "pred_exec_time: " + str(self.pred_exec_time) + " }"

    def get_task_id(self):
        return self.id

    def get_cpu_requested(self):
        return self.cpu_requested

    def get_mem_requested(self):
        return self.mem_requested

    def get_pred_exec_time(self):
        return self.pred_exec_time

    def get_remaining_time(self):
        return self.remaining_time

    def get_status(self):
        return self.finished

    def get_started_time(self):
        return self.started_time

    def get_started(self):
        return self.started

    def get_time_run(self):
        return self.time_run

    def update_remaining_time(self):
        self.remaining_time = self.remaining_time - 1

    def update_started_time(self,time):
        self.started_time = time

    def update_arrival_time(self,new_arrival_time):
        self.arrival_time = new_arrival_time

    def update_to_finished(self, global_timer):
        self.finished = True
        self.finished_time = global_timer

    def update_to_started(self):
        self.started = True

    def update_to_started_false(self):
        self.started = False

    def update_time_run(self):
        self.time_run = self.time_run+1

    def update_pred_exec_time(self, time):
        self.pred_exec_time = time
        self.remaining_time = time

    def reset_time_run(self):
        self.time_run = 0


