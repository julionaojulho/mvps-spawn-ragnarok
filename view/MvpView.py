# -*- coding: utf-8 -*-
# https://docs.python.org/3.5/library/datetime.html ler depois

# import string

class MvpView:
    def __init__(self,name):
        self.mvp = name
        self.queued = []
        self.time = []

    def add_entry(self,mvp_list):#linkar mvp_list com o controller
        """
        Ask user for input and store its values
        """
        mvp_name = self.mvp
        while mvp_name.lower() not in mvp_list:#mvp_list:
            print("Mvp not found, please, write the name again.\n")
            mvp_name = raw_input("Name: ")
        self.deathtime = raw_input("Death time (hh:mm:ss): ")
        self.time = [int(self.deathtime[:-6]),
                     int(self.deathtime[-5:-3]),
                     int(self.deathtime[-2:])]

    def next_on_list(self,mvp_time = []):
        """
        Print list of mvps in ascending respawn time order
        """
        self.queued = mvp_time
        return self.queued
