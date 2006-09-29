#
Summary:	An application to run and [manage|control] beryl
Summary(pl):	Aaplikacja do uruchamiania i kontroli beryla
Name:		beryl-manager
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://distfiles.xgl-coffee.org/beryl-manager/%{name}-%{version}.tar.bz2
# Source0-md5:	1ab7696d4f91c11eb86a252647d3a021
URL:		http://distfiles.xgl-coffee.org
BuildRequires:	gtk+2-devel >= 2:2.0
Requires:	beryl-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application to run and [manage|control] beryl

%prep
%setup -q -n %{name}

%build
autoreconf -v --install
%{__intltoolize}
%{__glib_gettextize} --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/beryl-manager.png
