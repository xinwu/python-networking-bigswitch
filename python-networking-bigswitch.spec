%global pypi_name bsnstacklib
%global rpm_prefix networking-bigswitch

Name:           python-%{rpm_prefix}
Version:        2015.1.33
Release:        1%{?dist}
Summary:        Big Switch Networks packages for OpenStack Networking
Group:          Applications/System
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        neutron-bsn-agent.service
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

Requires:       python-pbr
Requires:       openstack-neutron
Requires:       python-oslo-log
Requires:       python-oslo-config
Requires:       python-oslo-utils
Requires:       python-oslo-messaging
Requires:       python-oslo-serialization

%description
This package contails Big Switch Networks
neutron plugins and agent

%package -n python-%{rpm_prefix}-plugin
Summary:	Neutron Big Switch Networks plugin
Group:		Applications/System
%description -n python-%{rpm_prefix}-plugin
This library contains the ml2 plugin and l3 service plugin
required to integrate an OpenStack deployment with a
Big Switch Networks fabric.

%package -n python-%{rpm_prefix}-agent
Summary:        Neutron Big Switch Networks agent
Group:          Applications/System
%description -n python-%{rpm_prefix}-agent
This package contains the Big Switch Networks agent
to create neutron port on IVS.


%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/neutron-bsn-agent.service

%files
%license LICENSE

%files -n python-%{rpm_prefix}-plugin
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{rpm_prefix}-agent
/usr/bin/neutron-bsn-agent
%{_unitdir}/neutron-bsn-agent.service

%changelog
* Fri Aug 14 2015 Xin Wu <xin.wu@bigswitch.com> - 2015.1.33-1
- Initial package.


