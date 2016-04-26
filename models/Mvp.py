# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


class Mvp:
    """
        Represents a MvP monster.
        Given that the user cannot input new MvPs, this class should never be
        instantiated outside MvpDataMapper.

        Args:
            name (str): The monster's name.
            respawn_min (int): The average time, in minutes, the monster takes
             to respawn.
            spawn_map (str): The map in which the monster appears.

        Attributes:
            last_death (datetime):
        """
    def __init__(self, name, respawn_min, spawn_map):
        self.nome = name
        self.tempo_respawn = timedelta(minutes=respawn_min)
        self.map = spawn_map
        self.last_death = None  # type: datetime

    def next_respawn(self):
        """
        Estimates the time remaining for the next respawn of this mvp.

        Returns:
            int: Estimated time, in minutes, for next respawn of this monster.
                A negative result means the Mvp has already spawned since last
                informed death. Will return None if there is no previous death
                record.
        """
        if self.last_death is None:
            return None
        respawn_time = self.last_death+self.tempo_respawn
        remaining_time = respawn_time - datetime.now()
        return remaining_time.total_seconds()/60
