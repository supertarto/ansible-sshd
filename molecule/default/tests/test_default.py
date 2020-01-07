import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_myvar_using_get_variables(host):
    ansible_variables = host.ansible.get_variables()
    assert 'sshd_service_name' in ansible_variables
    assert 'sshd_packages' in ansible_variables


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_sshd_is_installed(host):
    ansible_variables = host.ansible.get_variables()
    sshd = ansible_variables['sshd_packages']
    assert sshd.is_installed


def test_sshd_is_running_and_enabled(host):
    ansible_variables = host.ansible.get_variables()
    sshd = ansible_variables['sshd_service_name']
    assert sshd.is_running
    assert sshd.is_enabled
