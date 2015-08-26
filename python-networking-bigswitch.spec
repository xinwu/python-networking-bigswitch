%global pypi_name bsnstacklib
%global rpm_prefix networking-bigswitch
%global docpath doc/build/html

Name:           python-%{rpm_prefix}
Version:        2015.1.36
Release:        1%{?dist}
Summary:        Big Switch Networks packages for OpenStack Networking
Group:          Applications/System
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        neutron-bsn-agent.service
Source2:        neutron-bsn-lldp.service
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:	systemd-units

Requires:       openstack-neutron
Requires:       python-pbr
Requires:       python-oslo-log
Requires:       python-oslo-config
Requires:       python-oslo-utils
Requires:       python-oslo-messaging
Requires:       python-oslo-serialization
Requires:       systemd

%description
This package contains Big Switch Networks
neutron plugins and agents

%package -n python-%{rpm_prefix}-agent
Summary:        Neutron Big Switch Networks agent
Group:          Applications/System
Requires:       python-%{rpm_prefix} = %{version}-%{release}
%description -n python-%{rpm_prefix}-agent
This package contains the Big Switch Networks agent
for security groups

%package -n python-%{rpm_prefix}-lldp
Summary:        Neutron Big Switch Networks LLDP package
Group:          Applications/System
Requires:       python-%{rpm_prefix} = %{version}-%{release}
%description -n python-%{rpm_prefix}-lldp
This package contains the Big Switch Networks LLDP agent.

%package -n python-%{rpm_prefix}-doc
Summary:        Neutron Big Switch Networks agent
Group:          Applications/System
%description -n python-%{rpm_prefix}-doc
This package contains the documentations for
Big Switch Networks neutron packages.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
%{__python2} setup.py build_sphinx
rm %{docpath}/.buildinfo

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/neutron-bsn-agent.service
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/neutron-bsn-lldp.service
mkdir -p %{buildroot}/%{_sysconfdir}/neutron/conf.d/neutron-bsn-agent

%files
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{rpm_prefix}-agent
%{_unitdir}/neutron-bsn-agent.service
%{_bindir}/neutron-bsn-agent
%dir /etc/neutron/conf.d/neutron-bsn-agent

%files -n python-%{rpm_prefix}-lldp
%{_unitdir}/neutron-bsn-lldp.service
%{_bindir}/bsnlldp

%files -n python-%{rpm_prefix}-doc
%doc README.rst
%doc %{docpath}

%changelog
* Fri Aug 14 2015 Xin Wu <xin.wu@bigswitch.com> - 2015.1.36-1
- Initial package.

