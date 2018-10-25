import operator

class Machine:

    def __init__(self, id, max_cpu_cores, max_mem):
        self.id = id
        self.max_cpu = int(max_cpu_cores) if int(max_cpu_cores) > 0 else 1
        self.max_mem = float(max_mem)
        self.in_use_mem = 0
        self.in_use_cpus = 0
        self.current_tasks = []
        self.scheduled_tasks = []
        self.number_of_finished = 0
        # print("created machine ID:",self.id)

    def __str__(self):
        return "{ id: " + str(self.id) + ", \t" + \
               "max_cpu: " + str(self.max_cpu) + ", \t" + \
               "max_mem: " + str(self.max_mem) + ", \t" + \
               "in_use_mem: " + str(self.in_use_mem) + ", \t" + \
               "in_use_cpus: " + str(self.in_use_cpus) + ", \t"

    def check_cpu_available(self):
        return self.max_cpu - self.in_use_cpus

    def check_mem_available(self):
        return self.max_mem - self.in_use_mem

    def check_num_curr_tasks(self):
        return len(self.current_tasks)

    def allocate_mem(self,num_mem):
        if self.check_mem_available() < num_mem:
            pass
        else:
            self.in_use_mem=self.in_use_mem+num_mem

    def deallocate_mem(self,num_mem):
        self.in_use_mem= self.in_use_mem-num_mem

    def allocate_cpu(self,num_cpu):
        if self.check_cpu_available() < num_cpu:
            pass
        else:
            self.in_use_cpus=self.in_use_cpus+num_cpu

    def get_ready_time(self, task):

        if self.max_mem < task.mem_requested or self.max_cpu < task.cpu_requested:
            return None

        if self.check_mem_available() >= task.get_mem_requested() and \
            self.check_cpu_available() >= task.get_cpu_requested():
                return 0
        if self.scheduled_tasks != []:
            x=0
        sorted_tasks = sorted(self.current_tasks, key=operator.attrgetter('remaining_time'))
        mem_will_be_free = 0
        cpu_will_be_free = 0
        ready_in = 0
        expec_start_time = 0
        for pending_task in sorted_tasks:
            mem_will_be_free += pending_task.mem_requested  # abs(self.max_mem - (self.in_use_mem - pending_task.mem_requested))
            cpu_will_be_free += pending_task.cpu_requested  # abs(self.max_cpu - (self.in_use_cpus - pending_task.cpu_requested))
            ready_in = max(ready_in, pending_task.remaining_time)
            if mem_will_be_free >= task.mem_requested and cpu_will_be_free >= task.cpu_requested:
                return ready_in + expec_start_time

        return ready_in

    def deallocate_cpu(self,num_cpu):
        self.in_use_cpus= self.in_use_cpus-num_cpu

    def clean_up(self):
        curr_tasks = []
        for task in self.current_tasks:
            if not task.finished:
                curr_tasks.append(task)
        self.current_tasks = curr_tasks

    def add_task(self,my_task):
        self.current_tasks.append(my_task)

    def get_current_tasks(self):
        return self.current_tasks

    def get_id(self):
        return self.id






