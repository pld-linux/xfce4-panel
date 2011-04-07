%define		xfce_version	4.8.0
Summary:	Next generation panel for Xfce
Summary(pl.UTF-8):	Panel nowej generacji dla Xfce
Name:		xfce4-panel
Version:	4.8.3
Release:	2
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce4-panel/4.8/%{name}-%{version}.tar.bz2
# Source0-md5:	31d7c15fb93f4a771fc26cf13d4dc010
URL:		http://www.xfce.org/projects/xfce4-panel
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	garcon-devel >= 0.1.5
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libwnck2-devel >= 2.22.0
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
# NOTE: xfce4-icon-theme doesn't match XDG specification.
#       Use Tango as a default icon theme.
Requires:	tango-icon-theme
Requires:	xfce4-dirs >= 4.6
Suggests:	xfce-preferred-applications
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
Requires:	glib2-devel >= 1:2.18.0
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libxfce4ui-devel >= %{xfce_version}
Requires:	libxfce4util-devel >= %{xfce_version}

%description devel
Header files for building Xfce panel plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do budowania wtyczek panelu Xfce.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/xfce4/panel-plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xfce4-panel
%attr(755,root,root) %{_bindir}/xfce4-popup-applicationsmenu
%attr(755,root,root) %{_bindir}/xfce4-popup-directorymenu
%attr(755,root,root) %{_bindir}/xfce4-popup-windowmenu

%dir %{_sysconfdir}/xdg/xfce4/panel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/default.xml
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/panel
%attr(755,root,root) %{_libdir}/xfce4/panel/migrate
%attr(755,root,root) %{_libdir}/xfce4/panel/wrapper
%dir %{_libdir}/xfce4/panel-plugins
%dir %{_libdir}/xfce4/panel/plugins
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libactions.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libapplicationsmenu.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libclock.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libdirectorymenu.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/liblauncher.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libpager.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libseparator.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libshowdesktop.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libsystray.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libtasklist.so
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwindowmenu.so
%{_datadir}/xfce4/panel
%dir %{_datadir}/xfce4/panel-plugins
%dir %{_datadir}/doc/xfce4-panel
%{_datadir}/doc/xfce4-panel/README.gtkrc-2.0
%dir %{_datadir}/doc/xfce4-panel/html
%{_datadir}/doc/xfce4-panel/html/*.css
%{_datadir}/doc/xfce4-panel/html/C
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxfce4panel-1.0

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4panel-1.0.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel-1.0.so
%{_includedir}/xfce4/libxfce4panel-1.0
%{_pkgconfigdir}/libxfce4panel-1.0.pc
