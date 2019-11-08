# ansible-sshd
Ansible role to install and configure SSHD

## Tested plateform
* Debian 9 (Stretch)
* Debian 10 (Buster)

## Role variables

Do you need a banner ? If set to true, the banner will be created in the path you choose here. 
```yaml
sshd_banner_needed: true
sshd_banner_path: /etc/ssh/sshd-banner
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

## Examples
## Installation
```
ansible-galaxy install supertarto.sshd
```
## License
GPL V3.0