#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Array
Summary:	Set::Array - arrays as objects with lots of handy methods
Summary(pl.UTF-8):	Set::Array - tablice jako obiekty z wieloma poręcznymi metodami
Name:		perl-Set-Array
Version:	0.18
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	32a60b3d384dada7628be132467549e4
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Want >= 0.05
BuildRequires:	perl-Test-Deep
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

%description -l pl.UTF-8
Set::Array pozwala na tworzenie tablic jako obiektów i używanie na
nich metod. Dostępnych jest wiele wygodnych metod, które podane są w
FAQ-ach, Perl Cookbook oraz postach z grupy comp.lang.perl.misc.
Dodatkowo są metody Set z odpowiadającymi (przeciążonymi) operatorami
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
