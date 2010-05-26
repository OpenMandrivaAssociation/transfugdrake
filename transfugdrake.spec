%define name transfugdrake
%define version 1.9.2

Summary: Migration wizard
Name: %{name}
Version: %{version}
Release: %mkrel 1
Source0: %{name}-%{version}.tar.lzma
License: GPL
Group: System/Configuration/Other
Url: http://svn.mandriva.com/svn/soft/transfugdrake
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: migration-assistant

%description
Transfugdrake is a wizard to migrate documents and settings from
Windows to Mandriva Linux.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_sbindir}/%{name}
%{_prefix}/lib/libDrakX/transfugdrake.pm
%{_prefix}/lib/libDrakX/icons/*.png
