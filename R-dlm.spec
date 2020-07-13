#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dlm
Version  : 1.1.5
Release  : 30
URL      : https://cran.r-project.org/src/contrib/dlm_1.1-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dlm_1.1-5.tar.gz
Summary  : Bayesian and Likelihood Analysis of Dynamic Linear Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-dlm-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Kalman filtering and smoothing, and Bayesian
    analysis of Normal linear State Space models, also known as 
    Dynamic Linear Models.

%package lib
Summary: lib components for the R-dlm package.
Group: Libraries

%description lib
lib components for the R-dlm package.


%prep
%setup -q -c -n dlm
cd %{_builddir}/dlm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589519819

%install
export SOURCE_DATE_EPOCH=1589519819
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dlm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dlm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dlm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dlm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dlm/CITATION
/usr/lib64/R/library/dlm/DESCRIPTION
/usr/lib64/R/library/dlm/INDEX
/usr/lib64/R/library/dlm/Meta/Rd.rds
/usr/lib64/R/library/dlm/Meta/data.rds
/usr/lib64/R/library/dlm/Meta/features.rds
/usr/lib64/R/library/dlm/Meta/hsearch.rds
/usr/lib64/R/library/dlm/Meta/links.rds
/usr/lib64/R/library/dlm/Meta/nsInfo.rds
/usr/lib64/R/library/dlm/Meta/package.rds
/usr/lib64/R/library/dlm/Meta/vignette.rds
/usr/lib64/R/library/dlm/NAMESPACE
/usr/lib64/R/library/dlm/NEWS
/usr/lib64/R/library/dlm/R/dlm
/usr/lib64/R/library/dlm/R/dlm.rdb
/usr/lib64/R/library/dlm/R/dlm.rdx
/usr/lib64/R/library/dlm/data/NelPlo.rda
/usr/lib64/R/library/dlm/data/USecon.rda
/usr/lib64/R/library/dlm/doc/dlm.R
/usr/lib64/R/library/dlm/doc/dlm.Rnw
/usr/lib64/R/library/dlm/doc/dlm.pdf
/usr/lib64/R/library/dlm/doc/index.html
/usr/lib64/R/library/dlm/help/AnIndex
/usr/lib64/R/library/dlm/help/aliases.rds
/usr/lib64/R/library/dlm/help/dlm.rdb
/usr/lib64/R/library/dlm/help/dlm.rdx
/usr/lib64/R/library/dlm/help/paths.rds
/usr/lib64/R/library/dlm/html/00Index.html
/usr/lib64/R/library/dlm/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dlm/libs/dlm.so
/usr/lib64/R/library/dlm/libs/dlm.so.avx2
/usr/lib64/R/library/dlm/libs/dlm.so.avx512
