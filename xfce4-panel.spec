#
# TODO:
# - check the icon & the desktop file
Summary:	Next generation panel for Xfce
Summary(pl):	Panel nowej generacji dla Xfce
Name:		xfce4-panel
Version:	4.2.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.us.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	3027c4601f208d290a988befed66a49f
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-handle-option.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= 4.2.1
BuildRequires:	libxfcegui4-devel >= 4.2.1
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.2.1
BuildRequires:	xfce4-dev-tools
Requires:	hicolor-icon-theme
Requires:	libxfce4mcs >= 4.2.1
Requires:	libxfcegui4 >= 4.2.1
Requires:	xfce-mcs-manager >= 4.2.1
Requires:	xfce4-icon-theme
Obsoletes:	xfce4-themes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panel is the panel for the Xfce desktop environment.

%description -l pl
xfce4-panel to panel dla ¶rodowiska Xfce.

%package devel
Summary:	Header files for building Xfce panel plugins
Summary(pl):	Pliki nag³ówkowe do budowania wtyczek panelu Xfce
Group:		Development/Libraries
Requires:	libxfcegui4-devel >= 4.2.1
Requires:	libxml2-devel >= 2.4.0
# doesn't require base

%description devel
Header files for building Xfce panel plugins.

%description devel -l pl
Pliki nag³ówkowe do budowania wtyczek panelu Xfce.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}
%{__make} html

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

%dir %{_sysconfdir}/xdg/xfce4/panel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml
%lang(ar) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ar
%lang(az) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.az
%lang(ca) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ca
%lang(da) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.da
%lang(el) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.el
%lang(eu) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.eu
%lang(fi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.fi
%lang(fr) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.fr
%lang(he) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.he
%lang(hu) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.hu
%lang(it) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.it
%lang(ja) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ja
%lang(ko) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ko
%lang(lt) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.lt
%lang(ms) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ms
%lang(nl) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.nl
%lang(pl) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.pl
%lang(ro) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ro
%lang(ru) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.ru
%lang(sk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.sk
%lang(sv) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.sv
%lang(tr) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.tr
%lang(vi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.vi
%lang(zh_CN) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.zh_CN
%lang(zh_TW) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/panel/contents.xml.zh_TW

%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%dir %{_libdir}/xfce4/panel-plugins
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so

%{_iconsdir}/hicolor/48x48/apps/xfce-mail.png
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(he) %{_datadir}/xfce4/doc/he/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xfce4/panel
%{_pkgconfigdir}/*.pc
