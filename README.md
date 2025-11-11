# INVESTMENT CALCULATOR Website
#### Video Demo: <https://youtu.be/c71P85PWM7Y>
#### Descrption:
- This is a investment calculator. It can calculate your personal investment.
- It base on my final project of CS50 for Python. That final project is a python program. Users have to run the program first. It's not that kind of user friendly for peple who do not have any programming backgroud. But now, it is a website. Everyone can use it easily.
- It base on your start capital, how much are you going to invest every month, how long you will invest, how is your expecting rate. And get your final money every year in table, generate a bar graph.
- This calculator can courage you to save money and invest it from small number.

## How to run the program
- 1. Run the website.
- 2. Enter your start capital. Like "0" or "1000". Start capital can be an integer or a float.
- 4. Enter your monthly invest. Like "0" or "100". Monthly invest can be an integer or a float. Be careful, start capital and monthly invest can NOT be both zero.
- 5. Enter your invest years. Like "30". It need to be an integer.
- 6. Enter your expecting yearly rate. Like "8". Rate can be an integer or a float.
- 7. You will get the result. A table with each year cumulative capital, cumulative return and total assets. And a bar graph.

## app.py
- It include all the python coding.

### month_calculate
- To calculate the monthly return. Each year has 12 months. For the first month invest, the user has 12 months investment time for that year. For the second month, only 11 months investment time. For the eleventh month, only 2 months investment time. And the final month, only 1 month investment time for that year. That's why I need this function.

### request methond
- To get the nummer in the website form, it needs the request method "POST"

### starting capital and monthly invest
- Be careful, starting capital and monthly invest can not be both zero. If the both nummber are zero, there is not meaning for the calculate. At this kind of situation. It will showing a appology websit.

### render_template("")
- If all four input are ok, it will show the final result with render_template("result.html")

## Layout.html, index.html, apology.html
- These three htmls are basic on the htmls from the cs50 finance. I just make a few ajustment.

## result.html
- In this html, it need to reach the effect: first part has one table with each year cummulated capital, cummulated return and total assets; second part it use chart.js to show a bar graph.


## Road Map
### Version 1
- Creat index.html
- Get user’s start capital.
- Get user's monthly invest.
- Get user’s invest year.
- Get user’s yearly investment rate.
- Creat a basic website with forms

### Version 2
- Creat app.py.
- Test if app.py can get the inputs from website forms.
- Change the inputs into integet or float.
- Calculte the result.

### Version 3
- Test if the appology website can load without problem.
- Creat result.html.
- Test result.html to see if the website can load.

### Version 4
- Test if the results are correct.
- Add chart.js into result.html and check if it can show the bar garph.

### Version 5
- Clean the bugs in result.html
- Seprate the results into two parts. One is the total capital, another is the total return.

### Version 6
- Writing the pytest code
- Test test_app.py
