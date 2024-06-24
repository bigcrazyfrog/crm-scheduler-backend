from invoke import task

from . import common


@task
def run(context, params=""):
    """Run django tests with ``extra`` args for ``p`` tests.

    `p` means `params` - extra args for tests
    manage.py test <extra>

    """
    common.success("Tests running")
    context.run(f"python manage.py test {params}")
