%define pkgname PTSerif

Summary:	Fonts to support national alphabet of Russian people
Name:		fonts-ttf-ptserif
Version:	0.1
Release:	%mkrel 2
License:	ParaType Free Font License
Group:		System/Fonts/True type
URL:		http://www.paratype.com/public/
Source0:	http://www.fontstock.com/public/%{pkgname}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
PT Serif is a transitional serif face with humanistic terminals designed
for use together with PT Sans and harmonized with PT Sans on metrics,
proportions, weights and design. PT Serif consists of six styles: regular
and bold weights with corresponding italics form a standard computer font
family for basic text setting; two caption styles (regular and italic) are
for texts of small point sizes.

Designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov.
Released by ParaType in 2010. 

%prep
%setup -q -c -n %{pkgname}
dos2unix *.txt
iconv -f cp1252 -t utf8 'PT Free Font License_eng_1.2.txt' > 'PT-Free-Font-License_eng_1.2.txt'

%build

%install
mkdir -p %{buildroot}%{_xfontdir}/TTF/ptserif

install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/ptserif
ttmkfdir %{buildroot}%{_xfontdir}/TTF/ptserif -o %{buildroot}%{_xfontdir}/TTF/ptserif/fonts.dir
ln -s fonts.dir %{buildroot}%{_xfontdir}/TTF/ptserif/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/ptserif \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ptserif:pri=50

%files
%doc PT-Free-Font-License_eng_1.2.txt
%dir %{_xfontdir}/TTF/ptserif
%{_xfontdir}/TTF/ptserif/*.ttf
%verify(not mtime) %{_xfontdir}/TTF/ptserif/fonts.dir
%{_xfontdir}/TTF/ptserif/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-ptserif:pri=50
