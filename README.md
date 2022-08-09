# EBApi

## How to run:

* Clone the repo
* Install requirements
* Run server using manage.py
* Access the URL

## Images:

### Property List page
![Properties page](https://i.imgur.com/NBDmppM.png)

### Property Detail page
![Property detail page](https://i.imgur.com/G0TJl0W.png)

## Notes:

The main improvement that I would've loved to implement, given more time, 
would've been implementing the REST framework. 
At the planning phase of the project I decided on going with REST, but, sadly,
my current skill with this library didn't allow me to work as fast as I needed to.
In the end, I went with a basic, but clear, Django project using Requests.

There are two areas of my project that I don't think are that 'clean':
* The properties view: The way I obtain the page number of the next page is not as
elegant as I would've wanted. 
* The templates and the styling: For this project, I opted on focusing entirely on
the code and delivering something presentable. The price I paid were the crude HTML
templates coupled with their even simpler styling.

The part I wasn't able to finish was the testing, it's another thing I would've loved
to implement so I could practice because I only have some experience with unit testing.

I'm happy with what I accomplished, as I said before, at the planning stage I planned
to go on a more complicated route (that seemed simpler to implement) but it didn't go
as smooth as I planned so I had to revert with what I knew I could deliver fast, clear
and concise.