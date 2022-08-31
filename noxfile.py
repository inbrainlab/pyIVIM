import nox


@nox.session(python=["3.9"])
def tests(session):
    session.run("pip", "install", "pytest", "--quiet")
    session.run("pip", "install", "coverage", "--quiet")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")


@nox.session
def lint(session, reuse_venvs=True):
    session.run_always("poetry", "install", external=True)
    session.run("pip", "install", "black", "--quiet")
    session.run("pip", "install", "flake8", "--quiet")
    session.run("black", "--check", ".")
    session.run("flake8", "--config=.flake8", ".")


@nox.session
def typing(session, reuse_venvs=True):
    session.run("pip", "install", "mypy", "--quiet")
    # session.run("poetry", "install")
    session.run("mypy", "--config-file=mypy.ini", ".")
