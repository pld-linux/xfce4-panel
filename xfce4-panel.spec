Summary:	Next generation panel for XFce
Summary(pl):	Panel nowej generacji dla XFce
Name:		xfce4-panel
Version:	4.0.5
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	e45c70fd08edf3fadd23571f3151ac5e
URL:		http://www.xfce.org/
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	libxml2 >= 2.4.0
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the XFce desktop environment.

%description -l pl
xfce4-panel to panel dla ¶rodowiska XFce.

%package devel
Summary:	Header files for building XFce panel plugins
Summary(pl):	Pliki nag³ówkowe do budowania wtyczek panelu XFce
Group:		Development/Libraries
Requires:	libxfcegui4-devel >= 4.0.0
Requires:	libxml2-devel >= 2.4.0
# doesn't require base

%description devel
Header files for building XFce panel plugins.

%description devel -l pl
Pliki nag³ówkowe do budowania wtyczek panelu XFce.

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

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
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.ca
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.hu
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.nl
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.vi
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%dir %{_libdir}/xfce4/panel-plugins
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/themes
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/panel
%{_pkgconfigdir}/*.pc
