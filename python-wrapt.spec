%define module wrapt
%bcond tests 1

Name:		python-wrapt
Version:	2.0.1
Release:	1
Summary:	Python module for decorators, wrappers and monkey patching
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.python.org/pypi/wrapt
Source0:	https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Python module for decorators, wrappers and monkey patching.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%build
export CLFAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
# This file contains mypy typechecking tests ignore it.
ignore="${ignore-} --ignore=tests/conftest.py"

# run tests
%{__python} -m pytest ${ignore-} -v
# run tests with wrapt C extensions disabled
WRAPT_DISABLE_EXTENSIONS=true %{__python} -m pytest ${ignore-} -v
%endif

%files
%doc README.md
%license LICENSE
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
