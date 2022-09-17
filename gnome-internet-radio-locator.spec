Summary:	GNOME Internet Radio Locator
Summary(pl.UTF-8):	GNOME Internet Radio Locator - program do wyszukiwania rozgłośni internetowych
Name:		gnome-internet-radio-locator
Version:	12.7.0
Release:	1
License:	GPL v3+ (parts LGPL v2.1+ or GPL v2+)
Group:		X11/Applications/Sound
Source0:	https://download.gnome.org/sources/gnome-internet-radio-locator/12.7/%{name}-%{version}.tar.xz
# Source0-md5:	c7993a732959447e6cfcaa79068ce28a
URL:		https://wiki.gnome.org/Apps/Girl
BuildRequires:	geoclue2-devel >= 2.5.7
BuildRequires:	geocode-glib-devel >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gstreamer-devel >= 1.0
# pkgconfig(gstreamer-player-1.0)
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk-doc >= 1.16
BuildRequires:	gtk+3-devel >= 3.24.28
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libchamplain-devel >= 0.12.10
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:0.28
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	geoclue2 >= 2.5.7
Requires:	geocode-glib >= 3.20
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.24.28
Requires:	libchamplain >= 0.12.10
# only functionally (both packages can be installed simultaneously), but girl is unmaintained since 2017
Obsoletes:	girl < 10.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Internet Radio Locator program, allows users to easily find live
radio programs on radio broadcasters on the Internet.

%description -l pl.UTF-8
GNOME Internet Radio Locator to program pozwalający użytkownikom łatwo
wyszukać programy internetowych rozgłości radiowych nadających na
żywo.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-recording
# --with-help is broken

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AMFM AUTHORS BROADCAST ChangeLog EFF GNU NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gnome-internet-radio-locator
%attr(755,root,root) %{_bindir}/org.gnome.Radio
%{_datadir}/gnome-internet-radio-locator
%{_datadir}/metainfo/gnome-internet-radio-locator.appdata.xml
%{_desktopdir}/gnome-internet-radio-locator.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-internet-radio-locator.png
%{_mandir}/man1/gnome-internet-radio-locator.1*
