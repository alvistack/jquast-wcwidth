# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-wcwidth
Epoch: 100
Version: 0.2.7
Release: 1%{?dist}
BuildArch: noarch
Summary: Measures the displayed width of unicode strings in a terminal
License: MIT
URL: https://github.com/jquast/wcwidth/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This library is mainly for CLI programs that carefully produce output
for Terminals, or make pretend to be an emulator.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-wcwidth
Summary: Measures the displayed width of unicode strings in a terminal
Requires: python3
Provides: python3-wcwidth = %{epoch}:%{version}-%{release}
Provides: python3dist(wcwidth) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wcwidth = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wcwidth) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wcwidth = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wcwidth) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-wcwidth
This library is mainly for CLI programs that carefully produce output
for Terminals, or make pretend to be an emulator.

%files -n python%{python3_version_nodots}-wcwidth
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-wcwidth
Summary: Measures the displayed width of unicode strings in a terminal
Requires: python3
Provides: python3-wcwidth = %{epoch}:%{version}-%{release}
Provides: python3dist(wcwidth) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-wcwidth = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(wcwidth) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-wcwidth = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(wcwidth) = %{epoch}:%{version}-%{release}

%description -n python3-wcwidth
This library is mainly for CLI programs that carefully produce output
for Terminals, or make pretend to be an emulator.

%files -n python3-wcwidth
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
