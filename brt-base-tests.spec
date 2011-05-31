# This is a spec file for brt-base-tests

%define name		brt-base-tests
%define release	        1 	
%define version 	0.9

Summary: 		brt-base-tests
License: 		BSD
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source0: 		%{name}-%{version}.tar.gz
Prefix: 		/usr/local
Group: 			Development/Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description
brt-base-tests package for MeeGo

%prep
%setup -q -n %{name}_%{version}

echo %{_sbindir}

%install
install -v -D tests.xml %{buildroot}/usr/share/%{name}/tests.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
/usr/share/brt-base-tests



