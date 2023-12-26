%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
%bcond_without bindings
%endif
%if "%{flavor}" == "main"
%bcond_with   bindings
%define psuffix -main
%endif
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
%if %{with bindings}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  swig
BuildRequires:  pkgconfig(octave)
Requires:       python-numpy
%endif

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.


%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%cmake \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=ON \
   -DNLOPT_TESTS:BOOL=ON \
   -DNLOPT_PYTHON:BOOL=OFF \
   -DNLOPT_OCTAVE:BOOL=OFF \
   -DNLOPT_SWIG:BOOL=OFF \
   %{nil}
%make_build

%install
%make_install -C build

%files
%{_libdir}/*.so.*
%{_libdir}/libnlopt.so
%{_libdir}/cmake/
%{_includedir}/nlopt.f
%{_includedir}/nlopt.h
%{_includedir}/nlopt.hpp
%{_libdir}/pkgconfig/nlopt.pc
%{_mandir}/man3/*
