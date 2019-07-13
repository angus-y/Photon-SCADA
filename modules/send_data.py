from urllib.request import Request, urlopen


zero = """
  [
    "0"
  ]
"""

one = """
  [
    "1"
  ]
"""


def main(values):
    values = values.encode()
    headers = {
      'Content-Type': 'application/json'
    }
    request = Request('http://blynk-cloud.com/PibLh_9lhMCt_5fmc17ftsDfMWkqdx0S/update/V10', data=values, headers=headers)
    request.get_method = lambda: 'PUT'
    response_body = urlopen(request).read()
    print (response_body)
