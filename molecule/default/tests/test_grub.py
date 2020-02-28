import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    # check if packages are present/absent
    if host.system_info.distribution == "ubuntu":
        assert host.package("grub2").is_installed
        assert not host.package("os-prober").is_installed
    elif host.system_info.distribution == "centos":
        assert host.package("grub2-common").is_installed

    # check if locale is set
    grub_conf = host.file("/etc/default/grub")
    lc_vars = {
        "GRUB_TIMEOUT": "10",
        "GRUB_DISTRIBUTOR": "\"Foo\"",
    }
    for k, v in lc_vars.items():
        assert grub_conf.contains("{}={}".format(k, v))
