from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)


form = """
<!DOCTYPE HTML>

<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<title>DruziCafe</title>
	  	<!--<meta name="description" content="The HTML5 Herald">
	  	<meta name="author" content="SitePoint">

	  	<link rel="stylesheet" href="css/styles.css?v=1.0">

	  [if lt IE 9]>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script>
	  <![endif]-->
	  	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css" integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
	
		<script>
			function isNumberKey(evt)
			{
				var charCode = (evt.which) ? evt.which : evt.keyCode;
				if (charCode != 46 && charCode > 31 
				&& (charCode < 48 || charCode > 57))
				return false;
				return true;
			}
		</script>
	
	</head>

	<style>
		body, html {
			padding:0px;
			margin:0px;
		}

		header {
			background-color: powderblue;
			height: 120px;
		}
		
		header img {
			float: left;	
			width: 100px;
			height: 100px;
			margin: 10px;
			background: #555;
		}

		header h1 {
			margin: 0;
			position: relative;
			top: 18px;
			left: 10px;
			
		}

		form {
			/* Just to center the form on the page */
			margin: 10 auto;
			width: 400px;

			/* To see the limits of the form */
			padding: 1em;
			border: 1px solid #CCC;
			border-radius: 1em;
		}

		.page-header {
			height: 120px;
			background-color: powderblue;
		}

		.page-header h1 {
			position: relative;
		}

		.page-header img {
			float: left;	
			width: 100px;
			height: 100px;
			margin: 10px;
			background: #555;
		}
	</style>
	
	<body>
		<div class="page-header">
			<img src="static/logo.jpg" alt="logo" />
			<h1>Delivery Panel 
				<br><small>Facebook FoodBot</small></h1>
		</div>

		<center>
			<form action="/delivery" method="post">

	  			<input type="text" class="form-control mb-2 mr-sm-2" onkeypress="return isNumberKey(event)" name="orderid" placeholder="Код заказа">
	  			<button type="submit" class="btn btn-primary mb-2">Submit</button><br>

				Название в меню: <input type="text" class="form-control" name="name" disabled><br>
				Номер заказа: <input type="text" class="form-control" name="ordernum" disabled><br>
				Дата заказа: <input type="date" class="form-control" name="orderdate" disabled><br>
				Сумма заказа: <input type="text" class="form-control" name="cost" disabled><br>
				Дата выдачи: <input type="date" class="form-control" name="takedate" disabled><br>
				
				<label for="sel1">Статус заказа:</label>
				<select class="form-control" id="sel1">
					<option>Active</option>
				    <option>Done</option>
				</select>

			</form>
		</center>
	  
	</body>
</html>
"""


@app.route('/')
def index():
    # return form
    return render_template('index.html')


@app.route('/delivery', methods=['POST', 'GET'])
def delivery():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        orderid = request.form.get('orderid')
        request.form['name'] = "Cake"
        request.form['ordernum'] = "12345"
        request.form['orderdate'] = "12/12/2017"
        request.form['cost'] = "123"
        request.form['takedate'] = "01/12/2017"
        request.form['sel1'] = "Done"

        print(orderid)
        # return render_template(form)
        # return render_template('index.html')
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
