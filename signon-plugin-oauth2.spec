Name:		signon-plugin-oauth2
Version:	0.22
Release:	1
Summary:	OAuth2 plugin for the Accounts framework
License:	LGPLv2
URL:		https://gitlab.com/accounts-sso/signon-plugin-oauth2
Source0:	https://gitlab.com/accounts-sso/signon-plugin-oauth2/repository/%{name}-%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	cmake(Qt5XmlPatterns)
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
%setup -q -n %{name}.git

%build
# (tpg) fix clang issue
export QMAKE_CFLAGS="$QMAKE_CFLAGS -Wno-unused-variable"
export QMAKE_CXXFLAGS="$QMAKE_CXXFLAGS -Wno-unused-variable"

export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{?_libdir} \
    QMAKE_CXXFLAGS="$QMAKE_CXXFLAGS -Wno-unused-variable" \
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
