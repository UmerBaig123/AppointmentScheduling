To run the server
1- Open the terminal in this directory
2- Type in terminal "Scripts/activate" and enter
3- Run command "python manage.py runserver"
4- Open the link thatll be shown in the terminal, it'll be something like http://127.0.0.1:8000/

The delay in the javascript side checking of availability is inside home->templates->home.html
at the end of file there is a comment indicating the number, it is in miliseconds
I've used 5000ms because my laptop was blowing up
