# TODO: revise packaging?
Summary:	COCOM tool set
Summary(pl):	Zestaw narzêdzi COCOM
Name:		cocom
Version:	0.995
Release:	0.2
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/cocom/%{name}-%{version}.tar.gz
# Source0-md5:	94040380e63afd6cb12d2abacb87f8c8
URL:		http://cocom.sourceforge.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is COCOM tool set (Russian Armoury) oriented onto the creation
of compilers, cross-compilers, interpreters, and other language
processors. The distribution also contains interpreter of language
DINO as an example of the tool set usage. The tool set is aimed to
use on Unixes of different flavors. COCOM also has been ported also
into WIN32 environment.

%description -l pl
To jest zestaw narzêdzi COCOM (arsena³ rosyjski), zorientowany na
tworzenie kompilatorów, kompilatorów skro¶nych, interpreterów i
innych procesorów jêzyków. Pakiet zawiera tak¿e interpreter jêzyka
DINO jako przyk³ad u¿ycia tego zestawu narzêdzi. Narzêdzia s±
przeznaczone do u¿ywania na ró¿nych uniksach, ale zosta³y sportowane
tak¿e do ¶rodowiska Win32.

%package devel
Summary:	COCOM header files
Summary(pl):	Pliki nag³ówkowe COCOM
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
COCOM header files.

%description devel -l pl
Pliki nag³ówkowe COCOM.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README armoury.html cocom.html *.jpg
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libcocom*.a
%{_libdir}/*.sprut
%dir %{_libdir}/dino-*
%attr(755,root,root) %{_libdir}/dino-*/*.so
%{_libdir}/dino-*/lib*.a
%{_libdir}/dino-*/*.d
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/dino-*
