from patient import Patient
from health_package import HealthPackage

class DAO:
    def __init__(self, filename: str) -> None:
        self._filename = filename

    
    def read_paitient_package(self, fileName: str = "") -> list[HealthPackage]:
        if fileName == "":
            fileName = self._filename
        # read from the file
        res_packages = []
        with open(fileName, "r") as file:
          for line in file:
            package_info = line.split("$")
            health_service = package_info[0]
            execution_dates = package_info[1]
            doctor_id = int(package_info[2])
            estimated_cost = int(package_info[3])
            res_packages.append(HealthPackage(health_service, execution_dates, doctor_id, estimated_cost))

        return res_packages
    
    def write_paitient_package(self, patientPackages: list[HealthPackage],
                               fileName: str = ""):
        if fileName == "":
            fileName = self._filename
        # write to the file
        with open(fileName, "w") as file:
          for package in patientPackages:
            pack_info = package.package_info()
            print(pack_info, file=file)
        
        

        
    

    
    


