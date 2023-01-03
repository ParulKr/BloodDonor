#from django.http import HttpResponse
from django.shortcuts import render
from IMDBMovieList.models import sqlservercon
import pyodbc
connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                                host='DESKTOP-CR351BQ',
                                database='students',
                                trusted_connection='yes')
def index(request):
    cursor=connection.cursor()
    cursor.execute('select * from Movie')
    result=cursor.fetchall()
    return render(request, 'index.html' ,{'sqlservercon' : result})

def saverec(request):
    if request.method=="POST":
        if request.POST.get('MovieName') and request.POST.get('Budget') and request.POST.get('IMDBrating') and request.POST.get('link'):
            insertstvalues=sqlservercon()
            insertstvalues.MovieName=request.POST.get('MovieName')
            insertstvalues.Budget=request.POST.get('Budget')
            insertstvalues.IMDBrating = request.POST.get('IMDBrating')
            insertstvalues.link = request.POST.get('link')
            cursor=connection.cursor()
            cursor.execute("insert into Movie values ('"+insertstvalues.MovieName+"','"+insertstvalues.Budget+"','"+insertstvalues.IMDBrating+"','"+insertstvalues.link+"', null)")
            cursor.commit()
            return render(request,'index2.html')
    else :
        return render(request, 'index2.html')