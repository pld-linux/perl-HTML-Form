#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Form
Summary:	HTML::Form - Class that represents an HTML form element
Summary(pl.UTF-8):	HTML::Form - klasa reprezentująca formularz HTML
Name:		perl-HTML-Form
Version:	6.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6dab3beda31a0c17cb6b5051a9a9c84
URL:		https://metacpan.org/release/HTML-Form
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Encode >= 2
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTTP-Message >= 6
BuildRequires:	perl-URI >= 1.10
%endif
Requires:	perl-Encode >= 2
Requires:	perl-HTML-Parser
Requires:	perl-URI >= 1.10
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Objects of the HTML::Form class represents a single HTML
<form>...</form> instance. A form consists of a sequence of inputs
that usually have names, and which can take on various values. The
state of a form can be tweaked and it can then be asked to provide
HTTP::Request objects that can be passed to the request() method of
LWP::UserAgent.

%description -l pl.UTF-8
Obiekt klasy HTML::Form reprezentuje pojedynczą instancję formularza
HTML (<form>...</form>). Formularz składa się z ciągu pól
wprowadzania, zwykle mających swoje nazwy i mogących przyjmować
różne wartości. Stan formularza może być zmieniany i po przekazaniu
obiektów HTTP::Request może być przekazany do metody request()
klasy LWP::UserAgent.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTML/Form.pm
%{_mandir}/man3/HTML::Form.3pm*
