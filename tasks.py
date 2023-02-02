import pty
from invoke import task


@task
def test(ctx):
    ctx.run("pytest", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
