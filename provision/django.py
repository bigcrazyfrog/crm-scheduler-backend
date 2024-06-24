from invoke import task

from . import common, docker, system


def wait_for_database(context):
    """Ensure that database is up and ready to accept connections.

    Function called just once during subsequent calls of management commands.

    """
    if hasattr(wait_for_database, "_called"):
        return
    docker.up(context)
    context.run(
        " ".join(["manage.py", "wait_for_database", "--stable 0"]),
    )
    wait_for_database._called = True  # pylint: disable=protected-access


@task
def manage(context, command):
    """Run ``manage.py`` command.

    This command also handle starting of required services and waiting DB to
    be ready.

    Args:
        context: Invoke context
        command: Manage command

    """
    return context.run(
        " ".join(["python", "manage.py", command]),
    )


@task
def makemigrations(context):
    """Run makemigrations command and chown created migrations."""
    common.success("Django: Make migrations")
    manage(context, "makemigrations")


@task
def migrate(context):
    """Run ``migrate`` command."""
    common.success("Django: Apply migrations")
    manage(context, "migrate")


@task
def run(context):
    """Run development web-server."""
    common.success("Running web app")
    manage(context, "runserver 0.0.0.0:8000")
