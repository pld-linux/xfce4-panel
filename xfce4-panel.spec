#
# TODO:
# - check the icon & the desktop file
#
%define		_snap 20040813
#
Summary:	Next generation panel for XFce
Summary(pl):	Panel nowej generacji dla XFce
Name:		xfce4-panel
Version:	4.1.7
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	e302b054bd2b13cb6a02ffaed5759640
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= 4.1.0
BuildRequires:	libxfcegui4-devel >= 4.1.19
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.1.0
Requires:	libxfce4mcs >= 4.1.0
Requires:	libxfcegui4 >= 4.1.19
Requires:	libxml2 >= 2.4.0
Requires:	xfce-mcs-manager >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the XFce desktop environment.

%description -l pl
xfce4-panel to panel dla ¶rodowiska XFce.

%package devel
Summary:	Header files for building XFce panel plugins
Summary(pl):	Pliki nag³ówkowe do budowania wtyczek panelu XFce
Group:		Development/Libraries
Requires:	libxfcegui4-devel >= 4.1.19
Requires:	libxml2-devel >= 2.4.0
# doesn't require base

%description devel
Header files for building XFce panel plugins.

%description devel -l pl
Pliki nag³ówkowe do budowania wtyczek panelu XFce.

%prep
%setup -q -n %{name}

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}
%{__make} html

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xfce4/themes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/{mcs-plugins,panel-plugins}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc
%lang(ar) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.ar
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.ca
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.hu
%lang(it) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.it
%lang(ms) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.ms
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.nl
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.vi

%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%dir %{_libdir}/xfce4/panel-plugins
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so

%{_iconsdir}/hicolor/48x48/apps/xfce-mail.png
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/themes
%{_iconsdir}/hicolor/*/*/*

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(it) %{_datadir}/xfce4/doc/it/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/panel
%{_pkgconfigdir}/*.pc
