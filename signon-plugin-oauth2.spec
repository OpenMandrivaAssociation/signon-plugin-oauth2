Name:		signon-plugin-oauth2
Version:	0.23
Release:	1
Summary:	OAuth2 plugin for the Accounts framework
License:	LGPLv2
URL:		https://gitlab.com/accounts-sso/signon-plugin-oauth2
Source0:	https://gitlab.com/accounts-sso/signon-plugin-oauth2/repository/%{name}-%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(signon-plugins)
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(libproxy-1.0)

%description
%{summary}.

%package devel
Summary:	Development files for %{name}
Requires:       %{name} = %{EVRD}

%description devel
%{summary}.

%prep
%setup -q

%build

export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 QMF_INSTALL_ROOT=%{_prefix} \
    QMAKE_CXXFLAGS_RELEASE="$QMAKE_CXXFLAGS -Wno-error -Wno-error=unused-variable" \
    CONFIG+=release \
    LIBDIR=%{?_libdir} \
    signon-oauth2.pro

%make


%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

# Delete tests
rm -fv %{buildroot}/%{_bindir}/signon-oauth2plugin-tests
rm -rfv %{buildroot}/%{_datadir}/signon-oauth2plugin-tests

# Delete examples
rm -fv %{buildroot}/%{_bindir}/oauthclient
rm -rvf %{buildroot}/%{_sysconfdir}

%files
%{_libdir}/signon/liboauth2plugin.so

%files devel
%{_includedir}/signon-plugins/*.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc
