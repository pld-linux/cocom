Summary:	cocom
Summary(pl):	cocom
Name:		cocom
Version:	0.995
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://osdn.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:
#BuildRequires:
#Requires:
URL:		http://cocom.sourceforge.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-- empty --

%description -l pl
-- pusty --

%package devel
Summary:	cocom-devel
Group:		Base
%description devel
%description devel -l pl

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_libdir}/*
%attr(644,root,root) %{_libdir}/*/*

%files devel
%defattr(644,root,root,755)
%doc
%attr(644,root,root) %{_includedir}/*
