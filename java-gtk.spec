%define	pname	libgtk-java
Summary:	Java interface for the GTK+
Summary(pl):	Wrapper Java dla GTK+
Name:		java-gtk
Version:	2.4.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.4/%{pname}-%{version}.tar.bz2
# Source0-md5:	647690c75e084a7e785860f443c9a78b
Patch0:		%{name}-DESTDIR.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libgcj-devel >= 5:3.3.2
Obsoletes:	libgtk-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for the GTK+.

%description -l pl
Wrapper Java dla GTK+.

%package devel
Summary:	Header files for java-gtk library
Summary(pl):	Pliki nag³ówkowe biblioteki java-gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgtk-java-devel

%description devel
Header files for java-gtk library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-gtk.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%build
%{__aclocal} -I macros
%{__autoconf}
%configure \
    GCJ_JAR=`echo /usr/share/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_javadir}/*.jar
%{_datadir}/%{pname}
%{_pkgconfigdir}/*.pc
