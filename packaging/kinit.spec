# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kinit

# >> macros
# << macros

Summary:    KDE Frameworks 5 tier 3 solution for process launching
Version:    5.3.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kinit.yaml
Source101:  kinit-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kservice-devel
BuildRequires:  kio-devel
BuildRequires:  ki18n-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kcrash-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kjs-devel
BuildRequires:  kbookmarks-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kauth-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  kglobalaccel-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  sonnet-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  solid-devel
BuildRequires:  kdoctools-devel
BuildRequires:  karchive-devel
BuildRequires:  libcap-devel

%description
KDE Frameworks 5 tier 3 solution for process launching


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kservice-devel
Requires:   kio-devel
Requires:   ki18n-devel
Requires:   kwindowsystem-devel
Requires:   kcrash-devel
Requires:   kconfig-devel
Requires:   kdoctools-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_bindir}/*
%{_kf5_libdir}/libkdeinit5_klauncher.so
%{_kf5_libexecdir}/*
%{_mandir}/man8/kdeinit5.8.gz
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_cmakedir}/KF5Init
%{_kf5_dbusinterfacesdir}/*.xml
# >> files devel
# << files devel
