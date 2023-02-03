import pty
from invoke import task


@task
def test(ctx):
    ctx.run("pytest", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def start(ctx):
    ctx.run("python src/display_dungeon.py", pty=True)
