Summary:	Modular patch bay for audio and MIDI systems based on JACK and ALSA
Summary(pl.UTF-8):	Modularny panel połączeniowy dla systemów dźwiękowych i MIDI opartych na JACK-u i ALSA-ie
Name:		patchage
Version:	1.0.10
Release:	1
License:	GPL v3+
Group:		X11/Applications/Sound
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	cd686e3a4a01fce08f27096e080c720b
URL:		http://drobilla.net/software/patchage/
BuildRequires:	alsa-lib-devel >= 1.0
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	ganv-devel >= 1.5.2
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	glibmm-devel >= 2.14.0
BuildRequires:	gtkmm-devel >= 2.12.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.120.0
BuildRequires:	libfmt-devel >= 9
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	ganv >= 1.5.2
Requires:	glib2 >= 1:2.14.0
Requires:	glibmm >= 2.14.0
Requires:	gtkmm >= 2.12.0
Requires:	jack-audio-connection-kit-libs >= 0.120.0
Requires:	libfmt >= 9
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/patchage
%{_datadir}/patchage
%{_desktopdir}/patchage.desktop
%{_iconsdir}/hicolor/*x*/apps/patchage.png
%{_iconsdir}/hicolor/*x*/apps/patchage.svg
%{_iconsdir}/hicolor/scalable/apps/patchage.svg
%{_mandir}/man1/patchage.1*
