from invoke import Collection

from provision import ci, django, docker, git, linters, project, system, tests

ns = Collection(
    ci,
    django,
    docker,
    linters,
    system,
    project,
    tests,
    git,
)

# Configurations for run command
ns.configure(
    {
        "run": {
            "pty": True,
            "echo": True,
        },
    },
)
