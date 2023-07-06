


class HealthPackage:
    def __init__(self,
                 health_service: str,
                 execution_dates: str,
                 doctor_id: int,
                 estimated_cost: int):
        self._health_service = health_service
        self._execution_dates = execution_dates
        self._doctor_id = doctor_id
        self._estimated_cost = estimated_cost
    
    def show_package(self):
        print("health service: ", self._health_service)
        print("execution_dates: ", self._execution_dates)
        print("doctor_id: ", self._doctor_id)
        print("estimated_cost: ", self._estimated_cost)

    def get_package_info_string(self):
        str = f'health service: {self._health_service}\n'
        str += f'execution_dates: {self._execution_dates}\n'
        str += f'doctor_id: {self._doctor_id}\n'
        str += f'estimated_cost: {self._estimated_cost}\n'
        return str
        
    # package info as a string 
    def package_info(self, delim = "$"):
        return self._health_service + \
          delim + self._execution_dates + delim + \
          str(self._doctor_id) + delim + str(self._estimated_cost)
    
    
    
    
    
