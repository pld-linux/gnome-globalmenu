Summary:	Global Menu Bar for GNOME
Name:		gnome-globalmenu
Version:	0.7.6
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://gnome2-globalmenu.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	c56f85e1f02546d3952f1474c9b388b4
URL:		http://code.google.com/p/gnome2-globalmenu/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.16.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Global Menu is the globally-shared menu bar of all applications
launched in your desktop session.

%package devel
Summary: Headers for libgnomemenu
Group:	Development/Libraries

%description devel
Headers for libgnomemenu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I autotools
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README README.GNOME README.XFCE
%{_sysconfdir}/gconf/schemas/gnome-globalmenu.schemas
%attr(755,root,root) %{_libdir}/GlobalMenu.PanelApplet
%attr(755,root,root) %{_libdir}/bonobo/servers/GlobalMenu_PanelApplet.server
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libglobalmenu-gnome-0.7.6.so
%attr(755,root,root) %{_libdir}/libgnomenu-0.7.6.so.2.0.0
%{_mandir}/man1/gnome-globalmenu.1*
%{_pixmapsdir}/globalmenu.png

%files devel
%{_libdir}/libgnomenu.la
%{_libdir}/libgnomenu.so
%{_pkgconfigdir}/libgnomenu.pc
%{_includedir}/libgnomenu/libgnomenu.h

%post -p /sbin/ldconfig
