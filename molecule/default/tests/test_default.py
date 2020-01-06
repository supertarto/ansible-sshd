import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_sshd_is_installed(host):
    sshd = host.package("ssh")
    assert sshd.is_installed


def test_sshd_is_running_and_enabled(host):
    sshd = host.service("ssh")
    assert sshd.is_running
    assert sshd.is_enabled