%define		xfce_version	4.20.0
Summary:	Next generation panel for Xfce
Summary(pl.UTF-8):	Panel nowej generacji dla Xfce
Name:		xfce4-panel
Version:	4.20.2
Release:	2
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/xfce/xfce4-panel/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	99f9137cef2168eef6a4d96b58cfeec2
URL:		https://docs.xfce.org/xfce/xfce4-panel/start
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	exo-devel >= 0.12.0
BuildRequires:	garcon-devel >= 4.20.0
BuildRequires:	garcon-gtk3-devel >= 4.20.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gobject-introspection-devel >= 1.72.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gtk-doc-automake >= 1.9
BuildRequires:	gtk-layer-shell-devel >= 0.7.0
BuildRequires:	libdbusmenu-gtk3-devel >= 16.04.0
BuildRequires:	libwnck-devel >= 3.0
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxfce4windowing-devel >= 4.20.1
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	vala
BuildRequires:	vala-libxfce4util >= %{xfce_version}
BuildRequires:	wayland-devel >= 1.20
BuildRequires:	xfce4-dev-tools >= 4.20.0
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRequires:	xorg-lib-libX11-devel >= 1.6.7
BuildRequires:	xorg-lib-libXext-devel >= 1.0.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	adwaita-icon-theme
Requires:	exo >= 0.12.0
Requires:	garcon >= 4.20.0
Requires:	garcon-gtk3 >= 4.20.0
Requires:	gtk-layer-shell >= 0.7.0
Requires:	hicolor-icon-theme
Requires:	libdbusmenu-gtk3 >= 16.04.0
Requires:	libwnck >= 3.0
Requires:	libxfce4windowing >= 4.20.1
Requires:	wayland >= 1.20
Requires:	xfce4-dirs >= 4.6
Requires:	xfconf >= %{xfce_version}
Requires:	xorg-lib-libX11 >= 1.6.7
Requires:	xorg-lib-libXext >= 1.0.0
Suggests:	adwaita-icon-theme-legacy
Suggests:	xfce-preferred-applications
Obsoletes:	xfce4-iconbox < 4.3
Obsoletes:	xfce4-showdesktop-plugin < 0.5
Obsoletes:	xfce4-systray < 4.3
Obsoletes:	xfce4-themes < 4.1
Obsoletes:	xfce4-windowlist-plugin < 0.2
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
BuildArch:	noarch

%description apidocs
Xfce panel API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API panelu Xfce.

%package libs
Summary:	xfce4panel library
Summary(pl.UTF-8):	Biblioteka xfce4panel
Group:		X11/Development/Libraries
Requires:	cairo >= 1.16.0
Requires:	glib2 >= 1:2.72.0
Requires:	gtk+3 >= 3.24.0
Requires:	libxfce4util >= %{xfce_version}

%description libs
This package contains xfce4panel library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę xfce4panel.

%package devel
Summary:	Header files for building Xfce panel plugins
Summary(pl.UTF-8):	Pliki nagłówkowe do budowania wtyczek panelu Xfce
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.72.0
Requires:	gtk+3-devel >= 3.24.0
Requires:	libxfce4ui-devel >= %{xfce_version}
Requires:	libxfce4util-devel >= %{xfce_version}

%description devel
Header files for building Xfce panel plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do budowania wtyczek panelu Xfce.

%package -n vala-xfce4-panel
Summary:	Vala API for Xfce panel
Summary(pl.UTF-8):	API języka Vala do panelu Xfce
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
Requires:	vala-libxfce4util >= %{xfce_version}

%description -n vala-xfce4-panel
Vala API for Xfce panel.

%description -n vala-xfce4-panel -l pl.UTF-8
API języka Vala ls panelu Xfce.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/xfce4/panel-plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}

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
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/xfce4-panel
%attr(755,root,root) %{_bindir}/xfce4-popup-applicationsmenu
%attr(755,root,root) %{_bindir}/xfce4-popup-directorymenu
%attr(755,root,root) %{_bindir}/xfce4-popup-windowmenu
%dir %{_sysconfdir}/xdg/xfce4/panel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/default.xml
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/panel
%attr(755,root,root) %{_libdir}/xfce4/panel/migrate
%attr(755,root,root) %{_libdir}/xfce4/panel/wrapper-2.0
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
%{_iconsdir}/hicolor/*x*/apps/org.xfce.panel*.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.panel*.svg
%{_desktopdir}/panel-desktop-handler.desktop
%{_desktopdir}/panel-preferences.desktop

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxfce4panel-2.0

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel-2.0.so.*.*.*
%ghost %{_libdir}/libxfce4panel-2.0.so.4
%{_libdir}/girepository-1.0/Libxfce4panel-2.0.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libxfce4panel-2.0.so
%{_includedir}/xfce4/libxfce4panel-2.0
%{_pkgconfigdir}/libxfce4panel-2.0.pc
%{_datadir}/gir-1.0/Libxfce4panel-2.0.gir

%files -n vala-xfce4-panel
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libxfce4panel-2.0.deps
%{_datadir}/vala/vapi/libxfce4panel-2.0.vapi
