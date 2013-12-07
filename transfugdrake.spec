%define name transfugdrake
%define version 1.9.2

Summary: Migration wizard
Name: %{name}
Version: %{version}
Release: 12
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-3mdv2011.0
+ Revision: 670728
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-2mdv2011.0
+ Revision: 608041
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.9.2-1mdv2010.1
+ Revision: 546247
- 1.9.2
- translation updates

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-3mdv2010.1
+ Revision: 524235
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.9.1-2mdv2010.0
+ Revision: 427432
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 1.9.1-1mdv2009.1
+ Revision: 367396
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 1.9-1mdv2009.1
+ Revision: 362307
- translation updates

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.8-3mdv2009.1
+ Revision: 351464
- rebuild

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 1.8-2mdv2009.0
+ Revision: 286972
- translation updates

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.7-2mdv2009.0
+ Revision: 225871
- rebuild

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 1.7-1mdv2008.1
+ Revision: 192089
- translation updates
- translation updates

* Thu Mar 13 2008 Olivier Blin <oblin@mandriva.com> 1.5-1mdv2008.1
+ Revision: 187549
- 1.5
- fix detection of partitions using UUID (#38689)
- fix matching windows system path with ntfs-3g
- find disks later not to slow startup
- handle wizcancel more cleanly

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdv2008.1
+ Revision: 179663
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 05 2007 Olivier Blin <oblin@mandriva.com> 1.4-1mdv2008.0
+ Revision: 95625
- 1.4
- disable documents sharing

* Thu Oct 04 2007 Olivier Blin <oblin@mandriva.com> 1.3-1mdv2008.0
+ Revision: 95498
- 1.3
- disable bookmarks and mail sharing
- implement skip buttons

* Wed Oct 03 2007 Olivier Blin <oblin@mandriva.com> 1.2-1mdv2008.0
+ Revision: 95187
- 1.2
- make sure XDG directories are created before starting import

* Wed Oct 03 2007 Olivier Blin <oblin@mandriva.com> 1.1-1mdv2008.0
+ Revision: 95083
- 1.1
- handle WINNT and lowercase system folder (#34377)
- fix ma-import 0.5.1 usage (by specifying --ostype as last option)

* Sun Sep 30 2007 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2008.0
+ Revision: 94062
- 1.0
- really run import if only one linux user and one windows user are detected
- do not pop wait messages

* Fri Sep 28 2007 Olivier Blin <oblin@mandriva.com> 0.9-1mdv2008.0
+ Revision: 93730
- 0.9
- uniquify linux users list (workaround a glibc bug)

* Fri Sep 28 2007 Olivier Blin <oblin@mandriva.com> 0.8-1mdv2008.0
+ Revision: 93723
- 0.8
- use translations (#33677)
- do not try to list windows users if no windows disk is detected
- do not allow to continue if no windows user is detected

* Thu Sep 20 2007 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2008.0
+ Revision: 91320
- 0.7
- strings and translations updates

* Tue Sep 04 2007 Olivier Blin <oblin@mandriva.com> 0.6-1mdv2008.0
+ Revision: 79584
- 0.6
- do not kill import helper after 10 minutes
- add icons

* Wed Aug 01 2007 Olivier Blin <oblin@mandriva.com> 0.5-2mdv2008.0
+ Revision: 57567
- require migration-assistant

* Wed Aug 01 2007 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2008.0
+ Revision: 57556
- rewrite transfugdrake
- Create transfugdrake

