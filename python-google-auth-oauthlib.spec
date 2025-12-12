Name:		python-google-auth-oauthlib
Version:	1.2.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/g/google-auth-oauthlib/google_auth_oauthlib-%{version}.tar.gz
Summary:	Google Authentication Library
URL:		https://pypi.org/project/google-auth-oauthlib/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Google Authentication Library

%files
%{_bindir}/google-oauthlib-tool
%{py_sitedir}/google_auth_oauthlib
%{py_sitedir}/google_auth_oauthlib-*.*-info
%{py_sitedir}/docs/conf.py
