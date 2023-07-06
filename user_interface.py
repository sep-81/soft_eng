import PySimpleGUI as sg
from patient import Patient
from file import PatientFile
from assistant import Assistant
from health_package import HealthPackage
from facade import Facade
from DAO import DAO

WINDOW_SIZE = (800, 600)

def init_objects():
    patient = Patient("Alireza", "Alireza1", "123456", "09121927732")
    file = PatientFile("Open", "Empty", "Height: 182, Weight: 81", 1000000)
    assistant = Assistant("Sepehr", "Sepehr1", 112, 5, "123456", 12)
    patient.assign_file(file)
    return patient, assistant

def init_health_packages():
    health_package1 = HealthPackage("brain_surgery", "2023/07/05 - 2023/07/08", 111, 10000)
    health_package2 = HealthPackage("heart_surgery", "2023/07/08 - 2023/07/11", 113, 20000)
    health_package3 = HealthPackage("dental_surgery","2023/07/16 - 2023/07/21", 116, 15000)
    health_packages = [health_package1, health_package2, health_package3]
    return health_packages

def init_patient_packages(dao: DAO, patient: Patient):
    patient_packages = dao.read_patient_package()
    for package in patient_packages:
        patient.assign_package(package)
         
def write_patient_packages(dao: DAO, patient_packages: list[HealthPackage]):
    dao.write_paitient_package(patient_packages)

def create_welcome_page():
    layout = [
        [sg.Push(), sg.Text("Welcome!", font=("Helvetica", 23)), sg.Push()],
        [sg.Push(), sg.Text("To Your Hospital", font=("Helvetica", 23)), sg.Push()],
        [sg.Push(), sg.Text("We Care About You", font=("Helvetica", 18), pad=(0, 50)), sg.Push()],   
        [sg.Push(), sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar', pad=(0, 10)), sg.Push()],
        [sg.Push(), sg.Text("Loading initial data...", font=("Helvetica", 10)), sg.Push()],
    ]

    window = sg.Window('Welcome', layout, size=WINDOW_SIZE, element_justification='center', margins=(0, 100))
    progress_bar = window['progressbar']

    for i in range(100):
        event, values = window.read(timeout=10)
        progress_bar.UpdateBar(i + 1)
    
    window.close()

if __name__ == '__main__':

    sg.theme('DarkPurple1')

    patient, assitant = init_objects()
    # health_packages = init_health_packages()
    # facade = Facade(patient, assitant, health_packages)
    # how about to move everything to the facade?
    dao = DAO("data/HealthPackages.txt")
    health_packages = dao.read_health_packages()
    facade = Facade(patient, assitant, health_packages)
    # init_patient_packages(dao, patient)

    create_welcome_page()

    layout = [
        [sg.Push(), sg.Button('Request Package', key='-Request-Package-',size=(20, 2), pad=(0, 20)), sg.Push()],
        [sg.Push(), sg.Button('Available Packages', key='-Available-Packages-',size=(20, 2), pad=(0, 20)), sg.Push()],
        [sg.Push(), sg.Button('My Packages', key='-My-Packages-',size=(20, 2), pad=(0, 20)), sg.Push()],
        [sg.Push(), sg.Exit(size=(20, 2), pad=(0, 20)), sg.Push()],
    ]
    window = sg.Window('Main Menu', layout, size=WINDOW_SIZE, element_justification='center', margins=(50, 80))

    while (True):

        event, values = window.read()

        if event == '-Request-Package-':
            patient.request_package(facade)

        elif(event == '-Available-Packages-'):
            facade.show_available_packages()

        elif(event == '-My-Packages-'):
            patient.show_res_packages()

        elif(event == sg.WIN_CLOSED or event == 'Exit'):
            write_path = "data/" + patient._nickname + ".txt"
            dao.write_health_packages(patient.get_res_packages(), write_path)
            break
        


