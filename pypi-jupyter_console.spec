#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_console
Version  : 6.4.4
Release  : 57
URL      : https://files.pythonhosted.org/packages/1b/2f/acb5851aa3ed730f8cde5ec9eb0c0d9681681123f32c3b82d1536df1e937/jupyter_console-6.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/2f/acb5851aa3ed730f8cde5ec9eb0c0d9681681123f32c3b82d1536df1e937/jupyter_console-6.4.4.tar.gz
Summary  : Jupyter terminal console
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: pypi-jupyter_console-bin = %{version}-%{release}
Requires: pypi-jupyter_console-license = %{version}-%{release}
Requires: pypi-jupyter_console-python = %{version}-%{release}
Requires: pypi-jupyter_console-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ipykernel)
BuildRequires : pypi(ipython)
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(prompt_toolkit)
BuildRequires : pypi(pygments)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
# Jupyter Console
[![Build Status](https://travis-ci.org/jupyter/jupyter_console.svg?branch=master)](https://travis-ci.org/jupyter/jupyter_console)
[![Documentation Status](http://readthedocs.org/projects/jupyter-console/badge/?version=latest)](https://jupyter-console.readthedocs.io/en/latest/?badge=latest)

%package bin
Summary: bin components for the pypi-jupyter_console package.
Group: Binaries
Requires: pypi-jupyter_console-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyter_console package.


%package license
Summary: license components for the pypi-jupyter_console package.
Group: Default

%description license
license components for the pypi-jupyter_console package.


%package python
Summary: python components for the pypi-jupyter_console package.
Group: Default
Requires: pypi-jupyter_console-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_console package.


%package python3
Summary: python3 components for the pypi-jupyter_console package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_console)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(prompt_toolkit)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-jupyter_console package.


%prep
%setup -q -n jupyter_console-6.4.4
cd %{_builddir}/jupyter_console-6.4.4
pushd ..
cp -a jupyter_console-6.4.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655999221
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_console
cp %{_builddir}/jupyter_console-6.4.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_console/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-console

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_console/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
