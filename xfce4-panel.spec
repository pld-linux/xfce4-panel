Summary: 	Next generation panel for xfce
Summary(pl):	Panel nowej generacji dla xfce
Name: 		xfce4-panel
Version: 	3.91.0
Release: 	0.1
License:	GPL
Group: 		X11/Applications
Source0: 	http://dl.sourceforge.net/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	04b4212b5aa4374f4846a918ce67fef1
URL: 		http://www.xfce.org/
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 0.0.3
BuildRequires: 	libxfcegui4-devel >= 0.0.17
BuildRequires: 	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 0.2.0
Requires:	libxfce4mcs >= 0.0.3
Requires:	libxfcegui4 >= 0.0.17
Requires:	libxml2 >= 2.4.0
Requires:	xfce-mcs-manager >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the XFce desktop environment.

%description -l pl
xfce4-panel to panel dla ¶rodowiska XFce.

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
# /etc/xfce4 belongs to xfce-utils at the moment
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
