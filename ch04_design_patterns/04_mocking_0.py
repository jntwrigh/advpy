import unittest.mock as mock
import ch04_design_patterns.sample as samp


@mock.patch('ch04_design_patterns.sample.my_function')
def invoke_me(mock_obj):

    mock_obj.return_value = 'my_function has been mocked!'

    result = samp.my_function()
    print(result)


invoke_me()
