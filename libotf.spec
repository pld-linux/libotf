#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Library for handling OpenType Font (OTF)
Summary(pl.UTF-8):	Biblioteka do obsługi fontów OpenType (OTF)
Name:		libotf
Version:	0.9.16
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
# Source0-md5:	9b0b708ba5de53bf83e1cb09c6a6e100
URL:		http://www.nongnu.org/m17n/
BuildRequires:	freetype-devel >= 2
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The library "libotf" provides the following facilites:
 - read Open Type Layout Tables from OTF file. Currently these
   tables are supported; head, name, cmap, GDEF, GSUB, and GPOS.
 - convert a Unicode character sequence to a glyph code sequence by
   using the above tables.

The combination of libotf and the FreeType library (Ver.2) realizes
CTL (complex text layout) by OpenType fonts.

%description -l pl.UTF-8
Biblioteka libotf zapewnia następującą funkcjonalność:
 - odczyt tablic Open Type Layout z plików OTF; obecnie obsługiwane
   są następujące tablice: head, name, cmap, GDEF, GSUB i GPOS.
 - konwersja sekwencji znaków unikodowych na sekwencje kodów glifów
   z użyciem tych tablic.

%package devel
Summary:	Header files for libotf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libotf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2

%description devel
Header files for libotf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libotf.

%package static
Summary:	Static libotf library
Summary(pl.UTF-8):	Statyczna biblioteka libotf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libotf library.

%description static -l pl.UTF-8
Statyczna biblioteka libotf.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libotf.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/otfdump
%attr(755,root,root) %{_bindir}/otflist
%attr(755,root,root) %{_bindir}/otftobdf
%attr(755,root,root) %{_bindir}/otfview
%attr(755,root,root) %{_libdir}/libotf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libotf.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libotf-config
%attr(755,root,root) %{_libdir}/libotf.so
%{_includedir}/otf.h
%{_pkgconfigdir}/libotf.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libotf.a
%endif
