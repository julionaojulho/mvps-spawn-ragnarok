# https://docs.python.org/3.5/library/datetime.html ler depois

# import string

class MvpView:
    def __init__(self,name):
        self.mvp = name

    def add_entry(self):
        """
        Ask user for input and store its values
        """
        mvp_name = self.mvp
        while mvp_name.lower() not in mvp_list:
            print("Mvp not found, please, write the name again.\n")
            mvp_name = input("Name: ")
        self.deathtime = input("Death time (hh:mm:ss): ")
        self.mvp.seconds = int(self.deathtime[-2:])
        self.mvp.minutes = int(self.deathtime[-5:-3])
        self.mvp.hours = int(self.deathtime[:-6])

    def next_on_list(self,mvp_time = []):
        """
        Print list of mvps in ascending respawn time order
        """
        self.queued = []
        return self.queued

    a = MvpView()
