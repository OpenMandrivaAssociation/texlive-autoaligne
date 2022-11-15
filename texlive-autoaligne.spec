Name:		texlive-autoaligne
Version:	56966
Release:	1
Summary:	Align terms and members in math expressions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autoaligne
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaligne.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaligne.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to align terms and members between lines
containing math expressions.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/autoaligne
%doc %{_texmfdistdir}/doc/generic/autoaligne

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
