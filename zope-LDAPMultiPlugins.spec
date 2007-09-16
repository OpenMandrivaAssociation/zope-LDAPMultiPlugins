%define Product	LDAPMultiPlugins
%define product	ldapmultiplugins
%define name    zope-%{Product}
%define version 1.5
%define release %mkrel 1

%define zope_minver	2.7
%define plone_minver	2.0
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Provides PluggableAuthService plugins that interoperate with LDAP
License:	GPL
Group:		System/Servers
URL:		http://www.dataflake.org/software/ldapultiplugins/
Source:		http://www.dataflake.org/software/ldapmultiplugins/ldapmultiplugins_%{version}/LDAPMultiPlugins-%{version}.tgz
Requires:	zope >= %{zope_minver}
Requires:	plone >= %{plone_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The LDAPMultiPlugins provides PluggableAuthService plugins that
interoperate with LDAP.

%prep
%setup -c -q

%build
# Not much, eh? :-)

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{Product} %{buildroot}%{software_home}/Products/%{product}

%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
