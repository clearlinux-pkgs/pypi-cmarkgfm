#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cmarkgfm
Version  : 0.8.0
Release  : 27
URL      : https://files.pythonhosted.org/packages/b2/e6/2b0dc26ce2fa72b583d17e4f86ef01a378c296390293bc88df1a950c6065/cmarkgfm-0.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b2/e6/2b0dc26ce2fa72b583d17e4f86ef01a378c296390293bc88df1a950c6065/cmarkgfm-0.8.0.tar.gz
Summary  : Minimal bindings to GitHub's fork of cmark
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-cmarkgfm-license = %{version}-%{release}
Requires: pypi-cmarkgfm-python = %{version}-%{release}
Requires: pypi-cmarkgfm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cffi)

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
%setup -q -n cmarkgfm-0.8.0
cd %{_builddir}/cmarkgfm-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646510221
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cmarkgfm
cp %{_builddir}/cmarkgfm-0.8.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cmarkgfm/592ea524450874d50778dd5db4a8dd176a0261e2
cp %{_builddir}/cmarkgfm-0.8.0/third_party/cmark/COPYING %{buildroot}/usr/share/package-licenses/pypi-cmarkgfm/fa524e3e5b56232fdada455ba84c938f5a1487d2
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
