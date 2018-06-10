%define		xfce_version	4.13.0
Summary:	Next generation panel for Xfce
Summary(pl.UTF-8):	Panel nowej generacji dla Xfce
Name:		xfce4-panel
Version:	4.13.3
Release:	0.1
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce4-panel/4.13/%{name}-%{version}.tar.bz2
# Source0-md5:	0ccb448e3792949eb0ae9db8dc22789b
Patch0:		%{name}-no-empty-panel.patch
URL:		http://www.xfce.org/projects/xfce4-panel
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	garcon-devel >= 0.4.0
BuildRequires:	garcon-gtk2-devel >= 0.6.1
BuildRequires:	garcon-gtk3-devel >= 0.6.1
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel >= 2:2.24.0
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libwnck2-devel >= 2.22.0
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
Requires:	glib2-devel >= 1:2.30.0
Requires:	gtk+2-devel >= 2:2.24.0
Requires:	libxfce4ui-devel >= %{xfce_version}
Requires:	libxfce4util-devel >= %{xfce_version}

%description devel
Header files for building Xfce panel plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do budowania wtyczek panelu Xfce.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules \
	--enable-gtk3

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir}}/xfce4/panel-plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

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
%attr(755,root,root) %{_libdir}/xfce4/panel/wrapper-1.0
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
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxfce4panel-1.0

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4panel-1.0.so.4
%attr(755,root,root) %{_libdir}/libxfce4panel-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4panel-2.0.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4panel-1.0.so
%attr(755,root,root) %{_libdir}/libxfce4panel-2.0.so
%{_includedir}/xfce4/libxfce4panel-1.0
%{_includedir}/xfce4/libxfce4panel-2.0
%{_pkgconfigdir}/libxfce4panel-1.0.pc
%{_pkgconfigdir}/libxfce4panel-2.0.pc
