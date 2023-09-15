class Timer:
    def __init__(self, second):
        second = int(float(second))
        self._second = second % 60
        self._minute = (second // 60) % 60
        self._hour = second // 3600
        
        
    def clock_string(self):
        if (0 <= self._hour <= 9):
            return_string = "0" + str(self._hour)
        else:
            return_string = str(self._hour)
        
        if (0 <= self._minute <= 9):
            return_string = return_string + ":" + "0" + str(self._minute)
        else:
            return_string = return_string + ":" + str(self._minute)
    
        if (0 <= self._second <= 9):
            return_string = return_string + ":" + "0" + str(self._second)
        else:
            return_string = return_string + ":" + str(self._second)
        return return_string
        
        
    def count_down(self):
        self._second -= 1;
        if (self._second == -1):
            self._second = 59
            self._minute -= 1
            if (self._minute == -1):
                self._minute = 59
                self._hour -= 1
        return self.clock_string()