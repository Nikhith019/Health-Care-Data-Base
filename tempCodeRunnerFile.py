# run.py
from app import create_app, db
from flask.cli import with_appcontext
import click

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    print("Creating tables...")
    db.create_all()
    print("Tables created successfully!")

app = create_app('development')
app.cli.add_command(create_tables)

if __name__ == '__main__':
    app.run(debug=True)
