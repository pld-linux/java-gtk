Summary:	Java-GTK is a preliminary version of Java wrappers for GTK
Summary(pl):	Wstêpna wersja javowych wrapperów do GTK
Name:		java-gtk
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/java-gnome/%{name}-%{version}.tar.gz
# Source0-md5:	bd97ee300dca6393b8b6f641ae7cdf87
URL:		http://java-gnome.sourceforge.net/
Requires:	gtk+ >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very preliminary version of Java wrappers for GTK and should
be deamed ALPHA although it might work for you.

%description -l pl
To bardzo wstêpna wersja javowych wrapperów do GTK - jest to wersja
ALFA, nawet je¶li mo¿e dzia³aæ.

%prep
%setup -q

%build
%configure \
	--with-gtk-only
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO THANKS doc
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gtk
