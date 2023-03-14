# APSE key-value app



# How to get code
```
cd existing_repo
git remote add origin https://stgit.dcs.gla.ac.uk/apse-group/apse-key-value-app.git
git branch -M main
git push -uf origin main
```
at this point, you may be prompted for a password, depending on your IDE, if you choose to push up code via the IDE, you will not have to encounter this question as much, as it will remember your password for you. Password should be just your gitlab one.
## Name
Our name is called "Flashcards For all" Developers credit goes to: Alastair Hood, Rayaan Syyed, Connor Crookston, Abdu Khan


## Description
Our specification was to create a key pair value database and the requirements were for a user to be able to: Update, delete and create from this database. So our project is to have our key as the question and the answer as the value. Users can create new flashcards and update old ones as well as deleting.


## Installation
To continue working on this application, there are some pre-requistes. 
You should have :
Python 3  
A suitable IDE  
Flask (most IDE's can handle the installation) but if you happen to not be in this situation, doing:
`pip install flask`
will work. More info [here](https://www.geeksforgeeks.org/how-to-install-flask-in-windows/) 
and [here](https://pypi.org/project/Flask/)

Sqlite (Most applications already have it)  
An application to view the datas database

[Resources](https://stgit.dcs.gla.ac.uk/apse-group/apse-key-value-app/-/wikis/Resources)

## Usage
Flask is used for our framework, the code is written in python and supported by flask which allows you to make frontend code using a mix of html and javascript, while the backend is python. The reason for this is listed [here](https://stgit.dcs.gla.ac.uk/apse-group/apse-key-value-app/-/wikis/ADR:-Web-framework)    
The database uses sqlite [Read More](https://stgit.dcs.gla.ac.uk/apse-group/apse-key-value-app/-/wikis/ADR:-Application's-DBMS)

## Support
Support can come from our wiki page.
most noticeably: [Additional Resources](https://stgit.dcs.gla.ac.uk/apse-group/apse-key-value-app/-/wikis/Online-Tutorials-and-additional-resources)


## Roadmap
Our original roadmap was to get the functionality down to base. As it stands, we are looking into logging in as a user to the application and reworking the schema to allow for an extra table for the users.


## Authors and acknowledgment
Alastair Hood, Rayaan Syyed, Connor Crookston, Abdu Khan
