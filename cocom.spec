Summary:	cocom
Summary(pl):	cocom
Name:		cocom
Version:	0.995
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://odsl.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:
#BuildRequires:
#Requires:
URL:
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-- empty --

%description -l pl
-- pusty --

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
