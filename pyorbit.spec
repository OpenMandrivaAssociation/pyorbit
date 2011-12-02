%define pyver 2.3

Summary: Python bindings for ORBit2
Name: pyorbit
Version: 2.24.0
Release: 8
License: LGPLv2+
Group: Development/GNOME and GTK+
URL: ftp://ftp.gnome.org/pub/GNOME/sources/pyorbit/
Source: %{name}-%{version}.tar.bz2
Patch0: pyorbit-2.24.0-linkage.patch

BuildRequires: libpython-devel >= %pyver
BuildRequires: libORBit2-devel >= 2.4.4
BuildRequires: libIDL-devel >= 0.7.1
BuildRequires: glib2-devel >= 1.3.10
Requires: ORBit2 >= 2.4.4
Requires: python >= %{pyver}

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
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name "*.la" -exec rm {} \;

%files
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/python?.?/site-packages/*

%files devel
%dir %{_includedir}/pyorbit-2
%{_includedir}/pyorbit-2/*.h
%{_libdir}/pkgconfig/*.pc
