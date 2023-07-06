import PySimpleGUI as sg
import time
from patient import Patient
from assistant import Assistant
from health_package import HealthPackage


class Facade:
    def __init__(self,
                 patient: Patient,
                 assistant: Assistant,
                 health_packages: list            
                 ):
        self._patient = patient
        self._assistant = assistant
        self._health_packages = health_packages
        
    def handle_package_request(self, patient: Patient):

        packages_array = [[package._health_service, package._execution_dates, package._doctor_id, package._estimated_cost]\
                            for package in self._health_packages]

        header = ["Health Service", "Execution Dates", "Doctor ID", "Estimated Cost"]
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
            [sg.Push(), sg.Text('Please select your desired package'), sg.Push()],
        ]

        packages_window = sg.Window('Health Packages', packages_layout)

        while True:
            
            event, values = packages_window.read()
            
            if event == sg.WIN_CLOSED:
                break

            elif event == '-Packages-Table-':
                selected_package_index = values['-Packages-Table-'][0]

                self.set_assistant_to_patient()
                
                ok = self.validation_simulation(self._health_packages[selected_package_index])
                if not ok:
                    break
                
                is_ok = self.execute_payment(selected_package_index)
                if not is_ok:
                    break
                
                self._patient.assign_package(self._health_packages[selected_package_index])
                
                sg.popup("Process finished succesfully")
                break

        packages_window.close()

    def set_assistant_to_patient(self):
        self._assistant.assign_patient(self._patient)
        self._patient.assign_assistant(self._assistant)

    def show_available_packages(self):

        packages_array = [[package._health_service, package._execution_dates, package._doctor_id, package._estimated_cost]\
                            for package in self._health_packages]

        header = ["Health Service", "Execution Dates", "Doctor ID", "Estimated Cost"]
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
            
    def validation_simulation(self, package):
        print("Processing request", end='', flush=True)
        for i in range (8):
            time.sleep(0.4)
            print('.', end='', flush=True)
        print()

        if self._patient.can_afford(package._estimated_cost):
            if self._assistant.can_validate(package):
                if not self._patient.exists(package):
                    return True
                else:
                    sg.popup("You already have this package")
            else:
                sg.popup("Validation failed")
        else:
            sg.popup("You don't have enough money for this package")

        return False
        
    def execute_payment(self, selected_package_index):

        event = sg.popup_yes_no(f'Package Information:\n{self._health_packages[selected_package_index].get_package_info_string()}\nAre you sure you want to pay the cost of this package via your online card?') 

        if event == "Yes":
            sg.popup("Payment was successful")
            return True

        else:
            sg.popup("Payment was cancelled")
            return False

        
            
    
        
        

    
        
        
        
    