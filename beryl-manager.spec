Summary:	An application to run and [manage|control] beryl
Summary(pl):	Aplikacja do uruchamiania i zarz±dzania berylem
Name:		beryl-manager
Version:	0.1.3
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c9559154c20db1bb41d3d480cfdf0299
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
Requires:	beryl-core >= 1:0.1.3
Obsoletes:	compiz-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application to run and [manage|control] beryl.

%description -l pl
Aplikacja do uruchamiania i zarz±dzania berylem.

%prep
%setup -q
mv -f po/{ar_AR,ar}.po
mv -f po/{ca_ES,ca}.po
mv -f po/{de_DE,de}.po
mv -f po/{es_ES,es}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{gl_ES,gl}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{ja_JP,ja}.po
mv -f po/{ko_KR,ko}.po
mv -f po/{my_MY,my}.po
mv -f po/{nl_NL,nl}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{ru_RU,ru}.po
mv -f po/{sk_SK,sk}.po
mv -f po/{sv_SE,sv}.po
mv -f po/{tr_TR,tr}.po
# gl_GL is outdated and looks bogus 
# nl_BE is identical to nl_NL
# sv_FI is identical to sv_SE

# NOTE: check the list after any upgrade!
cat > po/LINGUAS <<EOF
ar
ca
de
es
es_AR
fr
gl
hu
it
ja
ko
my
nl
pt_BR
pt
ru
sk
sv
tr
zh_CN
zh_HK
zh_TW
EOF

%build
%{__intltoolize}
%{__glib_gettextize} --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-mime-update
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
%{_iconsdir}/*/*/*/beryl-manager.*
%{_pixmapsdir}/*.png
%{_mandir}/man1/*.1*
