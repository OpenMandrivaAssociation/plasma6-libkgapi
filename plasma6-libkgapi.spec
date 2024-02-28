#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Library to access various Google services via their public API
Name:		plasma6-libkgapi
Version:	24.02.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.dvratil.cz/category/akonadi-google/
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/libkgapi/-/archive/%{gitbranch}/libkgapi-%{gitbranchd}.tar.bz2#/libkgapi-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkgapi-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	qt6-qtwayland
BuildRequires:	doxygen
BuildRequires:	qt6-qttools-assistant
Obsoletes:	%{mklibname KPimGAPIBlogger} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPICalendar} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPIContacts} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPICore} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPIDrive} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPILatitude} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPIMaps} < %{EVRD}
Obsoletes:	%{mklibname KPimGAPITasks} < %{EVRD}

%description
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs
for various Google services.

Currently supported APIs:
  - Calendar API v3 (https://developers.google.com/google-apps/calendar)
  - Contacts API v3 (https://developers.google.com/google-apps/contacts/v3/)
  - Tasks API v1 (https://developers.google.com/google-apps/tasks)
  - Latitude API v1 (https://developers.google.com/latitude/v1/)
  - Static Google Maps API v2
    (https://developers.google.com/maps/documentation/staticmaps/)
  - Drive API v2 (https://developers.google.com/drive/v2/reference)

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/libkgapi.categories
%{_libdir}/sasl2/libkdexoauth2.so*

%dependinglibpackage KPim6GAPIBlogger 6

%dependinglibpackage KPim6GAPICalendar 6

%dependinglibpackage KPim6GAPICore 6

%dependinglibpackage KPim6GAPIDrive 6

%dependinglibpackage KPim6GAPILatitude 6

%dependinglibpackage KPim6GAPIMaps 6

%dependinglibpackage KPim6GAPIPeople 6

%dependinglibpackage KPim6GAPITasks 6

%define devname %mklibname KF6GAPI -d

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Provides:	%{name}-devel = %{EVRD}
Requires:	%{mklibname KPim6GAPIBlogger} = %{EVRD}
Requires:	%{mklibname KPim6GAPICalendar} = %{EVRD}
Requires:	%{mklibname KPim6GAPICore} = %{EVRD}
Requires:	%{mklibname KPim6GAPIDrive} = %{EVRD}
Requires:	%{mklibname KPim6GAPILatitude} = %{EVRD}
Requires:	%{mklibname KPim6GAPIMaps} = %{EVRD}
Requires:	%{mklibname KPim6GAPIPeople} = %{EVRD}
Requires:	%{mklibname KPim6GAPITasks} = %{EVRD}
Obsoletes:	%{mklibname kgapi -d} <= 6.3.1-2

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%dir %{_includedir}/KPim6/KGAPI
%{_includedir}/KPim6/KGAPI/KGAPI
%{_includedir}/KPim6/KGAPI/kgapi
%{_includedir}/KPim6/KGAPI/kgapi_version.h
%{_libdir}/libKPim6GAPIBlogger.so
%{_libdir}/libKPim6GAPICalendar.so
%{_libdir}/libKPim6GAPICore.so
%{_libdir}/libKPim6GAPIDrive.so
%{_libdir}/libKPim6GAPILatitude.so
%{_libdir}/libKPim6GAPIMaps.so
%{_libdir}/libKPim6GAPIPeople.so
%{_libdir}/libKPim6GAPITasks.so
%{_libdir}/cmake/KPim6GAPI

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkgapi-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-qt
