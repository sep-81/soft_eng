from patient import Patient
from health_package import HealthPackage

class DAO:
    def __init__(self) -> None:
        self.filename = ""

    
    def read_paitient_package(self, fileName: str = "") -> list[Patient]:
        if fileName == "":
            fileName = self.filename
        # read from the file
        open(fileName, "r")

        return list[Patient]
    
    def write_paitient_package(self, patientPackages: list[HealthPackage],
                               fileName: str = ""):
        if fileName == "":
            fileName = self.filename
        # write to the file
        open(fileName, "w")
        for package in patientPackages:
            pass
        
    

    
    


