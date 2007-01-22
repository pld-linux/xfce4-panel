Summary:	Next generation panel for Xfce
Summary(pl):	Panel nowej generacji dla Xfce
Name:		xfce4-panel
Version:	4.4.0
Release:	1
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	c46925d2df393dba8f16979ba87d4776
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
Requires:	%{name}-libs = %{version}-%{release}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce-mcs-manager >= %{version}
Requires:	xfce4-icon-theme
Obsoletes:	xfce4-systray
Obsoletes:	xfce4-themes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the Xfce desktop environment.

%description -l pl
xfce4-panel to panel dla ¶rodowiska Xfce.

%package apidocs
Summary:	Xfce panel API documentation
Summary(pl):	Dokumentacja API panelu Xfce
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Xfce panel API documentation.

%description apidocs -l pl
Dokumentacja API panelu Xfce.

%package libs
Summary:	xfce4panel library
Summary(pl):	Biblioteka xfce4panel
Group:		Development/Libraries

%description libs
This package contains xfce4panel library.

%description libs -l pl
Pakiet ten zawiera bibliotekê xfce4panel.

%package devel
Summary:	Header files for building Xfce panel plugins
Summary(pl):	Pliki nag³ówkowe do budowania wtyczek panelu Xfce
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfcegui4-devel >= %{version}
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for building Xfce panel plugins.

%description devel -l pl
Pliki nag³ówkowe do budowania wtyczek panelu Xfce.

%prep
%setup -q
%patch0 -p1

mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtk-doc \
	--enable-startup-notification \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{,xfce4/{mcs-plugins,panel-plugins}}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README README.Kiosk README.Plugins
%attr(755,root,root) %{_bindir}/*

%dir %{_sysconfdir}/xdg/xfce4/panel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/clock-14.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-7.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-8.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-9.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-10.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/panels.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/systray-4.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/xfce4-menu-5.rc
%dir %{_libdir}/xfce4/panel-plugins
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/panel-plugins
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop

%{_datadir}/xfce4/doc/C/*
%docdir %{_datadir}/xfce4/doc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxfce4panel

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel.so
%{_includedir}/xfce4/libxfce4panel
%{_pkgconfigdir}/*.pc
