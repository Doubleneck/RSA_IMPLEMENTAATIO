from invoke import task

@task
def test(ctx):
    ctx.run("pytest src")

@task(test)
def start(ctx):
    ctx.run("python3 src/index.py", pty = True)

@task
def manual_test(ctx):
    ctx.run("python3 src/iterations.py")

@task
def mr_test(ctx):
    ctx.run("python3 src/millerrabinxtimes.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src")
