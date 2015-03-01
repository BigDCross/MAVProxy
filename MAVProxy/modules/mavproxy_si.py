#!/usr/bin/env python

"""
This is the si module.
Procedure to start safely:
-Arm Copter using TX
-Start up mavproxy w/ appropriate baudrate and aircraft name
-Run mavproxy command "module load si"
"""

import os, struct
from time import sleep

mpstate = None

from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module

from si_utils import map_range


class SI(mp_module.MPModule):
    def __init__(self, mpstate):
        super(SI, self).__init__(mpstate, "si", "SI control mode")

        # get calibrated rc values
        self.rc1_min = self.get_mav_param("RC1_MIN")
        self.rc1_trim = self.get_mav_param("RC1_TRIM")
        self.rc1_max = self.get_mav_param("RC1_MAX")

        self.rc2_min = self.get_mav_param("RC2_MIN")
        self.rc2_trim = self.get_mav_param("RC2_TRIM")
        self.rc2_max = self.get_mav_param("RC2_MAX")

        self.rc3_min = self.get_mav_param("RC3_MIN")
        self.rc3_trim = self.get_mav_param("RC3_TRIM")
        self.rc3_max = self.get_mav_param("RC3_MAX")

        self.rc4_min = self.get_mav_param("RC4_MIN")
        self.rc4_trim = self.get_mav_param("RC4_TRIM")
        self.rc4_max = self.get_mav_param("RC4_MAX")

    def idle_task(self):
        '''called in idle time'''

        manual_control = [0] * 4

        """
        manual_control[0] = control_packet["yaw"] # rc1
        manual_control[1] = control_packet["pitch"] # rc2
        manual_control[2] = control_packet["throttle"] # rc3
        manual_control[3] = control_packet["roll"] # rc4
        """

        manual_control[0] = self.rc1_min
        manual_control[1] = self.rc2_min
        manual_control[2] = (self.rc3_min + self.rc3_max) / 2 # send half throttle
        manual_control[3] = self.rc4_min

        self.master.mav.manual_control_send(self.target_system,
                                                       self.target_component,
                                                       *manual_control)

        sleep (.1)

    def unload(self): # This works! Use module unload si
        print "Unloading SI!"

def init(mpstate):
    '''initialise module'''
    return SI(mpstate)
