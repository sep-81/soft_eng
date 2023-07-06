import PySimpleGUI as sg

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

        layout = [
            [sg.Push(), sg.Text('Health Service'), sg.Push(), sg.Text(self._health_service), sg.Push()],
            [sg.Push(), sg.Text('Execution Dates'), sg.Push(), sg.Text(self._execution_dates), sg.Push()],
            [sg.Push(), sg.Text('Doctor ID'), sg.Push(), sg.Text(self._doctor_id), sg.Push()],
            [sg.Push(), sg.Text('Estimated Cost'), sg.Push(), sg.Text(self._estimated_cost), sg.Push()], 
        ]

        window = sg.Window('Health Package', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
        window.close()

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
    
    
    
    
    
