Summary:	Next generation panel for xfce
Summary(pl):	Panel nowej generacji dla xfce
Name:		xfce4-panel
Version:	3.99.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce4-rc4/src/%{name}-%{version}.tar.gz
# Source0-md5:	8a26007aa716fe8b1facde6d0cd23e63
URL:		http://www.xfce.org/
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 3.99.4
BuildRequires:	libxfcegui4-devel >= 3.99.4
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 3.99.4
Requires:	libxfce4mcs >= 3.99.4
Requires:	libxfcegui4 >= 3.99.4
Requires:	libxml2 >= 2.4.0
Requires:	xfce-mcs-manager >= 3.99.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the xfce desktop environment.

%description -l pl
xfce4-panel to panel dla ¶rodowiska xfce.

%package devel
Summary:	Header files for building xfce panel plugins
Summary(pl):	Pliki nag³ówkowe do budowania wtyczek panelu xfce
Group:		Development/Libraries
Requires:	libxfcegui4-devel >= 0.0.17
Requires:	libxml2-devel >= 2.4.0
# doesn't require base

%description devel
Header files for building xfce panel plugins.

%description devel -l pl
Pliki nag³ówkowe do budowania wtyczek panelu xfce.

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc.*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xfce4rc
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
