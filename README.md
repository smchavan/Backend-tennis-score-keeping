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


## Guidelines for Pair-Programming

- The driver is the person who is at the keyboard and mouse
- The navigator is the person who is thinking out loud, actively collaborating with the driver about the next step, and helping guide the development
- Trade-off driver and navigator roles often, at least daily, or every hour for longer work sessions.
- Take time to make sure you're on the same page
