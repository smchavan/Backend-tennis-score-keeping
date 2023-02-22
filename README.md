# Backend-tennis-score-keeping


## Goal


* Improve our understanding of Flask & SQL Alchemy with repetition

In this activity, we will build a Backend-tennis-score-keeping API. This API will store information about different users,matches created by that user, players, set stats and player stats

We will focus on creating RESTful endpoints for CRUD operations.

## Tips

- Don't forget to work in a virtual environment
- Put endpoints in `app/routes.py`
- Add configuration, such as registering blueprints or configuring databases, in `app/__init__.py`
- Commit and push often

## One-Time Project Setup

Follow these directions once, a the beginning of your project:

1. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

2. In Github click on the "Fork" button in github and fork the repository to your Github account.  This will make a copy of the project in your github account. 

![Fork Button](images/fork.png)

3. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `viewing-party`, and then puts the project into this new folder.  Make sure you are cloning from your copy of the project and not the class version (ada-cX).

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

4. Move your location into this project folder

```bash
$ cd Backend-tennis-score-keeping
```

5. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

6. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:

- [ ] `cd` into your `projects` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `Backend-tennis-score-keeping` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Github Setup

1. Choose one member to fork the Solar System API repo 
1. Add all members to the forked repo as collaborators (through the repo settings)
1. All group members should clone this new, forked, group repo and `cd` into it
1. Discuss good git hygiene: 
    * Make regular commits
    * Push commits before switching driver
    * Pull before starting to drive

## ERD for the project
 https://drive.google.com/file/d/1HfrKYCNisBVDIIxI-FUXMm36QxXp4nsm/view?usp=sharing
## Endpoint Documents for the project for Sample request and response Bodies
https://docs.google.com/document/d/1pN75cD_Cc_7sv7mDxHbIkN-oYhhEofJXBM8PsI6oQWo/edit?usp=sharing
## API Document With CRUD endpoint table
https://docs.google.com/spreadsheets/d/1oZAXevK7zXG4Id6_c5rvnNiWDYDM4FFPTxiEg47gfH0/edit?usp=share_link
## Project Directions

- Write all the models for 
     * user
     * player
     * match
     * set
     * game
     * stat
     * player_match
 - Write all the CRUD endpoints for all the models 
 - Write/Create nested endpoints like 
    * A user creating a match
    * A user creating players
    * Adding a set to a match
    * Adding a game to a set
    * Adding stats for the two players for a set
    * Getting all the matches created by the user
    * Getting all the players created by the user
    * Getting all the sets of a match
    * Getting all games of a set
    * Getting all stats for a player
    * Getting all stats for a set
    

#### Database Setup/Update

1. Pull down all new git commits
1. Activate the virtual environment
1. Create the database `tennis_development`
2. Create the database `tennis_test`
3. Run `flask db migrate`
4. Run `flask db upgrade`
5. Run `flask run` to confirm that the API is running as expected

## Steps for Deploying to Heroku
 - Create a Heroku account and get access to the Heroku CLI
 - Configure our Flask project for Heroku
 - Commit our new configurations
 - Create a Heroku app via the CLI
 - Push code to the Heroku remote
 - Create a database in Heroku via the CLI
 - Set the environment variables for Heroku
 - Setup and initialize the database in Heroku via the CLI
 - Verify
 ### Folowwing Commands can be reffered from your terminal in mac
 - $ heroku login
 - We will use a Python package named gunicorn  to launch our Flask API on Heroku.
gunicorn is capable of running Flask apps so that they can handle multiple simultaneous requests, which is very important for production web applications.
We should confirm that the package gunicorn is in the project's requirements.txt file.
If gunicorn does not appear in our requirement.txt, we can add it by installing it locally with:
- (venv) $ pip install gunicorn
- After it has installed, we can update our requirements.txt by running:
- (venv) $ pip freeze > requirements.txt
- Create a Procfile for Heroku
Procfile  is a file specifically used in codebases deployed on Heroku.
We'll use our Procfile to define how to start our Flask web server.
First, create a Procfile inside the project root. This file must be named exactly Procfile, with no file extension.
- $ touch Procfile
- Then, fill the Procfile with this content:
web: gunicorn 'app:create_app()'
- Commit your changes to your local main and then push to github
- cd in your app 
- We can create a Heroku app with an automatically generated app name using:
   $ heroku create your-app-name
- It will cretae your app and you can check on your Heroku Dashboard
- Verify the New Heroku Remote
Creating a Heroku app will add a new Git remote to our project! A Git remote is a destination to which we can git push! The new Git remote will be named heroku. This Git remote points exactly to where Heroku keeps and serves our code! Confirm that we have a heroku remote by running this command:
- $ git remote -v
- $git status (to check your current branch)
- $ git push heroku main:main
- Create a Database in Heroku
Now that we've created our Heroku app for the first time, we need to tell the app that we're interested in adding a Postgres database to our deployed Heroku app.
This command uses the Heroku CLI to add a Postgres database to the app.
- $ heroku addons:create heroku-postgresql:mini
- Verify in the Dashboard
We can verify that our Heroku app has added a Postgres database by checking the Heroku dashboard  .
We can use the Heroku dashboard to view our Heroku app. In the "Overview" tab, in the "Installed add-ons" section, we should see "Heroku Postgres."
- Set Environment Variables in Heroku
Our current app sets the SQLALCHEMY_DATABASE_URI environment variable using our .env file. Our Flask code accesses this environment variable with the code os.environ.get("SQLALCHEMY_DATABASE_URI").
Instead of giving Heroku our .env file, we need to add our environment variables to Heroku using the Heroku dashboard.
- Find the Database URL in Heroku
First, let's find the connection string that will connect to our Heroku database, instead of a local database.
When we added the Postgres database add-on above, Heroku created this connection string.
In the Heroku dashboard, in the "Settings" tab, there is a section titled "Config Vars."
- Once we locate this section, we should:
   * Click "Reveal Config Vars"
   * Find the automatically generated variable named "DATABASE_URL"
   * Copy the value of this connection string
   * Set the Environment Variables in Heroku
     Now, let's set the SQLALCHEMY_DATABASE_URI variable.In the "Config Vars" section:
   * Create a new environment variable named SQLALCHEMY_DATABASE_URI
   * Set the value of this variable to the connection string we copied
- Setup and Initialize the Database in Heroku
   Now that our Flask app is on Heroku and can connect to a database, we need to initialize the database in Heroku once.
   We can run the following:
- $ heroku run flask db upgrade
- Verify using postman as it is a backend app
### Debugging with Heroku 
- Use Heroku Logs to Debug
### Redeploying your app in Heroku
- If you make any changes to your database schema you need to run following commands
     * heroku run flask db migrate
     * heroku run flask db upgrade
- To redeploy your app on Heroku
- $ git push heroku main


## Guidelines for Pair-Programming

- The driver is the person who is at the keyboard and mouse
- The navigator is the person who is thinking out loud, actively collaborating with the driver about the next step, and helping guide the development
- Trade-off driver and navigator roles often, at least daily, or every hour for longer work sessions.
- Take time to make sure you're on the same page
