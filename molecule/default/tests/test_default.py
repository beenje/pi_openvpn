import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_openvpn_started_and_enabled(host):
    with host.sudo():
        service = host.service("openvpn")
        assert service.is_running
        assert service.is_enabled
