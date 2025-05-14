import os
import click
from flask.cli import with_appcontext
from flask_migrate import init as alembic_init
from init import initialize_users
from app.providers.extensions import db

@click.command('init_db')
@with_appcontext
def db_init():
    """Perintah untuk inisialisasi migrasi."""
    migrations_dir = os.path.join(os.getcwd(), 'migrations')
    if os.path.exists(migrations_dir):
        click.echo("Folder 'migrations' sudah ada.")
    else:
        alembic_init()
        click.echo("Inisialisasi migrasi selesai.")

@click.command('seed_db')
@with_appcontext
def db_seed():
    """Menginisialisasi database dengan skema dan data awal."""
    click.echo('Membuat tabel baru...')
    db.create_all()
    
    click.echo('Menginisialisasi data pengguna...')
    initialize_users()
    
    click.echo('Database berhasil diinisialisasi!')