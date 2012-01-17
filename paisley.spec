%global __python python2.6
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define version 0.3.1
%define unmangled_version 0.3.1-feat.1
%define build_rev feat.1

Name:           python-paisley
Summary:        CouchDB client for Python's twisted framework
Version:        %{version}
Release:        %{?build_rev}%{?dist}
Source0:        paisley-%{unmangled_version}.tar.gz

Group:          Development/Languages
License:        MIT
URL:            http://github.com/f3at/paisley

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-setuptools >= 0.6c9

Provides:       %{name}

%description
Paisley is a CouchDB client written in Python to be used within a Twisted application.

%prep
%setup -q -n paisley-%{unmangled_version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT \
     --record=INSTALLED_FILES

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jan 17 2012 Sebastien Merle <s.merle@gmail.com>
- First spec file.
