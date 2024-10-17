Name:		texlive-fnspe
Version:	45360
Release:	2
Summary:	Macros for supporting mainly students of FNSPE CTU in Prague
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fnspe
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnspe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnspe.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is primary intended for students of FNSPE CTU in
Prague but many other students or scientists can found this
package as useful. This package implements different standards
of tensor notation, interval notation and complex notation.
Further many macros and shortcuts are added, e.q. for spaces,
operators, physics unit, etc.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fnspe
%doc %{_texmfdistdir}/doc/latex/fnspe

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
