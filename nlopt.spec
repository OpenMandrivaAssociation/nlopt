%global flavor @BUILD_FLAVOR@%{nil}

%define pname nlopt

Name:           nlopt
Version:        2.7.1
Release:        1
Summary:        A library for nonlinear optimization
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://nlopt.readthedocs.io/en/latest/
Source0:        https://github.com/stevengj/nlopt/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-numpy
BuildRequires:  swig
#BuildRequires:  pkgconfig(octave)
Requires:       python-numpy

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package     -n lib%{pname}0
Summary:        A library for nonlinear optimization
Group:          System/Libraries

%description -n lib%{pname}0
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package -n     %{pname}-devel
Summary:        Development files for %{pname}
Group:          Development/Libraries/C and C++
Requires:       lib%{pname}0 = %{version}

%description -n %{pname}-devel
The %{pname}-devel package contains libraries and header files for
developing applications that use NLopt.

#package     -n octave-nlopt_optimize
#Summary:        Octave interface to nonlinear optimization libray
#Group:          Productivity/Scientific/Math
#Requires:   octave-cli

#description -n octave-nlopt_optimize
#NLopt is a free/open-source library for nonlinear optimization,
#providing a common interface for a number of different free
#optimization routines available online as well as original
#implementations of various other algorithms.

#This package contains the Octave interface for NLopt.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
%cmake \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=ON \
   -DNLOPT_TESTS:BOOL=ON \
   -DNLOPT_PYTHON:BOOL=ON \
   -DNLOPT_OCTAVE:BOOL=OFF \
   -DNLOPT_SWIG:BOOL=ON \
   -DPYTHON_EXECUTABLE=%{_bindir}/$python
%make_build

%install
export PYTHON=$python
pushd ../${PYTHON}_build
%make_install -C build
# remove files from the main package
for e in %{_includedir} %{_libdir}/lib\* %{_libdir}/pkgconfig %{_libdir}/cmake %{_mandir} ; do
    rm -R %{buildroot}/${e}
done
%fdupes %{buildroot}%{$python_sitearch}

%files -n lib%{pname}0
%{_libdir}/*.so.*

%files -n %{pname}-devel
%license COPYING
%doc AUTHORS NEWS.md README.md TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{pname}.pc
%{_libdir}/cmake/%{pname}/
%{_mandir}/man3/*.3%{?ext_man}

%files
%license COPYING
%{python_sitearch}/*

%files -n octave-nlopt_optimize
%license COPYING
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%{_datadir}/octave/*/site/m/*
