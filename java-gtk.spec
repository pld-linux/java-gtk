%define		pname	libgtk-java
Summary:	Java interface for the GTK+
Summary(pl):	Wrapper Java dla GTK+
Name:		java-gtk
Version:	2.6.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtk-java/2.6/%{pname}-%{version}.tar.bz2
# Source0-md5:	17d558597494261ff92b155a10a27d20
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	gtk+2-devel >= 2:2.6.0
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

%package doc
Summary:        Reference documentation and examples for java-gtk
Summary(pl):    Szczegó³owa dokumentacja i przyk³ady dla java-gtk
Group:          Documentation

%description doc
Reference documentation and examples for java-gtk.

%description doc -l pl
Szczegó³owa dokumentacja i przyk³ady dla java-gtk.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__aclocal} -I macros
%{__autoconf}
%configure \
	GCJ_JAR=`echo %{_datadir}/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}/examples \
        $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.in

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libgtk*-2.6.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkjava.so
%attr(755,root,root) %{_libdir}/libgtkjni.so
%{_datadir}/%{pname}
%{_includedir}/%{pname}/*.h
%{_javadir}/*.jar
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{pname}-%{version}
%{_examplesdir}/%{name}-%{version}
