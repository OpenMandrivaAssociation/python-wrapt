%define module wrapt
%define debug_package %{nil}
  
Summary:	Python module for decorators, wrappers and monkey patching
Name:		python-wrapt
Version:	1.17.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/wrapt
Source0:	https://files.pythonhosted.org/packages/source/w/wrapt/wrapt-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
# FIXME why isn't this autodetected???
Provides:	python3egg(wrapt) = %{version}
 
%description 
Python module for decorators, wrappers and monkey patching.

%prep
%autosetup -p1 -n %{module}-%{version}
  
%build
%py_build

%install 
%py_install

%files
%{py_platsitedir}/wrapt
%{py_platsitedir}/wrapt*.egg-info
