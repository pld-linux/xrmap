#
# TODO: separate subpackages with at least pdfmaps and eawpats
Summary:	xrmap - generate maps of the Earth with an amazing accuracy
Summary(pl):	xrmap - generowanie map Ziemi z zadziwiaj±c± dok³adno¶ci±
Name:		xrmap
Version:	2.30
Release:	1
License:	GPL v2 + others - see README for details
Group:		X11/Applications/Science
Source0:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/%{name}-%{version}.tar.bz2
# Source0-md5:	f3d37e38337aaae35c9ea7d3499002eb
Source1:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/CIA_WDB2.jpd.gz
# Source1-md5:	5a08415115ef4555aa6ba5e8a19791ec
Source2:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/anthems-1.1.tar.bz2
# Source2-md5:	4d63e6a61e9197f3c382e518de6503db
Source3:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/flags-1.1.tar.bz2
# Source3-md5:	e15fbfb1f1c8a313573ac499fb0ea090
Source4:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/hymns-1.2.tar.bz2
# Source4-md5:	b5c1c26e1d5c842c53c9a5460cb02864
Source5:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/factbook_text_2002.tar.bz2
# Source5-md5:	d28fc69a9fd48d9d39a1fda8099cfb1b
Source6:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/factbook_html_2002.tar.bz2
# Source6-md5:	7909b52825123c677369eb723e5b267f
Source7:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/pdfmaps-1.1.tar.gz
# Source7-md5:	9a40499034f7a98949ab690731eb6e70
Source8:	ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/data/eawpats12.tar.bz2
# Source8-md5:	7d1b390e976ca121a6713f779a7c2148
URL:		http://frmas.free.fr/li_1.htm
BuildRequires:	XFree86-devel
BuildRequires:	imake
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

%description -l pl
Program Xrmap dostarcza przyjaznego dla u¿ytkownika klienta X do
generowania obrazów Ziemi i przetwarzania ogólno¶wiatowych informacji
wektorowych z CIA World Data Bank (du¿ego zbioru informacji
geograficznych o objêto¶ci oko³o 45MB). Mo¿liwo¶ci obejmuj± linie
wybrze¿y i wyspy, granice polityczne, wiêksze i mniejsze rzeki,
lodowce, jeziora, kana³y, rafy itp. Obrazy mog± byæ szczegó³owo
powiêkszane a¿ do wspó³czynnika 100 lub wiêcej. Pakiet zawiera tak¿e
do¶æ obszerny zbiór danych o miastach z ca³ego ¶wiata i po³o¿eniach -
dostêpna jest lista oko³o 20000 miast.

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

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE2} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE3} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE4} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE5} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE6} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE7} -C $RPM_BUILD_ROOT%{_datadir}/rmap
tar jxf %{SOURCE8} -C $RPM_BUILD_ROOT%{_datadir}/rmap

mv -f editkit/README{,-editkit}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO WARNING editkit/README-editkit
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rmap
%{_mandir}/man1/*
