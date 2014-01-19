# Django Heroku Skeleton

This is a minimal Django skeleton app that will is set up for local
development and ready to deploy to Heroku.


## Setting up for local development.

Download/fork/clone this repo to your local machine and then cd into
the root of the repository.

Create the virtualenv and install the requirements &ndash;

    virtualenv venv
    . ./venv/bin/activate
    pip install -r requirements.txt


Set up the local project &ndash;

    python app/manage.py syncdb --settings=app.settings.local
    python app/manage.py collectstatic --settings=app.settings.local
    
You can now runserver &ndash;

    python app/manage.py runserver --settings=app.settings.local

Once it's up and running, you can carve the project to your needs. The
static assets are in `srv/assets` and you can use a one liner shell
command to sync the assets to static as you develop ( _remember to
activate your virtualenv `./venv/bin/activate`_ ) &ndash;
    
    while true; do python app/manage.py collectstatic --noinput --settings=app.settings.local; sleep 1; done

## Deploying to Heroku

Make sure you've done the following three things

* have a Heroku account
* have the Heroku toolbelt installed
* have auth'd against Heroku using `heroku login` command.

Create the app

    heroku apps:create sensible-app-name --region eu

Just double check that it's likely to run on Heroku by using the
foreman command &ndash;

    foreman start

If all is good, do your first deploy to Heroku

    git push heroku master

If you check your deploy once it's completed it will fail.
Now scale up the worker to one

    heroku ps:scale web=1
