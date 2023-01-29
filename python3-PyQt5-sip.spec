%define		module	PyQt5-sip
Summary:	The sip module support for PyQt5
Name:		python3-%{module}
Version:	12.11.1
Release:	1
Epoch:		2
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/MODULE/
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt5_sip/PyQt5_sip-%{version}.tar.gz
# Source0-md5:	1036bf431e155f198309ea8c7a5082cf
URL:		https://www.riverbankcomputing.com/software/sip/
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sip extension module provides support for the PyQt5 package.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n PyQt5_sip-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py3_sitedir}/PyQt5/*.so
%{py3_sitedir}/PyQt5_sip-%{version}-py*.egg-info
