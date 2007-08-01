%define name transfugdrake
%define version 0.5
%define release %mkrel 1

Summary: Migration wizard
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Configuration/Other
Url: http://svn.mandriva.com/svn/soft/transfugdrake
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
Transfugdrake is a wizard to migrate documents and settings from
Windows to Mandriva Linux.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_sbindir}
install -m755 %{name} %{buildroot}%{_sbindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/%{name}
