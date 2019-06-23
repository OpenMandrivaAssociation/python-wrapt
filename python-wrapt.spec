%define module wrapt
  
Summary:	Python module for decorators, wrappers and monkey patching
Name:		python-wrapt
Version:	1.11.2
Release:	4
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/wrapt
Source0:	https://files.pythonhosted.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz
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
