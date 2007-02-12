%define	pname	libgtk-java
Summary:	Java interface for the GTK+
Summary(pl.UTF-8):   Wrapper Java dla GTK+
Name:		java-gtk
Version:	2.3.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.3/%{pname}-%{version}.tar.bz2
# Source0-md5:	72e67744126d48f4e893fa71cda107cd
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libgcj-devel >= 3.3.2
BuildRequires:	slocate
Obsoletes:	libgtk-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for the GTK+.

%description -l pl.UTF-8
Wrapper Java dla GTK+.

%package devel
Summary:	Header files for java-gtk library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki java-gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgtk-java-devel

%description devel
Header files for java-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki java-gtk.

%prep
%setup -q -n %{pname}-%{version}

%build
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
%{_datadir}/java-gnome
