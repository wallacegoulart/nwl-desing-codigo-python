from typing import Dict , List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandle(DriverHandlerInterface):
    def standar_derivation(self, numbers : List[float]):
        return 3

def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    formart_response = calculator_2.calculate(mock_request)

    print()
    print(formart_response)

    assert isinstance(formart_response, dict)
    assert formart_response == {'data': {'Calculator': 2, 'result': 0.08 }}


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandle()
    calculator_2 = Calculator2(driver)
    formart_response = calculator_2.calculate(mock_request)

    print()
    print(formart_response)

    assert isinstance(formart_response, dict)
    assert formart_response == {'data': {'Calculator': 2, 'result': 0.33 }}    