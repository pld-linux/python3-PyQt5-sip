#
# Conditional build:
%bcond_without	obsolete_py2	# obsolete python 2.x package

%define		module	PyQt5-sip
Summary:	The sip module support for PyQt5
Summary(pl.UTF-8):	Obsługa PyQt5 dla modułu sip
Name:		python3-%{module}
Version:	12.17.2
Release:	1
Epoch:		2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyqt5-sip/
Source0:	https://files.pythonhosted.org/packages/source/p/pyqt5_sip/pyqt5_sip-%{version}.tar.gz
# Source0-md5:	24cabc5bc969c18111d5187d8ea6e8d9
URL:		https://www.riverbankcomputing.com/software/sip/
BuildRequires:	python3-devel >= 1:3.10
BuildRequires:	python3-setuptools >= 1:30.3
BuildRequires:	python3-wheel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.10
%if %{with obsolete_py2}
Obsoletes:	python-PyQt5-sip < 2:5
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sip extension module provides support for the PyQt5 package.

%description -l pl.UTF-8
Rozszerzenie modułu sip, zapewniające obsługę pakietu PyQt5.

%prep
%setup -q -n pyqt5_sip-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{py3_sitedir}/PyQt5/sip.cpython-*.so
%{py3_sitedir}/PyQt5_sip-%{version}-py*.egg-info
