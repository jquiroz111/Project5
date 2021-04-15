# Test Code 1 for the API
test = requests.post("http://localhost:5000/md5/test")

expected_output = '908f6bcd4621d373cade832627b4f6'

test.json()

if expected_result == test.json()['output']:
  print('/md5/test   The Test Passed')
 else:
  print('/md5/test   The Test Failed)
        
# Test Code 2 for the API        
test2 = requests.post("http://localhost:5000/keyval/")

expected_output = '908f6bcd4621d373cade832627b4f6'

test2.json()

if expected_result == test2.json()['output']:
  print('/keyval/   The Test Passed')
 else:
  print('/keyval/  The Test Failed)
