Name:           sbctl-kernel-sign
Version:        1.0
Release:        1%{?dist}
Summary:        RPM filetrigger for automatic kernel signing via sbctl
License:        MIT
URL:            https://github.com/hilltty/sbctl-kernel-sign

Requires:       cachyos-settings
Requires:       sbctl

BuildArch:      noarch

%description
Automatically signs kernel images and EFI binaries via sbctl-batch-sign
after any kernel installation using a kernel-install plugin.
Overrides the broken 91-sbctl.install for CachyOS kernel layout.
Designed for Fedora with CachyOS kernel from COPR and sbctl Secure Boot manager.

%install
mkdir -p %{buildroot}/etc/kernel/install.d
cat > %{buildroot}/etc/kernel/install.d/91-sbctl.install << 'EOF'
#!/bin/bash
COMMAND="$1"

[ "$COMMAND" = "add" ] || exit 0

if ! command -v sbctl-batch-sign &>/dev/null; then
    echo "sbctl-kernel-sign: sbctl-batch-sign not found, skipping."
    exit 0
fi

echo "sbctl-kernel-sign: new kernel detected, signing EFI binaries..."
if sbctl-batch-sign; then
    echo "sbctl-kernel-sign: done."
else
    echo "sbctl-kernel-sign: warning: sbctl-batch-sign failed, check manually."
fi
EOF
chmod 755 %{buildroot}/etc/kernel/install.d/91-sbctl.install

%files
/etc/kernel/install.d/91-sbctl.install

%changelog
* Mon Mar 17 2025 hilltty <49129010+hilltty@users.noreply.github.com> - 1.0-1
- Initial release