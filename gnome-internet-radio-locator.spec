Summary:	GNOME Internet Radio Locator
Summary(pl.UTF-8):	GNOME Internet Radio Locator - program do wyszukiwania rozgłośni internetowych
Name:		gnome-internet-radio-locator
Version:	0.6.0
Release:	1
License:	GPL v3+ (parts LGPL v2.1+ or GPL v2+)
Group:		X11/Applications/Sound
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-internet-radio-locator/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	6cd0e2e665e34396d8979ce9e2b9cd04
URL:		https://wiki.gnome.org/Apps/Girl
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gstreamer-devel >= 1.0
# pkgconfig(gstreamer-player-1.0)
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.16
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libchamplain-devel >= 0.12.10
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:0.28
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.38.0
Requires:	libchamplain >= 0.12.10
# only functionally, both packages can be installed simultaneously
#Obsoletes:	girl
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
%doc AUTHORS BROADCAST ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gnome-internet-radio-locator
%{_datadir}/appdata/gnome-internet-radio-locator.appdata.xml
%{_datadir}/gnome-internet-radio-locator
%{_desktopdir}/gnome-internet-radio-locator.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-internet-radio-locator.png
%{_mandir}/man1/gnome-internet-radio-locator.1*
