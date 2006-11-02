Summary:	An application to run and [manage|control] beryl
Summary(pl):	Aplikacja do uruchamiania i zarz±dzania berylem
Name:		beryl-manager
Version:	20061102
Release:	1
License:	LGPL v2+
Group:		X11/Window Managers/Tools
#Source0:	http://distfiles.xgl-coffee.org/beryl-manager/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	8947ff077d4aa27dc76aa097484a4799
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
Requires:	beryl-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application to run and [manage|control] beryl.

%description -l pl
Aplikacja do uruchamiania i zarz±dzania berylem.

%prep
%setup -q -n %{name}

mv -f po/{ar_AR,ar}.po
mv -f po/{de_DE,de}.po
mv -f po/{es_ES,es}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{it_IT,it}.po
mv -f po/{ko_KR,ko}.po
mv -f po/{my_MY,my}.po
mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{ru_RU,ru}.po
mv -f po/{sk_SK,sk}.po
mv -f po/{sv_SE,sv}.po

# NOTE: check the list ofter any upgrade!
cat > po/LINGUAS <<EOF
ar
de
en_US
es
fr
it
ko
my
nl
it
pt_BR
pt
ru
sk
sv
zh_CN
EOF

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
%{_pixmapsdir}/*
%{_mandir}/man1/*.1*
