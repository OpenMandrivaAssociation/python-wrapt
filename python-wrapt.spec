%define module wrapt
  
Summary:	Python module for decorators, wrappers and monkey patching
Name:		python-wrapt
Version:	1.10.11
Release:	1
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/wrapt
Source0:	https://pypi.python.org/packages/a0/47/66897906448185fcb77fc3c2b1bc20ed0ecca81a0f2f88eda3fc5a34fc3d/wrapt-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
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
