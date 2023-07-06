# unit tests for all the functions in the program
import unittest
from file import PatientFile
from health_package import HealthPackage
from DAO import DAO
from facade import Facade
from patient import Patient
from assistant import Assistant


class TestDAOLayer(unittest.TestCase):
    def setUp(self) -> None:
        self.dao = DAO("test.txt")
        self.file_text_str = "heart_surgery$2023/07/08 - 2023/07/11$113$20000\n\
          heart_surgery$2023/07/08 - 2023/07/11$113$20000\n\
          dental_surgery$2023/07/16 - 2023/07/21$116$15000"
        with open("test.txt", "w") as file:
            file.write(self.file_text_str)

    def test_init(self):
        self.assertEqual(self.dao._filename, "test.txt")

    def test_read_health_packages(self):
        res_packages = self.dao.read_health_packages()
        self.assertEqual(len(res_packages), 3)

    def test_write_health_packages(self):
        res_packages = self.dao.read_health_packages()
        self.assertEqual(len(res_packages), 3)
        res_packages.append(HealthPackage("heart_surgery", "2023/07/08 - 2023/07/11", 113, 20000))
        self.dao.write_health_packages(res_packages)
        res_packages = self.dao.read_health_packages()
        self.assertEqual(len(res_packages), 4)



class TestFacade(unittest.TestCase):
    def setUp(self) -> None:
        self.patient = Patient("Alireza", "Alireza1", "123456", "09121927732")
        self.assistant = Assistant("Hadi", "Hadi1", 112, 5, "123456", 12)
        file = PatientFile("Open", "Empty", "Height: 182, Weight: 81", 1000000)
        self.patient.assign_file(file)
        health_package1 = HealthPackage("brain_surgery", "2023/07/05 - 2023/07/08", 111, 10000)
        health_package2 = HealthPackage("heart_surgery", "2023/07/08 - 2023/07/11", 113, 20000)
        health_package3 = HealthPackage("dental_surgery","2023/07/16 - 2023/07/21", 116, 15000)
        self.health_packages = [health_package1, health_package2, health_package3]
        self.facad = Facade(self.patient,self.assistant,self.health_packages)

    def test_init(self):
        self.assertEqual(self.facad._patient, self.patient)
        self.assertEqual(self.facad._assistant, self.assistant)
        self.assertEqual(self.facad._health_packages, self.health_packages)

    def test_vlidation(self):
        result = self.facad.validation_simulation(self.health_packages[1])
        self.assertEqual(result, True)



class TestPatient(unittest.TestCase):
    def setUp(self) -> None:
        self.patient = Patient("Alireza", "Alireza1", "123456", "09121927732")
        self.file = PatientFile("Open", "Empty", "Height: 182, Weight: 81", 1000000)
        self.pack = HealthPackage("brain_surgery", "2023/07/05 - 2023/07/08", 111, 10000)

    def test_init(self):
        self.assertEqual(self.patient._name, "Alireza")
        self.assertEqual(self.patient._nickname, "Alireza1")
        self.assertEqual(self.patient._password, "123456")
        self.assertEqual(self.patient._call_info, "09121927732")
    

    def test_assign_assistant(self):
        assis = Assistant("Hadi", "Hadi1", 112, 5, "123456", 12)
        self.patient.assign_assistant(assis)
        self.assertEqual(self.patient._assigned_assistant, assis)


    def test_assign_file(self):
        self.patient.assign_file(self.file)
        self.assertEqual(self.patient._file, self.file)

    def test_append_pack(self):
        self.patient.assign_package(self.pack)
        self.assertEqual(self.patient._reserved_packages[0], self.pack)

    def test_get_res_packages(self):
        self.patient.assign_package(self.pack)
        self.assertEqual(self.patient.get_res_packages(), [self.pack])
        
    def test_can_afford(self):
        self.patient._file = self.file
        self.assertFalse(self.patient.can_afford(1000000000))

    def test_exist(self):
        self.patient._reserved_packages.append(self.pack)
        self.patient.exists(self.pack)


class TestHealthPackage(unittest.TestCase):
    def setUp(self) -> None:
        self.pack = HealthPackage("brain_surgery", "2023/07/05 - 2023/07/08", 111, 10000)

    def test_init(self):
        self.assertEqual(self.pack._health_service, "brain_surgery")
        self.assertEqual(self.pack._execution_dates, "2023/07/05 - 2023/07/08")
        self.assertEqual(self.pack._doctor_id, 111)
        self.assertEqual(self.pack._estimated_cost, 10000)
    
    def test_get_package_info_string(self):
        result = "health service: brain_surgery\nexecution_dates: 2023/07/05 - 2023/07/08\ndoctor_id: 111\nestimated_cost: 10000\n"
        self.assertEqual(self.pack.get_package_info_string(), result)

    def test_pack_info(self):
        result = "brain_surgery$2023/07/05 - 2023/07/08$111$10000"
        self.assertEqual(self.pack.package_info(), result)

if __name__ == '__main__':
    unittest.main()


