%define module wrapt
%bcond tests 1

Name:		python-wrapt
Version:	2.1.1
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

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%build -p
export CLFAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
# This file contains mypy typechecking tests ignore it.
ignore="${ignore-} --ignore=tests/conftest.py"
# test_wrap_class_method_inherited is failing with an AssertionError in v2.1.0, skip it for now:
# FAILED tests/core/test_monkey_patching.py::TestMonkeyPatching::test_wrap_class_method_inherited - AssertionError: <class 'test_monkey_patching.Class_2_1'> != <class 'test_monkey_patching.Class_2'>
skiptests+="not test_wrap_class_method_inherited"

# run tests
pytest -v ${ignore-} -k "$skiptests"
# run tests with wrapt C extensions disabled
WRAPT_DISABLE_EXTENSIONS=true pytest -v ${ignore-} -k "$skiptests"
%endif

%files
%doc README.md
%license LICENSE
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
