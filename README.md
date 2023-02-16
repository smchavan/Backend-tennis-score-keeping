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

## Github Setup

1. Choose one member to fork the Solar System API repo 
1. Add all members to the forked repo as collaborators (through the repo settings)
1. All group members should clone this new, forked, group repo and `cd` into it
1. Discuss good git hygiene: 
    * Make regular commits
    * Push commits before switching driver
    * Pull before starting to drive

## Guidelines for Pair-Programming

- The driver is the person who is at the keyboard and mouse
- The navigator is the person who is thinking out loud, actively collaborating with the driver about the next step, and helping guide the development
- Trade-off driver and navigator roles often, at least daily, or every hour for longer work sessions.
- Take time to make sure you're on the same page

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

#### Database Setup/Update

1. Pull down all new git commits
1. Activate the virtual environment
1. Create the database `tennis_development`
2. Run `flask db migrate`
3. Run `flask db upgrade`
4. Run `flask run` to confirm that the API is running as expected
