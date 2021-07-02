# open-pos
open-pos is an open source point of service software.


## FAQ

### What is a POS?
POS stands for point of service, this is the system that many buisnesses use in order to serve customers.

### How do I use this software?
Currently you do not as it is not in a production state.


## Contributing
Feel free to send me whatever you feel like should be changed or if you want to help work on it more long term feel free to contact me either by discord in the contact section or join my slack server I just made for this the link to join will be in the contact section as well.


## Contact
Feel free to message me on discord Sagulls#9550 currently, or join the slack server listed below. Unfortunetly I don't have any other kind of contact setup you could try and email me but my email is a mess and I've been meaning to setup my own email server but I haven't gotten around to it yet.

Slack server : (Sorry it's not really setup yet)
https://join.slack.com/t/jadonsslackserver/shared_invite/zt-sgjs56oi-J_uZrM6ecqdnUcxjx67NcA


## File Structure
The file structure is a bit odd at first glace.  The reason for this is that there are actually a few seperate types of clients in this git repo.

### /config
This is for storing config and any other settings that software might use.

### /database
For handling reading and writing to the database this is also where the debug database and scheme will likely be stored, in the long run you would have a seperate mySQL server.

### /flaskr
This stores everything todo with the flask web-server.  (Flask dev server is only intended for development a real web-server will be used if this ever goes to a production phase.)

### /local_client
This is the local client version of the website, more advanced tools will be avalable here that will not be avalable on the web server by default.  This is intended to be ran on a local computer in the store so employees can't clock in randomly from the comfort of their own home.  This will of course be configurable because it's open source so you can really configure whatever you want.

### /local_register
This is the software for the register to ring up customers it will automatically update inventory calculate price etc.  Should add support for opening drawers, counting money, and taking credit card payments.

### /run
This is where all the main files of each of the main modules are stored.  (where you can launch them for testing purposes)

### /setup
This is for basic setup stuff that may need to be done on first run of the software for instance setting up the database.

### /tests
This is for tests to make sure all functions are operating as they should and test for any known security flaws etc.


## Features
Future features that are planned on being added.

### Security camera support
Support for local security cameras as well as streaming to a web server.

### Inventory system
A system to keep track of inventory.

### Sales tracking
A system to track sales.

### Wages / Employee management
A clock in and clock out system to keep track of how much money you owe employees.

### And probably more
If I don't feature creep this project into oblivion.


## Disclosure
This is my first "big" project in python I'm fairly comfortable with python but there are something I might not do in the most optimal way but please feel free to give me some advice.


## License
I put this under the MIT license because I looked up open source licenses I don't really know the differences between them so this may change in the future depending on what input I get from people.