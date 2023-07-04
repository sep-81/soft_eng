from patient import Patient
from facade import Facade
from assistant import Assistant
from health_package import HealthPackage


def init_obejects():
    patient = Patient("Alireza", "Alireza1", "123456", "09121927732")
    assistant = Assistant("Sepehr", "Sepehr1", 112, 5, "123456", 12)
    patient.assign_assistant(assistant)
    assistant.assign_patient(patient)
    return patient, assistant


def init_health_packages():
    health_package1 = HealthPackage("brain surgery", "2023/07/05 - 2023/07/08", 111, 10000)
    health_package2 = HealthPackage("heart_surgery", "2023/07/08 - 2023/07/11", 113, 20000)
    health_package3 = HealthPackage("dental_surgery","2023/07/16 - 2023/07/21", 116, 15000)
    health_packages = [health_package1, health_package2, health_package3]
    return health_packages

if __name__ == '__main__':
    patient, assitant = init_obejects()
    health_packages = init_health_packages()
    while (True):
        command = input();
        if(command == 'request_package'):
            pass
        
        
        # TODO