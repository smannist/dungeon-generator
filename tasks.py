from invoke import task


@task
def test(ctx):
    ctx.run("pytest", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/display_dungeon.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)
    ctx.run("coverage html", pty=True)

@task
def report(ctx):
    ctx.run("xdg-open htmlcov/index.html")
