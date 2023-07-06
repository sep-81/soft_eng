

class PatientFile:
    def __init__(self,
                 file_status: str,
                 medical_history: str,
                 biometric_info: str,
                 balance: int = 0
                 ):
        self._file_status = file_status
        self._medical_history = medical_history
        self._biometric_info = biometric_info
        self._balance = balance
        
    