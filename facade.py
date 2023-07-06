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
        
    def Temp_handle_package_request(self):
        packages_array = [[package._health_service, package._execution_dates, package._doctor_id, package._estimated_cost]\
                            for package in self._health_packages]
        packages_layout = [

        ]
    
    def handle_package_request(self):
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
        print("Package Information:")
        print(self._health_packages[selected_package_index].show_package())
        print("Please type \"Yes\" to pay the cost of this package via your online card: ")
        input()

        
            
    
        
        

    
        
        
        
    