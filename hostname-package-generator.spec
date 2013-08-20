Name: hostname-package-generator
Version: __VERSION__
Release: 1__EXTRAREV__
Summary: Generate hostname RPM package
Group: Applications/System
License: GPL
URL: https://github.com/yadt/hostname-package-generator
Source0: %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: rpm, rpm-build

%description
hostname-package is an RPM generator that creates and installs an RPM package
with the hostname of the current system as an RPM Provides.

This is used to export the hostname of a system into the RPM database to be
able to pin configuration RPMs to their intended host.

%prep
%setup -q

%build
make test

%install
umask 0002
rm -rf $RPM_BUILD_ROOT
install -m 0755 hostname-package -D $RPM_BUILD_ROOT/usr/bin/hostname-package

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/hostname-package
