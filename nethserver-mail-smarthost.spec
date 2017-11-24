Summary: Configuration for smart host
Name: nethserver-mail-smarthost
Version: 1.0.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-base
Requires: cyrus-sasl-plain, postfix

BuildRequires: nethserver-devtools

%description
Smarthost configuration for sending mail, based on Postfix.

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%doc README.rst
%dir %{_nseventsdir}/%{name}-update

%changelog
* Fri Nov 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- GSSAPI error from Postfix smarthost client - Bug NethServer/dev#5366

* Mon Mar 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.1.1-1
- Migration from sme8 NethServer/dev#5196

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 0.1.0-1
- First NS7 release

