#
# TODO:
# - check the icon & the desktop file
Summary:	Next generation panel for XFce
Summary(pl):	Panel nowej generacji dla XFce
Name:		xfce4-panel
Version:	4.1.90
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2a99d50d37a04f1d67c89886c7a509d5
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
%setup -q

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

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml
%lang(ar) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ar
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ca
%lang(eu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.eu
%lang(he) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.he
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.hu
%lang(it) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.it
%lang(ms) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ms
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.nl
%lang(ro) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ro
%lang(ru) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ru
%lang(sk) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.sk
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.vi
%lang(zh_TW) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.zh_TW

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
