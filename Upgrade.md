# Uninstall and install latest version to upgrade Docker

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

This command uninstalls docker and it's components.

# Download binaries manually or run steps from [Installation](Documents/Installation.md)

