Name:           libfprint-tod-goodix-550a

Version:        0.0.9
Release:        %autorelease
Summary:        Repackaged driver module binary from Lenovo for Goodix 0x27C6 0x550A fingerprint reader

License:        Redistributable, no modification permitted
URL:            https://support.lenovo.com/ca/en/downloads/ds560884-goodix-fingerprint-driver-for-linux-thinkpad-e14-gen-4-e15-gen-4
Source0:        https://github.com/QuanTrinhCA/libfprint-tod-goodix-550a/raw/main/libfprint-tod-goodix-550a-%{version}.tar.gz

Requires:       libfprint-tod

%global debug_package %{nil}

%description
Repackaged Goodix driver module from Lenovo for fingerprint reader to support 0x27C6 0x550A.

%prep
%setup -q

%build

%install
install -p -d -m 0755 %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -m 0644 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -p -d -m 0755 %{buildroot}%{_usr}/lib/udev/rules.d/
install -m 0644 lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules %{buildroot}%{_usr}/lib/udev/rules.d/

%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so
%{_usr}/lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules

%changelog
%autochangelog
