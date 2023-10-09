# Ansible SSHD
[![CI](https://github.com/supertarto/ansible-sshd/workflows/CI/badge.svg?event=push)](https://github.com/supertarto/ansible-sshd/actions?query=workflow%3ACI)

Ansible role to install and configure SSHD

## Requirements
None
## Tested plateform
* Debian 10 (Buster)
* Debian 11 (Bullseye)
* Debian 12 (Bookworm)

## Role variables

Do you need a banner ? If set to true, the banner will be created in the path you choose here. 

```yaml
sshd_banner_needed: true
sshd_banner_path: /etc/ssh/sshd-banner
```

Content of the sshd banner file. Can be a multiline text.

```yml
sshd_banner_content: |
  This is a sshd banner
  a multiline text
```

The name of the sshd service.

```yaml
sshd_service_name: ssh
```

Path where the sshd_config file will be.

```yaml
sshd_config_path: /etc/ssh/sshd_config
```

List of options in the sshd_config file. Those are the default value.

```yml
sshd_port: 22
sshd_listen_address:
  - 0.0.0.0
sshd_syslog_facility: AUTH
sshd_log_level: INFO
sshd_login_grace_time: 2m
sshd_permit_root_login: "no"
sshd_strict_mode: "yes"
sshd_max_auth_tries: 6
sshd_max_sessions: 10
sshd_authorized_keys_file:
  - "%h/.ssh/authorized_keys"
sshd_allow_users: []
sshd_password_authentication: "yes"
sshd_permit_empty_password: "no"
sshd_x11_forwarding: "yes"
```

Use for Match User and Match group, to force SFTP. Set to "true" if you want to use those features.

```yml
sshd_use_sftp_chroot_user: false
sshd_sftp_chroot_user: "sftpuser"
sshd_sftp_chroot_user_directory: "/home/{{ sshd_sftp_chroot_user }}"

sshd_use_sftp_chroot_group: false
sshd_sftp_chroot_group: "sftpgroup"
sshd_sftp_chroot_group_directory: "/my/folder/chroot"
```
## Example(s)

```yml
---
- hosts: somehost
  roles:
    - supertarto.sshd
  vars:
    sshd_password_authentication: "yes"
    sshd_permit_empty_password: "no"
    sshd_x11_forwarding: "yes"

```

## Installation

```bash
ansible-galaxy role install supertarto.sshd
```

## License
GPL V3.0
