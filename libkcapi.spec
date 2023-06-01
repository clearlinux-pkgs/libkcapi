#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
#
Name     : libkcapi
Version  : 1.4.0
Release  : 19
URL      : https://github.com/smuellerDD/libkcapi/archive/v1.4.0/libkcapi-1.4.0.tar.gz
Source0  : https://github.com/smuellerDD/libkcapi/archive/v1.4.0/libkcapi-1.4.0.tar.gz
Summary  : Linux Kernel Crypto API User Space Interface Library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libkcapi-lib = %{version}-%{release}
Requires: libkcapi-license = %{version}-%{release}
BuildRequires : cppcheck
BuildRequires : docbook-xml
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : sed
BuildRequires : util-linux
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libkcapi -- Linux Kernel Crypto API User Space Interface Library [![Build Status](https://github.com/smuellerDD/libkcapi/workflows/checks/badge.svg)](https://github.com/smuellerDD/libkcapi/actions?query=branch%3Amaster)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/github/smuellerDD/libkcapi.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/smuellerDD/libkcapi/context:cpp)
================================================================

%package dev
Summary: dev components for the libkcapi package.
Group: Development
Requires: libkcapi-lib = %{version}-%{release}
Provides: libkcapi-devel = %{version}-%{release}
Requires: libkcapi = %{version}-%{release}

%description dev
dev components for the libkcapi package.


%package lib
Summary: lib components for the libkcapi package.
Group: Libraries
Requires: libkcapi-license = %{version}-%{release}

%description lib
lib components for the libkcapi package.


%package license
Summary: license components for the libkcapi package.
Group: Default

%description license
license components for the libkcapi package.


%prep
%setup -q -n libkcapi-1.4.0
cd %{_builddir}/libkcapi-1.4.0
pushd ..
cp -a libkcapi-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685639700
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685639700
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkcapi
cp %{_builddir}/libkcapi-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libkcapi/5d5f6328aa28826ff829bb743d99aa26001f7828 || :
cp %{_builddir}/libkcapi-%{version}/COPYING.bsd %{buildroot}/usr/share/package-licenses/libkcapi/44a9f67b4a6876452742044723d955958f241b2c || :
cp %{_builddir}/libkcapi-%{version}/COPYING.gplv2 %{buildroot}/usr/share/package-licenses/libkcapi/b47456e2c1f38c40346ff00db976a2badf36b5e3 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/kcapi.h
/usr/lib64/libkcapi.so
/usr/lib64/pkgconfig/libkcapi.pc
/usr/share/man/man3/kcapi_aead_authsize.3
/usr/share/man/man3/kcapi_aead_blocksize.3
/usr/share/man/man3/kcapi_aead_ccm_nonce_to_iv.3
/usr/share/man/man3/kcapi_aead_decrypt.3
/usr/share/man/man3/kcapi_aead_decrypt_aio.3
/usr/share/man/man3/kcapi_aead_destroy.3
/usr/share/man/man3/kcapi_aead_encrypt.3
/usr/share/man/man3/kcapi_aead_encrypt_aio.3
/usr/share/man/man3/kcapi_aead_getdata_input.3
/usr/share/man/man3/kcapi_aead_getdata_output.3
/usr/share/man/man3/kcapi_aead_inbuflen_dec.3
/usr/share/man/man3/kcapi_aead_inbuflen_enc.3
/usr/share/man/man3/kcapi_aead_init.3
/usr/share/man/man3/kcapi_aead_ivsize.3
/usr/share/man/man3/kcapi_aead_outbuflen_dec.3
/usr/share/man/man3/kcapi_aead_outbuflen_enc.3
/usr/share/man/man3/kcapi_aead_setassoclen.3
/usr/share/man/man3/kcapi_aead_setkey.3
/usr/share/man/man3/kcapi_aead_settaglen.3
/usr/share/man/man3/kcapi_aead_stream_init_dec.3
/usr/share/man/man3/kcapi_aead_stream_init_enc.3
/usr/share/man/man3/kcapi_aead_stream_op.3
/usr/share/man/man3/kcapi_aead_stream_update.3
/usr/share/man/man3/kcapi_aead_stream_update_last.3
/usr/share/man/man3/kcapi_akcipher_decrypt.3
/usr/share/man/man3/kcapi_akcipher_decrypt_aio.3
/usr/share/man/man3/kcapi_akcipher_destroy.3
/usr/share/man/man3/kcapi_akcipher_encrypt.3
/usr/share/man/man3/kcapi_akcipher_encrypt_aio.3
/usr/share/man/man3/kcapi_akcipher_init.3
/usr/share/man/man3/kcapi_akcipher_setkey.3
/usr/share/man/man3/kcapi_akcipher_setpubkey.3
/usr/share/man/man3/kcapi_akcipher_sign.3
/usr/share/man/man3/kcapi_akcipher_sign_aio.3
/usr/share/man/man3/kcapi_akcipher_stream_init_dec.3
/usr/share/man/man3/kcapi_akcipher_stream_init_enc.3
/usr/share/man/man3/kcapi_akcipher_stream_init_sgn.3
/usr/share/man/man3/kcapi_akcipher_stream_init_vfy.3
/usr/share/man/man3/kcapi_akcipher_stream_op.3
/usr/share/man/man3/kcapi_akcipher_stream_update.3
/usr/share/man/man3/kcapi_akcipher_verify.3
/usr/share/man/man3/kcapi_akcipher_verify_aio.3
/usr/share/man/man3/kcapi_cipher_blocksize.3
/usr/share/man/man3/kcapi_cipher_dec_aes_cbc.3
/usr/share/man/man3/kcapi_cipher_dec_aes_ctr.3
/usr/share/man/man3/kcapi_cipher_dec_sm4_cbc.3
/usr/share/man/man3/kcapi_cipher_dec_sm4_ctr.3
/usr/share/man/man3/kcapi_cipher_decrypt.3
/usr/share/man/man3/kcapi_cipher_decrypt_aio.3
/usr/share/man/man3/kcapi_cipher_destroy.3
/usr/share/man/man3/kcapi_cipher_enc_aes_cbc.3
/usr/share/man/man3/kcapi_cipher_enc_aes_ctr.3
/usr/share/man/man3/kcapi_cipher_enc_sm4_cbc.3
/usr/share/man/man3/kcapi_cipher_enc_sm4_ctr.3
/usr/share/man/man3/kcapi_cipher_encrypt.3
/usr/share/man/man3/kcapi_cipher_encrypt_aio.3
/usr/share/man/man3/kcapi_cipher_init.3
/usr/share/man/man3/kcapi_cipher_ivsize.3
/usr/share/man/man3/kcapi_cipher_setkey.3
/usr/share/man/man3/kcapi_cipher_stream_init_dec.3
/usr/share/man/man3/kcapi_cipher_stream_init_enc.3
/usr/share/man/man3/kcapi_cipher_stream_op.3
/usr/share/man/man3/kcapi_cipher_stream_update.3
/usr/share/man/man3/kcapi_cipher_stream_update_last.3
/usr/share/man/man3/kcapi_get_maxsplicesize.3
/usr/share/man/man3/kcapi_handle_reinit.3
/usr/share/man/man3/kcapi_hkdf.3
/usr/share/man/man3/kcapi_kdf_ctr.3
/usr/share/man/man3/kcapi_kdf_dpi.3
/usr/share/man/man3/kcapi_kdf_fb.3
/usr/share/man/man3/kcapi_kpp_destroy.3
/usr/share/man/man3/kcapi_kpp_dh_setparam_pkcs3.3
/usr/share/man/man3/kcapi_kpp_ecdh_setcurve.3
/usr/share/man/man3/kcapi_kpp_init.3
/usr/share/man/man3/kcapi_kpp_keygen.3
/usr/share/man/man3/kcapi_kpp_keygen_aio.3
/usr/share/man/man3/kcapi_kpp_setkey.3
/usr/share/man/man3/kcapi_kpp_ssgen.3
/usr/share/man/man3/kcapi_kpp_ssgen_aio.3
/usr/share/man/man3/kcapi_md_destroy.3
/usr/share/man/man3/kcapi_md_digest.3
/usr/share/man/man3/kcapi_md_digestsize.3
/usr/share/man/man3/kcapi_md_final.3
/usr/share/man/man3/kcapi_md_hmac_sha1.3
/usr/share/man/man3/kcapi_md_hmac_sha224.3
/usr/share/man/man3/kcapi_md_hmac_sha256.3
/usr/share/man/man3/kcapi_md_hmac_sha384.3
/usr/share/man/man3/kcapi_md_hmac_sha512.3
/usr/share/man/man3/kcapi_md_hmac_sm3.3
/usr/share/man/man3/kcapi_md_init.3
/usr/share/man/man3/kcapi_md_setkey.3
/usr/share/man/man3/kcapi_md_sha1.3
/usr/share/man/man3/kcapi_md_sha224.3
/usr/share/man/man3/kcapi_md_sha256.3
/usr/share/man/man3/kcapi_md_sha384.3
/usr/share/man/man3/kcapi_md_sha512.3
/usr/share/man/man3/kcapi_md_sm3.3
/usr/share/man/man3/kcapi_md_update.3
/usr/share/man/man3/kcapi_memset_secure.3
/usr/share/man/man3/kcapi_pad_iv.3
/usr/share/man/man3/kcapi_pbkdf.3
/usr/share/man/man3/kcapi_pbkdf_iteration_count.3
/usr/share/man/man3/kcapi_rng_destroy.3
/usr/share/man/man3/kcapi_rng_generate.3
/usr/share/man/man3/kcapi_rng_get_bytes.3
/usr/share/man/man3/kcapi_rng_init.3
/usr/share/man/man3/kcapi_rng_seed.3
/usr/share/man/man3/kcapi_rng_seedsize.3
/usr/share/man/man3/kcapi_set_maxsplicesize.3
/usr/share/man/man3/kcapi_set_verbosity.3
/usr/share/man/man3/kcapi_version.3
/usr/share/man/man3/kcapi_versionstring.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkcapi.so.1.4.0
/usr/lib64/libkcapi.so.1
/usr/lib64/libkcapi.so.1.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkcapi/44a9f67b4a6876452742044723d955958f241b2c
/usr/share/package-licenses/libkcapi/5d5f6328aa28826ff829bb743d99aa26001f7828
/usr/share/package-licenses/libkcapi/b47456e2c1f38c40346ff00db976a2badf36b5e3
