from assistant import Assistant


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
    
    def assign_supporter(self, assigned_assistant: Assistant):
        self._assigned_assistant = assigned_assistant
    
    def request_package(self):
        pass
        