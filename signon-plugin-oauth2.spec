%undefine _debugsource_packages

Name:		signon-plugin-oauth2
Version:	0.25
Release:	1
Summary:	OAuth2 plugin for the Accounts framework
License:	LGPLv2
Group:		System/Libraries
URL:		https://gitlab.com/accounts-sso/signon-plugin-oauth2
Source0:	https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/archive/VERSION_%{version}/signon-plugin-oauth2-VERSION_%{version}.tar.bz2
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(signon-plugins)
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(libproxy-1.0)
Requires:	signond

%patchlist
# From upstream git
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/d38cd1e356506f6ded2211eba8f1127e846fdf2d.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/a7db188b4e8d813b32997a26907d82432b4a5c1c.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/ee8cc854d941d6ad91db66958d58c64fb6fa1589.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/d1626628a65d47a8c764c6f1049781eb385d0cb8.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/5245185626009b939713f075462f0e04b220fe94.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/7b5fcc221bc22ca8ce45a05a61d3227262a5d42d.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/2bf858a8c92aadaf75ce8213ea037fe7db544ae8.patch
https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/commit/d759439066f0a34e5ad352ebab0b3bb2790d429e.patch
# Qt 6.x port
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/d3ba6d4c19ca0b1081fbafc757d3c496cc21ada2.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/a0b372dfb6d37d0a81a545239128fec5ee94283c.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/8211fd4a3ca31370069c6953db1589c1110dca90.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/039dab8db2e16d02872c6e12c698157e05dc43e2.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/47ff5a950e54ae2a570183be21312bcaa5271396.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/bef68f45e80c13501f836ec9d14aa3df682748e8.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/e9d3bdbd4eb8331a03b0c49d6b3a6c020db11c7f.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/a275d6eacc71a1c0ac6a95e2c77a29b13e6c189e.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/3ead61662e9b931ff2487869904c9be33cf97a85.patch
https://gitlab.com/nicolasfella/signon-plugin-oauth2/-/commit/fab698862466994a8fdc9aa335c87b4f05430ce6.patch

%description
%{summary}.

%package devel
Summary:	Development files for %{name}
Requires:       %{name} = %{EVRD}
Group:		Development/C++

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-VERSION_%{version}

%build

export PATH=%{_qtdir}/bin:$PATH
%{_qtdir}/bin/qmake QMF_INSTALL_ROOT=%{_prefix} \
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
