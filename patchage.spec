Summary:	Modular patch bay for audio and MIDI systems based on JACK and ALSA
Summary(pl.UTF-8):	Modularny panel połączeniowy dla systemów dźwiękowych i MIDI opartych na JACK-u i ALSA-ie
Name:		patchage
Version:	0.5.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	3f1c297c8c6b998563d1a2fbc215cf85
URL:		http://drobilla.net/software/patchage/
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	boost-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	flowcanvas-devel >= 0.7.1
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtkmm-devel >= 2.11.12
BuildRequires:	jack-audio-connection-kit-devel >= 0.107.0
BuildRequires:	libglademm-devel >= 2.6.0
BuildRequires:	libgnomecanvasmm-devel >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	raul-devel >= 0.5.1
Requires:	flowcanvas >= 0.7.1
Requires:	glib2 >= 1:2.14.0
Requires:	gtkmm >= 2.11.12
Requires:	jack-audio-connection-kit-libs >= 0.107.0
Requires:	libglademm >= 2.6.0
Requires:	libgnomecanvasmm >= 2.6.0
Requires:	raul >= 0.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Patchage is a modular patch bay for audio and MIDI systems based on
JACK and ALSA.

%description -l pl.UTF-8
Patchage to modularny panel połączeniowy dla systemów dźwiękowych i
MIDI opartych na JACK-u i ALSA-ie.

%prep
%setup -q

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/patchage
%{_datadir}/patchage
%{_desktopdir}/patchage.desktop
%{_iconsdir}/hicolor/*x*/apps/patchage.png
%{_iconsdir}/hicolor/scalable/apps/patchage.svg
%{_mandir}/man1/patchage.1*
