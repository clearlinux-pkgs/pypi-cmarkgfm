#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-cmarkgfm
Version  : 2022.10.27
Release  : 41
URL      : https://files.pythonhosted.org/packages/94/29/b3c6f8bcaf9332e337f3ac178c3dd729e7148d2a478272779dd33f87b729/cmarkgfm-2022.10.27.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/29/b3c6f8bcaf9332e337f3ac178c3dd729e7148d2a478272779dd33f87b729/cmarkgfm-2022.10.27.tar.gz
Summary  : Minimal bindings to GitHub's fork of cmark
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-cmarkgfm-license = %{version}-%{release}
Requires: pypi-cmarkgfm-python = %{version}-%{release}
Requires: pypi-cmarkgfm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
cmarkgfm - Python bindings to GitHub's cmark
============================================

%package license
Summary: license components for the pypi-cmarkgfm package.
Group: Default

%description license
license components for the pypi-cmarkgfm package.


%package python
Summary: python components for the pypi-cmarkgfm package.
Group: Default
Requires: pypi-cmarkgfm-python3 = %{version}-%{release}

%description python
python components for the pypi-cmarkgfm package.


%package python3
Summary: python3 components for the pypi-cmarkgfm package.
Group: Default
Requires: python3-core
Provides: pypi(cmarkgfm)
Requires: pypi(cffi)

%description python3
python3 components for the pypi-cmarkgfm package.


%prep
%setup -q -n cmarkgfm-2022.10.27
cd %{_builddir}/cmarkgfm-2022.10.27
pushd ..
cp -a cmarkgfm-2022.10.27 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683036331
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cmarkgfm
cp %{_builddir}/cmarkgfm-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cmarkgfm/592ea524450874d50778dd5db4a8dd176a0261e2 || :
cp %{_builddir}/cmarkgfm-%{version}/third_party/cmark/COPYING %{buildroot}/usr/share/package-licenses/pypi-cmarkgfm/fa524e3e5b56232fdada455ba84c938f5a1487d2 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cmarkgfm/592ea524450874d50778dd5db4a8dd176a0261e2
/usr/share/package-licenses/pypi-cmarkgfm/fa524e3e5b56232fdada455ba84c938f5a1487d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
