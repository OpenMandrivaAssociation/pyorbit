%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Python bindings for ORBit2
Name:		pyorbit
Version:	2.24.0
Release:	17
License:	LGPLv2+
Group:		Development/GNOME and GTK+
Url:		ftp://ftp.gnome.org/pub/GNOME/sources/pyorbit/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/pyorbit/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		pyorbit-2.24.0-linkage.patch
Patch1:		pyorbit-2.24.0-link-against-python.patch
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libIDL-2.0)
BuildRequires:	pkgconfig(ORBit-2.0)
BuildRequires:	pkgconfig(ORBit-imodule-2.0)
BuildRequires:	pkgconfig(python2)

%description
pyorbit is an extension module for python that gives you access
to the ORBit2 CORBA ORB.

%package	devel
Summary:	Files needed to build wrappers for ORBit2 addon libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description	devel
This package contains files required to build wrappers for ORBit2 addon
libraries so that they interoperate with pyorbit

%prep
%setup -q
%autopatch -p1
autoreconf -fi

%build
export PYTHON=%{__python2}
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README ChangeLog
%{python2_sitearch}/*

%files devel
%dir %{_includedir}/pyorbit-2
%{_includedir}/pyorbit-2/*.h
%{_libdir}/pkgconfig/*.pc

