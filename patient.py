from assistant import Assistant
from file import PatientFile
# from facade import Facade
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
        facade.handel_package_request()
    