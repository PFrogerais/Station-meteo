from bottle import route, run

@route('/')
def hello():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Station metéo </title>
</head>
<body>
    <h2>Infomations reçues par la station météo :</h2>
    <table>
        <tbody>
          <tr>
            <th scope="row">Humidité(%) = </th>
            <td>50</td>
          </tr>
          <tr>
            <th scope="row">Température(°C) =</th>
            <td>19</td>
          </tr>
        </tbody>
      </table>
      
</body>
</html>

"""
run(host='0.0.0.0', port=8585, debug=True)