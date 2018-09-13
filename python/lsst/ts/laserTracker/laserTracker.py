import logging

class LaserTrackerComponent():
    """
    
    """
    def __init__(self):
        self.targets = ["M1M3", "M2", "CAM"]

    def get_tracker_status(self):
        """ Queries the laser tracker device for current overall status. 
            
            Parameters
            ----------
            None

            Returns
            -------
            String :
                'R'         Ready to receive commands
                'EMP'       Executing Measurement Plan
                'ERR ??'    Error status. The ?? will be replaced by a numeric
                            error code
        """
        self.send_msg("?STAT")
    
    def get_laser_status(self):
        """ Queries the laser tracker device for the state of the laser.
            
            Parameters
            ----------
            None

            Returns
            -------
            String :
                'LNC'       Laser Not Connected
                'LON'       Laser On
                'LOFF'      Laser Off
        """
        self.send_msg("?LSTA")
    
    def get_position(self, target):
        """ Queries for the last measurement of a particular target.

            Parameters
            ----------
            target : string
                'M1M3'  Get M1M3 position
                'M2'    Get M2 position
                'CAM'   Get camera position

            Returns
            -------
            String :
                '??;X:<n>;Y:<n>;Z:<n>;Rx:<n>;Ry:<n>;Rz:<n>;date'
                Wherein ?? is the name of the component being measured,
                <n> are double precision floats, and date is the datetime
                the measurement was taken in the format 'MM/dd/yy H:mm:ss'
        """
        if target in self.targets:
            self.send_msg("?POS " + target)
        else:
            raise Exception

    def execute_measurement(self, target):
        """ Executes the measurement plan for the specified target.

            Parameters
            ----------
            target : string
                'M1M3'  Execute M1M3 measurement plan
                'M2'    Execute M2 measurement plan
                'CAM'   Execute camera measurement plan

            Returns
            -------
            None
        """
        if target in self.targets:
            self.send_msg("!CMD " + "MP" + target)
        else:
            raise Exception

    def clear_error(self):
        """ Clears errors. 

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        self.send_msg("!CLER")
    
    def laser_off(self):
        """ Turn laser off. Laser will turn on automatically when
            executing a measurement plan. 

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        self.send_msg("!CMD TLOFF")

    def send_msg(self, msg):
        outgoing = msg + "\r\n"

    