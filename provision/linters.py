from invoke import Exit, UnexpectedExit, task

from . import common

DEFAULT_FOLDERS = "apps tasks.py"


@task
def isort(context, path=DEFAULT_FOLDERS):
    """Run `isort` linter."""
    common.success("Linters: flake8 running")
    context["run"].env["DJANGO_SETTINGS_MODULE"] = "config.settings"
    return context.run(command=f"isort {path} --check-only")


@task
def flake8(context, path=DEFAULT_FOLDERS):
    """Run `flake8` linter."""
    common.success("Linters: flake8 running")
    context["run"].env["DJANGO_SETTINGS_MODULE"] = "config.settings"
    return context.run(command=f"flake8 apps/ {path} --show-source")


# pylint: disable=redefined-builtin
@task
def all(context, path=DEFAULT_FOLDERS):
    """Run all linters."""
    common.success("Linters: running all linters")
    linters = (flake8,)
    failed = []
    for linter in linters:
        try:
            linter(context, path)
        except UnexpectedExit:
            failed.append(linter.__name__)
    if failed:
        common.error(
            f"Linters failed: {', '.join(map(str.capitalize, failed))}",
        )
        raise Exit(code=1)
