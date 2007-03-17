Summary:	An application to run and [manage|control] beryl
Summary(pl.UTF-8):	Aplikacja do uruchamiania i zarządzania berylem
Name:		beryl-manager
Version:	0.2.0
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	5bd0fb5786b6d79d6ebe87c14ba668c9
Patch0:		%{name}-desktop.patch
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	beryl-core >= 1:%{version}
Obsoletes:	compiz-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application to run and [manage|control] beryl.

%description -l pl.UTF-8
Aplikacja do uruchamiania i zarządzania berylem.

%prep
%setup -q
%patch0 -p1
mv -f po/{ar_AR,ar}.po
mv -f po/{de_DE,de}.po
mv -f po/{es_ES,es}.po
mv -f po/{gl_ES,gl}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{my_MY,my}.po
mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{ru_RU,ru}.po
mv -f po/{sk_SK,sk}.po
mv -f po/{sv_SE,sv}.po
mv -f po/{tr_TR,tr}.po
mv -f po/{uk_UA,uk}.po

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
nb
nl
pl
pt_BR
pt
ru
sk
sv
tr
uk
zh_CN
zh_HK
zh_TW
EOF

%build
%{__glib_gettextize}
%{__intltoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/beryl-manager.desktop
%{_iconsdir}/hicolor/*/*/beryl-manager.*
%{_pixmapsdir}/*.png
%{_mandir}/man1/*.1*
