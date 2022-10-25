# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 
import pdb

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############

        return np.matrix([
            [1, 0, 0, params.dt, 0, 0],
            [0, 1, 0, 0, params.dt, 0],
            [0, 0, 1, 0, 0, params.dt],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]])
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        t3q = (params.dt ** 3) * params.q / 3
        t2q = (params.dt ** 2) * params.q / 2
        tq = params.dt * params.q

        return np.matrix([
            [t3q, 0, 0, t2q, 0, 0],
            [0, t3q, 0, 0, t2q, 0],
            [0, 0, t3q, 0, 0, t2q],
            [t2q, 0, 0, tq, 0, 0],
            [0, t2q, 0, 0, tq, 0],
            [0, 0, t2q, 0, 0, tq]])
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        track.x = self.F() * track.x
        track.P = self.F() * track.P * self.F().transpose() + self.Q()
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############

        H = meas.sensor.get_H(track.x)
        S = self.S(track, meas, H)
        K = track.P * H.transpose() * np.linalg.inv(S)
        track.x = track.x + K * self.gamma(track, meas)
        track.P = (np.identity(params.dim_state) - K * H) * track.P
        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        return meas.z - meas.sensor.get_hx(track.x)
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        return H * track.P * H.transpose() + meas.R
        
        ############
        # END student code
        ############ 
