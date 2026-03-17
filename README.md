# sbctl-kernel-sign

RPM filetrigger that automatically signs kernel images and EFI binaries
via `sbctl-batch-sign` after any kernel installation or update.

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