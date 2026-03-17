# sbctl-kernel-sign

kernel-install plugin that automatically signs kernel images and EFI binaries
via `sbctl-batch-sign` after any kernel installation or update.

## How it works

Installs `/etc/kernel/install.d/91-sbctl.install` which overrides the broken
default sbctl plugin for CachyOS kernel layout. The plugin is called by
`kernel-install` via `%posttrans` scriptlet in `kernel-cachyos-core`.

## Requirements

- Fedora with [CachyOS kernel COPR](https://copr.fedorainfracloud.org/coprs/bieszczaders/kernel-cachyos/)
- [sbctl COPR](https://copr.fedorainfracloud.org/coprs/chenxiaolong/sbctl/)
- `cachyos-settings` (provides `sbctl-batch-sign`)
- Secure Boot keys already enrolled via `sbctl`

## Installation
```bash
dnf copr enable hilltty/sbctl-kernel-sign
dnf install sbctl-kernel-sign
```

## License

MIT