%define 	zope_subname	PlacelessTranslationService
Summary:	PTS is, a translation service for Zope
Summary(pl):	PTS - us³uga pomagaj±ca lokalizowaæ us³ugi Zope
Name:		Zope-%{zope_subname}
Version:	1.2.3
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://plone.org/products/pts/releases/%{version}/PlacelessTranslationService-%{version}.tar.gz
# Source0-md5:	21d3fab97b2cb08c9bc422e7984383e2
URL:		http://plone.org/products/pts/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Conflicts:	Zope-CMFPlone <= 2.0.5-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PTS is, a translation service. It's a zope-wide service, which reads
"PO" format files containing translations for messages, and provides
these translations to Zope software when requested.

%description -l pl
PTS jest us³ug± pomagaj±c± lokalizowaæ us³ugi Zope. Czyta pliki
formatu "PO" zawieraj±ce t³umaczenia i udostêpnia te t³umaczenia,
kiedy odpowiedni produkt o to poprosi.

%prep
%setup -q -c
find . -type d -name .svn | xargs rm -rf
rm -rf %{zope_subname}/doc/license.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af %{zope_subname}/{bin,i18n,tests,www,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/doc/*
%{_datadir}/%{name}
