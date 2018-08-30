import logging

class LaserTrackerComponent():
    

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
        pass
    
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
        pass
    
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
        pass

    def execute_measurement(self, target):
        """ Executes the measurement of the specified target.

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
        pass

    def clear_error(self):
        """ Clears errors. 

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        pass
    
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
        pass

    