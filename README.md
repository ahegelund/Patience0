TL;DR:

`	- What is Patience0?`
`		- A script that can complete a web form that is used by the Danish state to allow citizens to sign up for surplus vaccine doses at the end of the day for COVID vaccination centres around the capital`
`		- Patience0 is a play on words, combining:`
`			- "Patient 0", a term reserved for the "first documented patient in a disease epidemic within a population"`
`			- "Patience", something you need when you want life to get back to normal after (what feels like) 5 years of the pancdmic and the best chance is a COVID vaccine`

`	- Why Patience0?`
`		- It is possible to sign up for surplus doses via a web form but the data is deleted daily just before midnight`
`		- It is only possible to sign up for surplus vaccines in a daily window (00:30 - 13:30)`
`		- I'm lazy and forgetful, plus; if I remember to do it daily, for two centres, between now (start of May) and when I might be able to get the vaccine through other channels (mid August), I will probably spend >150 hours in total filling in the form. Who has that kind of time?`
`		- I might never get a surplus vaccine but at least I learnt about Selenium, Heroku, DB management and the paint that comes with incorrectly installing Python in a virtual environment on a MacBook`

`	- How does Patience0 work?`
`		- Read the comments in the code, I tried to make it intuitive`
`		- If you need a TL;DR, it uses Selenium with a web driver to input data in fields `and click on buttons that I identified using Chrome's inspect elements to find the XPath
`		- If you want to see where I learnt how to do most of this then look in the added links in the documentation`

Documentation:

`	- Scoping Doc: https://docs.google.com/document/d/1KX5R9kR5k3eceyAJ0NsxVXW6LiURmxSdrzwAHudnKhw/edit#heading=h.xng07i5f7e5b`

Current action points (as of the recent commit on the start of May):

`	- Fix the clusterfuck of a Python installation on my local Mac Book (I can't gey the local env package to work and it's driving me nuts)`
`	- Personal data variables set as environmental variables stored in a local file that isn't pushed to Github`
`	- Set up in Heroku & test (using var files to host the private data)
`	- Find out how to track the success of the form fill using the network data (URL params aren't an option)`
`	- Look into setting up a secure DB on Heroku for storing the personal data`