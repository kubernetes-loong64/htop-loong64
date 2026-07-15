Name: htop
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Interactive process viewer (loong64)
License: GPL-2.0
URL: https://github.com/htop-dev/htop
BugURL: https://github.com/htop-dev/htop/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>
Requires: ncurses

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
htop is a cross-platform interactive process viewer.
It requires ncurses.

This package provides htop for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# Pre-built binary, nothing to compile

%install
mkdir -p %{buildroot}/usr/local/bin/
install -m 755 htop %{buildroot}/usr/local/bin/htop

mkdir -p %{buildroot}/usr/local/share/man/man1/
install -m 644 htop.1 %{buildroot}/usr/local/share/man/man1/htop.1

mkdir -p %{buildroot}/usr/local/share/icons/hicolor/scalable/apps/
install -m 644 htop.svg %{buildroot}/usr/local/share/icons/hicolor/scalable/apps/htop.svg

mkdir -p %{buildroot}/usr/local/share/pixmaps/
install -m 644 htop.png %{buildroot}/usr/local/share/pixmaps/htop.png

mkdir -p %{buildroot}/usr/local/share/applications/
install -m 644 htop.desktop %{buildroot}/usr/local/share/applications/htop.desktop

mkdir -p %{buildroot}/usr/local/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/local/share/licenses/%{name}/LICENSE

%files
%license /usr/local/share/licenses/%{name}/LICENSE
/usr/local/bin/htop
/usr/local/share/man/man1/htop.1*
/usr/local/share/icons/hicolor/scalable/apps/htop.svg
/usr/local/share/pixmaps/htop.png
/usr/local/share/applications/htop.desktop

%changelog
