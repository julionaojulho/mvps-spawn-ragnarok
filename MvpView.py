import string
# https://docs.python.org/3.5/library/datetime.html ler depois

class MvpView():
    def __init__(self,name,time=0):
        pass     # não sei direito o que fazer aqui

    def add_entry(self):
        """
        Ask user for input and store its values
        """
        mvp_name = input("Name: ")
        while mvp_name.lower() not in mvp_list:
            print "Mvp not found, please, write the name again.\n"
            mvp_name = input("Name: ")
        mvp_deathtime = input("Death time (hh:mm:ss): ")
        mvp.seconds = int(mvp_deathtime[-2:])
        mvp.minutes = int(mvp_deathtime[-5:-3])
        mvp.hours = int(mvp_deathtime[:-6])

    def next_on_list(self,mvp_time = []):
        """
        Print list of mvps in ascending respawn time order
        """
        self.queued = []
        return self.queued
