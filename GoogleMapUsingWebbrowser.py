import webbrowser
basic_url='https://www.google.co.in/maps'
str= input('Enter the city name : ')
str.replace(' ','+')
webbrowser.open(basic_url+'/place/'+str)
