Summary:	Python bindings for ORBit2
Name:		pyorbit
Version:	2.24.0
Release:	9
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/pyorbit/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		pyorbit-2.24.0-linkage.patch
Requires:	ORBit2 >= 2.4.4
Requires:	libIDL >= 0.7.1
Requires:	glib2 >= 1.3.10
Buildrequires:	python-devel
Buildrequires:	libORBit2-devel >= 2.4.4
Buildrequires:	libIDL-devel >= 0.7.1
Buildrequires:	glib2-devel >= 1.3.10

%description
pyorbit is an extension module for python that gives you access
to the ORBit2 CORBA ORB.

%package	devel
Summary:	Files needed to build wrappers for ORBit2 addon libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%release
Requires:	libORBit2-devel

%description	devel
This package contains files required to build wrappers for ORBit2 addon
libraries so that they interoperate with pyorbit

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README ChangeLog
%{python_sitearch}/*

%files devel
%dir %{_includedir}/pyorbit-2
%{_includedir}/pyorbit-2/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.24.0-7mdv2011.0
+ Revision: 667908
- mass rebuild

* Sun Oct 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.24.0-6mdv2011.0
+ Revision: 591063
- rebuild for python-2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.24.0-5mdv2010.1
+ Revision: 523756
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.24.0-4mdv2010.0
+ Revision: 426792
- rebuild

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 2.24.0-3mdv2009.1
+ Revision: 333727
- link against python

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.24.0-2mdv2009.1
+ Revision: 319509
- rebuild with python 2.6

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287367
- new version
- update license

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.14.3-3mdv2009.0
+ Revision: 225127
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.14.3-2mdv2008.1
+ Revision: 179392
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Sat May 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-1mdv2008.0
+ Revision: 31515
- new version


* Sun Feb 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
+ Revision: 125668
- new version

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.1-2mdv2007.1
+ Revision: 87916
- Import pyorbit

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.1-2mdv2007.1
- Rebuild

* Tue Jun 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.1-1mdv2007.0
- New release 2.14.1

* Tue Apr 11 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.0-1mdk
- Release 2.14.0
- use mkrel

* Wed Aug 24 2005 Abel Cheung <deaddog@mandriva.org> 2.0.1-3mdk
- Rebuild

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 2.0.1-2mdk
- Rebuild for new python

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.1-1mdk
- New release 2.0.1

* Fri May 14 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.0-2mdk
- fix deps

