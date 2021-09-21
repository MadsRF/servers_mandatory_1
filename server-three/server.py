from bottle import run, post, request
import requests
import csv
import io

@post('/')
def handle_request():
  # gets request
  json = request.json
  
  # multiplies the number from the request by 3
  number = int(json['number'])
  multiplied_number = number * 3
  json['number'] = str(multiplied_number)

  # converts to csv and writes to string
  output = io.StringIO()
  headers = ['number']
  writer = csv.DictWriter(output, fieldnames=headers, delimiter=",")
  writer.writeheader()
  writer.writerow(json)

  # gets the converted data
  csv_data = output.getvalue()

  # responds with the data
  return csv_data

# leaving host empty will allow any connection
run(host="127.0.0.1", port=3333, debug=True, reloader=True)