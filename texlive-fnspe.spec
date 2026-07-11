%global tl_name fnspe
%global tl_revision 45360

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	Macros for supporting mainly students of FNSPE CTU in Prague
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fnspe
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnspe.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnspe.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is primary intended for students of FNSPE CTU in Prague but
many other students or scientists can found this package as useful. This
package implements different standards of tensor notation, interval
notation and complex notation. Further many macros and shortcuts are
added, e.q. for spaces, operators, physics unit, etc.

