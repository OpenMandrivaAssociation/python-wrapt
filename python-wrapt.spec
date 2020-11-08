%define module wrapt
%define debug_package %{nil}
  
Summary:	Python module for decorators, wrappers and monkey patching
Name:		python-wrapt
Version:	1.12.1
Release:	2
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/wrapt
Source0:	https://files.pythonhosted.org/packages/source/w/wrapt/wrapt-1.12.1.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
# FIXME why isn't this autodetected???
Provides:	python3egg(wrapt) = %{version}
 
%description 
Python module for decorators, wrappers and monkey patching.

%prep
%setup -qn %{module}-%{version}
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%{py_platsitedir}/wrapt
%{py_platsitedir}/wrapt*.egg-info
