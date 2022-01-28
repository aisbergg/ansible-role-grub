# Changelog

All notable changes to this project will be documented in this file.

- [2.1.0 (2022-01-28)](#2.1.0-2022-01-28)
- [2.0.0 (2021-10-11)](#200-2021-10-11)
- [1.1.1 (2020-05-28)](#111-2020-05-28)
- [1.1.0 (2020-05-18)](#110-2020-05-18)
- [1.0.2 (2020-04-11)](#102-2020-04-11)
- [1.0.1 (2020-03-01)](#101-2020-03-01)

---

<a name="2.1.0"></a>
## [2.1.0](https://github.com/aisbergg/ansible-role-grub/compare/v2.0.0...2.1.0) (2022-01-28)

### CI Configuration

- fix automatic release and publish process

### Chores

- include changelog in bump commits
- add 'molecule' to ansible-lint exclude list
- remove old boolean test (is now available in Jinja directly)
- update changelog template
- **requirements.yml:** add role requirements


<a name="2.0.0"></a>
## [2.0.0](https://github.com/aisbergg/ansible-role-grub/compare/v1.1.1...v2.0.0) (2021-10-11)

### CI Configuration

- add Github action for automatic releases

### Chores

- update changelog
- update development configs
- **.pre-commit-config.yaml:** bump pre-commit hook versions
- **CHANGELOG.tpl.md:** update changelog template

### Code Refactoring

- use full name
- drop support for Ansible < 2.10


<a name="1.1.1"></a>
## [1.1.1](https://github.com/aisbergg/ansible-role-grub/compare/v1.1.0...v1.1.1) (2020-05-28)

### Code Refactoring

- clean up repo


<a name="1.1.0"></a>
## [1.1.0](https://github.com/aisbergg/ansible-role-grub/compare/v1.0.2...v1.1.0) (2020-05-18)

### Code Refactoring

- clean up


<a name="1.0.2"></a>
## [1.0.2](https://github.com/aisbergg/ansible-role-grub/compare/v1.0.1...v1.0.2) (2020-04-11)

### Bug Fixes

- correct Ansible version requirement

### Chores

- add bump2version config
- update changelog

### Features

- rename _grub_config variable


<a name="1.0.1"></a>
## [1.0.1]() (2020-03-01)

Initial Release
