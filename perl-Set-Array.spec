#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Array
Summary:	Set::Array - arrays as objects with lots of handy methods
Summary(pl):	Set::Array - tablice jako obiekty z wieloma porêcznymi metodami
Name:		perl-Set-Array
Version:	0.14
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	7509d4d50551b07cb3e083335c7742e8
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Want >= 0.05
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Array allows you to create arrays as objects and use OO-style
methods on them. Many convenient methods are provided here that appear
in the FAQ's, the Perl Cookbook or posts from comp.lang.perl.misc. In
addition, there are Set methods with corresponding (overloaded)
operators for the purpose of Set comparison, i.e. +, ==, etc.

%description -l pl
Set::Array pozwala na tworzenie tablic jako obiektów i u¿ywanie na
nich metod. Dostêpnych jest wiele wygodnych metod, które podane s± w
FAQ-ach, Perl Cookbook oraz postach z grupy comp.lang.perl.misc.
Dodatkowo s± metody Set z odpowiadaj±cymi (przeci±¿onymi) operatorami
do porównywania, np. +, == itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
