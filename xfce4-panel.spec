Summary: 	Next generation panel for xfce
Name: 		xfce4-panel
Version: 	3.90.0
Release: 	0.1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	8e7531c9924d318f3aa0320223328949
Group: 		X11/Applications
Requires:	libxfcegui4
Requires:	libxfce4mcs
Requires:	xfce-mcs-manager
Requires:	libxml2 >= 2.4.0
BuildRequires: 	libxfcegui4-devel
BuildRequires:	libxfce4mcs-devel
BuildRequires:	xfce-mcs-manager-devel
BuildRequires: 	libxml2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the XFce desktop environment

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
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog NEWS NOTES INSTALL COPYING AUTHORS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_libdir}/xfce4/panel-plugins/*.la
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_libdir}/xfce4/mcs-plugins/*.la
%{_libdir}/pkgconfig/
%{_sysconfdir}/xfce4/
%{_datadir}/xfce4/doc/
%{_datadir}/locale/
%{_includedir}/xfce4/
%{_datadir}/xfce4/themes/
