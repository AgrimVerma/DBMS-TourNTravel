# Tminus0-Tours-N-Travel

## About
> A user-friendly online Tour and travel booking function to the people to replace the hardcopy ordering form.


## Team Members
- Agrim Verma
- Shantanu
- Krishna Shah
- Neel Patel
- Jiniya Singal


## Software Requirements
- Microsoft Visual Studio Code   
- PostgreSQL (fully configured)  
- Python3  
- Pgadmin4 
- Django (django will be installed when you run pip install -r requirements.txt)



## How to run this project


```sh
git clone https://github.com/AgrimVerma/DBMS-TourNTravel.git
cd DBMS-TourNTravel
pip3 or pip install -r requirements.txt

```
# For setting up the Database

- First create a database in postgreSQL named as ‘ToursNTravel’.

- We have created a backup of our own database (which includes the information about travel destinations and flights, trains and hotels schedules we are providing for this project) that you can restore .

- Then open settings.py in the code editor and change the database information, particularly username and password which you have set in your postgres.

- Now run the following commands - 
 

```
python or python3 manage.py migrate
python or python3 manage.py runserver
```
Now, open localhost:8000 or 127.0.0.1:8000 at the browser of your choice.
Voila, now you must have landed at the homepage of our website Tours & Travels.

> NOTE-
To book any flight, train or hotel you must be logged in. Flights, trains, and hotels are limited to the destinations and dates we have picked. So please use the dummy data provided below.
**All the fields are case sensitive.

Destinations added - 
1.	Tokyo
2.	New York
3.	Sydney
4.	Ladakh
5.	Seoul

Flights-
| Source |	Destination |	Departure Date |
|----------|:-------------:|------:|
| New York | 	Tokyo |	12-5-2022 | 
| Ladakh |	Seoul |	12-5-2022 | 
| Tokyo |	Sydney |	12-5-2022 |
| Sydney |	Ladakh |	12-5-2022 |


Trains -
| Source |	Destination |	Departure Date |
|----------|:-------------:|------:|
| New York |	Tokyo |	2022-05-12 |
| Ladakh	| Seoul	 | 2022-05-12 |
| Tokyo	| Sydney |	2022-05-12 |
| Seoul	| New York |	2022-05-12 |
| Sydney	| Ladakh	| 2022-05-12 |

Hotels - 
| Company Name	| City |	Address |
|----------|:-------------:|------:|
| ToursNTravel	| Tokyo |	TokyoCity|
| ToursNTravel	| Seoul	| SeoulCity |
| ToursNTravel	| Sydney	| SydneyCity |
| ToursNTravel	| New York	| NewYorkCity |
| ToursNTravel	| Ladakh	| LadakhCity |





 
