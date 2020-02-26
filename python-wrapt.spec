%define module wrapt
  
Summary:	Python module for decorators, wrappers and monkey patching
Name:		python-wrapt
Version:	1.12.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/wrapt
Source0:	https://files.pythonhosted.org/packages/ee/bc/7993faa8084b5a5dbabb07a197ae1b7590da4752dc80455d878573553e2f/wrapt-1.12.0.tar.gz
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
