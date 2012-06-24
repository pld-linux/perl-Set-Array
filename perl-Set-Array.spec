#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	Array
Summary:	Set::Array - Arrays as objects with lots of handy methods
Summary(pl):	Set::Array - tablice jako obiekty z wieloma por�cznymi metodami
Name:		perl-Set-Array
Version:	0.10
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Want >= 0.05
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Array allows you to create arrays as objects and use OO-style
methods on them. Many convenient methods are provided here that appear
in the FAQ's, the Perl Cookbook or posts from comp.lang.perl.misc. In
addition, there are Set methods with corresponding (overloaded)
operators for the purpose of Set comparison, i.e. +, ==, etc.

%description -l pl
Set::Array pozwala na tworzenie tablic jako obiekt�w i u�ywanie na
nich metod. Dost�pnych jest wiele wygodnych metod, kt�re podane s� w
FAQ-ach, Perl Cookbook oraz postach z grupy comp.lang.perl.misc.
Dodatkowo s� metody Set z odpowiadaj�cymi (przeci��onymi) operatorami
do por�wnywania, np. +, == itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
