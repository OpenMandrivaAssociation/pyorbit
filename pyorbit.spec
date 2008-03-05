%define pyver 2.3
Summary: Python bindings for ORBit2
Name: pyorbit
Version: 2.14.3
Release: %mkrel 2
License: LGPL
Group: Development/GNOME and GTK+
URL: ftp://ftp.gnome.org/pub/GNOME/sources/pyorbit/
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Requires: ORBit2 >= 2.4.4
Requires: libIDL >= 0.7.1
Requires: glib2 >= 1.3.10
Requires: python >= %pyver
Buildrequires: libpython-devel >= %pyver
Buildrequires: libORBit2-devel >= 2.4.4
Buildrequires: libIDL-devel >= 0.7.1
Buildrequires: glib2-devel >= 1.3.10

%description
pyorbit is an extension module for python that gives you access
to the ORBit2 CORBA ORB.

%package devel
Summary: Files needed to build wrappers for ORBit2 addon libraries
Group: Development/GNOME and GTK+
Requires: %{name} = %{version}-%release
Requires: libORBit2-devel

%description devel
This package contains files required to build wrappers for ORBit2 addon
libraries so that they interoperate with pyorbit

%prep
%setup -q

%build
# gw: the configure macro doesn't work
./configure --prefix=%_prefix --libdir=%_libdir
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;

%clean
rm -rf %buildroot

%files
%defattr(755, root, root, 755)
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/python?.?/site-packages/*

%files devel
%defattr(755, root, root, 755)
%dir %{_includedir}/pyorbit-2
%{_includedir}/pyorbit-2/*.h
%{_libdir}/pkgconfig/*.pc


