%define		pname	libgtk-java
Summary:	Java interface for the GTK+
Summary(pl.UTF-8):   Wrapper Javy dla GTK+
Name:		java-gtk
Version:	2.10.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtk-java/2.10/%{pname}-%{version}.tar.bz2
# Source0-md5:	b953f9e106727028ab6ca025357212f0
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	java-cairo-devel >= 1.0.8
BuildRequires:	libtool
Obsoletes:	libgtk-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		macros  %{_datadir}/glib-java/macros

%description
Java interface for the GTK+.

%description -l pl.UTF-8
Wrapper Javy dla GTK+.

%package devel
Summary:	Header files for java-gtk library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki java-gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.7
Requires:	java-cairo-devel >= 1.0.8
Obsoletes:	libgtk-java-devel

%description devel
Header files for java-gtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki java-gtk.

%package doc
Summary:	Reference documentation and examples for java-gtk
Summary(pl.UTF-8):   Szczegółowa dokumentacja i przykłady dla java-gtk
Group:		Documentation

%description doc
Reference documentation and examples for java-gtk.

%description doc -l pl.UTF-8
Szczegółowa dokumentacja i przykłady dla java-gtk.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I macros -I %{macros}
%{__automake}
%{__autoconf}
%configure \
	GCJFLAGS="%{rpmcflags}" \
	--without-javadocs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}/examples \
        $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/examples/*.in

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libgtk*-2.10.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkjava.so
%attr(755,root,root) %{_libdir}/libgtkjni.so
%{_datadir}/%{pname}
%{_includedir}/%{pname}
%{_javadir}/*.jar
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{pname}-%{version}
%{_examplesdir}/%{name}-%{version}
