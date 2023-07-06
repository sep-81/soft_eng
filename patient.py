from typing import Any
from assistant import Assistant
from file import PatientFile
# from facade import Facade
import PySimpleGUI as sg
from health_package import HealthPackage

class Patient:
    def __init__(self,
                 name: str,
                 nickname: str,
                 password: str,
                 call_info: str,
                ):
        self._name = name
        self._nickname = nickname
        self._password = password
        self._call_info = call_info
        self._reserved_packages = []
        
        
    def assign_assistant(self, assigned_assistant: Assistant):
        self._assigned_assistant = assigned_assistant
    
    def assign_file(self, file: PatientFile):
        self._file = file
    
    def assign_package(self, package: HealthPackage):
        self._reserved_packages.append(package)
    
    def request_package(self, facade):
        facade.handle_package_request(self)
      
    def get_res_packages(self) -> list[HealthPackage]:
        return self._reserved_packages
    
    def can_afford(self, cost: int) -> bool:
        return self._file._balance >= cost
    
    def exists(self, package: HealthPackage) -> bool:
        return package in self._reserved_packages
    
    def show_res_packages(self):

        packages_array = [[package._health_service, package._execution_dates, package._doctor_id, package._estimated_cost]\
                            for package in self._reserved_packages]

        header = ['Health Service', 'Execution Dates', 'Doctor ID', 'Estimated Cost']
        packages_layout = [
            [sg.Table(values=packages_array,
                    headings=header,
                    max_col_width=35,
                    auto_size_columns=True,
                    justification='right',
                    num_rows=7,
                    key='-Packages-Table-',
                    row_height=35,
                    tooltip='Health Packages',
                    enable_events=True,
                    display_row_numbers=True)],
        ]
        
        packages_window = sg.Window('Health Packages', packages_layout)

        while True:
                event, values = packages_window.read()
                if event == sg.WIN_CLOSED:
                    break

        packages_window.close()