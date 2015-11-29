#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	django-voting
Summary:	Generic voting application for Django
Name:		python-%{module}
Version:	0.2
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/d/django-voting/django-voting-%{version}.tar.gz
# Source0-md5:	d4dbc8c0530f127027f6af6e76f91ead
URL:		https://pypi.python.org/pypi/django-voting
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic voting application for Django projects.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/voting/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt INSTALL.txt LICENSE.txt README.txt docs/overview.txt
%dir %{py_sitescriptdir}/voting
%{py_sitescriptdir}/voting/*.py[co]
%{py_sitescriptdir}/voting/migrations
%{py_sitescriptdir}/voting/templatetags
%{py_sitescriptdir}/django_voting-%{version}-py*.egg-info
