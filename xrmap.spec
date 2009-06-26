#
# TODO: separate subpackages with at least pdfmaps and eawpats
Summary:	xrmap - generate maps of the Earth with an amazing accuracy
Summary(pl.UTF-8):	xrmap - generowanie map Ziemi z zadziwiającą dokładnością
Name:		xrmap
Version:	2.30
Release:	1
License:	GPL v2 + others - see README for details
Group:		X11/Applications/Science
Source0:	http://frmas.free.fr/files/%{name}-%{version}.tar.bz2
# Source0-md5:	f3d37e38337aaae35c9ea7d3499002eb
Source1:	http://frmas.free.fr/files/CIA_WDB2.jpd.bz2
# Source1-md5:	8b5255a685bbb5eef2f86df182731a32
Source2:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/anthems-1.2.tar.bz2
# Source2-md5:	f69ffa62fa798a62657038250786795d
Source3:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/flags-1.1.tar.bz2
# Source3-md5:	e15fbfb1f1c8a313573ac499fb0ea090
Source4:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/hymns-1.3.tar.bz2
# Source4-md5:	85483d2fe168e0b5e8ca4fc422341ee6
Source5:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/factbook_text_2002.tar.bz2
# Source5-md5:	d28fc69a9fd48d9d39a1fda8099cfb1b
Source6:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/factbook_html_2002.tar.bz2
# Source6-md5:	7909b52825123c677369eb723e5b267f
Source7:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/pdfmaps-1.3.tar.bz2
# Source7-md5:	049df5f1c9d3f1fe105d214ce45ef687
Source8:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/eawpats12.tar.bz2
# Source8-md5:	7d1b390e976ca121a6713f779a7c2148
# there are also {png,xpm}_{150,480} available
Source9:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/flags-2.9-eps.tar.bz2
# Source9-md5:	9df0819ef558796442cfc72784c9b92e
Source10:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/flags-2.9-svg.tar.bz2
# Source10-md5:	714f367a44ece703548b498406ad8936
Source11:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/earthdata_med_res.tar.bz2
# Source11-md5:	d1754a7bf81d97c3338da30db467598c
Source12:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/etopo2.bz2
# Source12-md5:	376e8990e775497a4c7a808d33cb840e
Source13:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/etopo5.bz2
# Source13-md5:	4d21bfee318688f44badccec54184362
Source14:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/population.dat.bz2
# Source14-md5:	0fa2a9b9805f55aa021456bccd4f5281
# each coat of arms has its specific copyright
#Source15:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/coat_of_arms-2.10.tar.bz2
URL:		http://frmas.free.fr/li_1.htm
BuildRequires:	gpsd-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-imake
BuildRequires:	zlib-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xrmap program provides a user-friendly X client for generating
images of the Earth and manipulating the CIA World data bank II global
vector information (a huge geodata set of about 45 MB). Available
features include coastlines and islands, political boundaries, major
and minor rivers, glaciers, lakes, canals, reefs, etc. The images can
be accurately zoomed in, up to a factor of 100 or more. The package
also contains a rather comprehensive data set of world cities and
locations - about 20000 cities are listed.

%description -l pl.UTF-8
Program Xrmap dostarcza przyjaznego dla użytkownika klienta X do
generowania obrazów Ziemi i przetwarzania ogólnoświatowych informacji
wektorowych z CIA World Data Bank (dużego zbioru informacji
geograficznych o objętości około 45MB). Możliwości obejmują linie
wybrzeży i wyspy, granice polityczne, większe i mniejsze rzeki,
lodowce, jeziora, kanały, rafy itp. Obrazy mogą być szczegółowo
powiększane aż do współczynnika 100 lub więcej. Pakiet zawiera także
dość obszerny zbiór danych o miastach z całego świata i położeniach -
dostępna jest lista około 20000 miast.

%prep
%setup -q

sed -i -e 's/-O //' Imakefile

%build
xmkmf
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

# originally DESTDIR was meant as prefix, but we can abuse it
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	SHAREDIR=%{_datadir}/rmap

bzip2 -dc %{SOURCE1} > $RPM_BUILD_ROOT%{_datadir}/rmap/CIA_WDB2.jpd
tar jxf %{SOURCE2} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE3} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE4} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE5} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE6} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE7} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE8} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE9} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE10} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE11} -C $RPM_BUILD_ROOT%{_datadir}/rmap
bzip2 -dc %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/rmap/etopo2
bzip2 -dc %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/rmap/etopo2
bzip2 -dc %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/rmap/population.dat

mv -f editkit/README{,-editkit}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO WARNING editkit/README-editkit
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rmap
%{_mandir}/man1/*
