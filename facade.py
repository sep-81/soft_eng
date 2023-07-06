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
                self.validation_simulation()
                self.execute_payment(selected_package_index)
                self._patient.assign_package(self._health_packages[selected_package_index])
                print("Process finished succesfully")
                break

        packages_window.close()

    
    def Temp_handle_package_request(self, patient: Patient):

        packages_array = [[package._health_service, package._execution_dates, package._doctor_id, package._estimated_cost]\
                            for package in self._health_packages]
        print(packages_array)

        self.show_available_packages()
        print("--- Please select your desired package: ")
        selected_package_index = int(input())
        self.set_assistant_to_patient()
        self.validation_simulation()
        self.execute_payment(selected_package_index)
        self._patient.assign_package(self._health_packages[selected_package_index])
        print("Process finished succesfully")

    def set_assistant_to_patient(self):
        self._assistant.assign_patient(self._patient)
        self._patient.assign_assistant(self._assistant)

    def show_available_packages(self):
        i = 0
        for package in self._health_packages:
            print("-> package number ", i , ":")
            package.show_package()
            i += 1
            
    def validation_simulation(self):
        print("Processing request")
        for i in range (0,5):
            time.sleep(0.8)
            print(".")
        
    def execute_payment(self, selected_package_index):

        event = sg.popup_yes_no(f'Package Information:\n{self._health_packages[selected_package_index].get_package_info_string()}\nAre you sure you want to pay the cost of this package via your online card?') 

        if event == "Yes":
            print("Payment was successful")
            # Write to file

        else:
            print("Payment was cancelled")

        # print("Package Information:")
        # print(self._health_packages[selected_package_index].show_package())
        # print("Please type \"Yes\" to pay the cost of this package via your online card: ")
        # input()

        
            
    
        
        

    
        
        
        
    