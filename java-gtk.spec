%define ver	0.5.0
%define rel	2

Summary: Java-GTK is a preliminary version of Java wrappers for GTK.
Name: java-gtk
Version: %{ver}
Release: %{rel}
Requires: gtk+ >= 1.2.0
Copyright: GPL
Group: ""
Source: java-gtk-%{ver}.tar.gz
URL: http://java-gnome.sourceforge.net/
Packager: Jean van Wyk <jeanvanwyk@iname.com>

%description
This is a very preliminary version of Java wrappers for GTK and should be 
deamed ALPHA although it might work for you.

%prep
%setup

%build
./configure --prefix %{_prefix} --with-gtk-only
make

%install
make install

%files
%doc AUTHORS COPYING INSTALL README NEWS TODO THANKS doc
%{_prefix}/lib/libGTKJava.so.0.5.0
%{_prefix}/lib/libGTKJava.so
%{_prefix}/share/java-gtk/
