from typing import Dict , List
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        
""""
class MockDriverHandle(DriverHandlerInterface):
    def variance(self, numbers : List[float]):
        return 159680.16
"""

def test_calculate_integration():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 1000]})

    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)
    formart_response = calculator_3.calculate(mock_request)

    print()
    print(formart_response)

    assert isinstance(formart_response, dict)
    assert formart_response == {'data': {'Calculator': 3, "value": 159680.16 , "sucess": True }}

""""
def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 1000]})

    driver = MockDriverHandle()
    calculator_3 = Calculator3(driver)
    formart_response = calculator_3.calculate(mock_request)

    print()
    print(formart_response)

    assert isinstance(formart_response, dict)
    assert formart_response == {'data': {'Calculator': 3, "value": 159680.16 , "sucess": True }}    
"""