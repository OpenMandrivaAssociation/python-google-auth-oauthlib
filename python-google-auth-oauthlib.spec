Name:		python-google-auth-oauthlib
Version:	1.5.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/google-auth-oauthlib/google_auth_oauthlib-%{version}.tar.gz
Summary:	Google Authentication Library
URL:		https://pypi.org/project/google-auth-oauthlib/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
Google Authentication Library

%files
%{_bindir}/google-oauthlib-tool
%{py_sitedir}/google_auth_oauthlib
%{py_sitedir}/google_auth_oauthlib-*.*-info
