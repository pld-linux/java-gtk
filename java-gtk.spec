Summary:	Java-GTK is a preliminary version of Java wrappers for GTK
Summary(pl):	Wstêpna wersja javowych wrapperów do GTK
Name:		java-gtk
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://download.sourceforge.net/pub/sourceforge/java-gnome/%{name}-%{version}.tar.gz
URL:		http://java-gnome.sourceforge.net/
Requires:	gtk+ >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

gzip -9nf AUTHORS README NEWS TODO THANKS doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gtk
