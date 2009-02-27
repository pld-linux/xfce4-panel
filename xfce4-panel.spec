Summary:	Next generation panel for Xfce
Summary(pl.UTF-8):	Panel nowej generacji dla Xfce
Name:		xfce4-panel
Version:	4.6.0
Release:	1
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	b4c7cce05cc858d11c9dcd4c2f8dbfdb
URL:		http://www.xfce.org/projects/xfce4-panel/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	exo-devel >= 0.3.100
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xfce4-icon-theme
Obsoletes:	xfce4-iconbox
Obsoletes:	xfce4-showdesktop-plugin
Obsoletes:	xfce4-systray
Obsoletes:	xfce4-taskbar-plugin
Obsoletes:	xfce4-themes
Obsoletes:	xfce4-windowlist-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the Xfce desktop environment.

%description -l pl.UTF-8
xfce4-panel to panel dla środowiska Xfce.

%package apidocs
Summary:	Xfce panel API documentation
Summary(pl.UTF-8):	Dokumentacja API panelu Xfce
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Xfce panel API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API panelu Xfce.

%package libs
Summary:	xfce4panel library
Summary(pl.UTF-8):	Biblioteka xfce4panel
Group:		X11/Development/Libraries

%description libs
This package contains xfce4panel library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę xfce4panel.

%package devel
Summary:	Header files for building Xfce panel plugins
Summary(pl.UTF-8):	Pliki nagłówkowe do budowania wtyczek panelu Xfce
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfce4util-devel >= %{version}
Requires:	libxfcegui4-devel >= %{version}

%description devel
Header files for building Xfce panel plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do budowania wtyczek panelu Xfce.

%prep
%setup -q

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

mv $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

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
%doc AUTHORS ChangeLog HACKING NEWS README
%attr(755,root,root) %{_bindir}/xfce4-panel
%attr(755,root,root) %{_bindir}/xfce4-popup-windowlist

%dir %{_sysconfdir}/xdg/xfce4/panel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/clock-14.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-7.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-8.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-9.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/launcher-10.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/panels.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/systray-4.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/xfce4-menu-5.rc
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/panel-plugins
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libactions.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libclock.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libiconbox.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/liblauncher.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libpager.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libseparator.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libshowdesktop.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libsystray.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libtasklist.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libwindowlist.so
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
%attr(755,root,root) %{_libdir}/libxfce4panel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4panel.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel.so
%{_libdir}/libxfce4panel.la
%{_includedir}/xfce4/libxfce4panel
%{_pkgconfigdir}/libxfce4panel-1.0.pc
