

class Assistant:
    def __init__(self,
                 name: str,
                 nickname: str,
                 sid: str,
                 score: int,
                 password: str,
                 contract_duration: int,              
                ):  
        self._name = name
        self._nickname = nickname
        self._sid = sid
        self._score = score
        self._password = password
        self._contract_duration = contract_duration             # By month
        
    def assign_patient(self, assigned_patient):
        self._assigned_patient = assigned_patient
        
    
