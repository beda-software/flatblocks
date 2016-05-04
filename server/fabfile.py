from fabric.api import local, env

env.docker_compose_file = ''


def ci(test_args=''):
    env.docker_compose_file = '-f docker-compose.test.yml'
    build()
    start()
    test(coverage='report', test_args=test_args)
    stop()


def build():
    local("docker build -t api-flatblocks-core .")


def start():
    local("docker-compose {0} up -d db".format(env.docker_compose_file))


def test(coverage=None, test_args=''):
    cmd = "./manage.py test --no-input {0}".format(test_args)

    if coverage:
        cmd = "bash -c 'coverage run {0} && coverage {1}'".format(cmd, coverage)

    local("docker-compose {0} run --rm server {1}"
          .format(env.docker_compose_file, cmd))


def stop():
    local("docker-compose {0} stop".format(env.docker_compose_file))
