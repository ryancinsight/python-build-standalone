# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

DOWNLOADS = {
    # 6.0.19 is the last version licensed under the Sleepycat license.
    "bdb": {
        "url": "https://ftp.osuosl.org/pub/blfs/conglomeration/db/db-6.0.19.tar.gz",
        "size": 36541923,
        "sha256": "2917c28f60903908c2ca4587ded1363b812c4e830a5326aaa77c9879d13ae18e",
        "version": "6.0.19",
        "library_names": ["db"],
        "licenses": ["Sleepycat"],
        "license_file": "LICENSE.bdb.txt",
    },
    "binutils": {
        "url": "ftp://ftp.gnu.org/gnu/binutils/binutils-2.35.1.tar.xz",
        "size": 22031720,
        "sha256": "3ced91db9bf01182b7e420eab68039f2083aed0a214c0424e257eae3ddee8607",
        "version": "2.35.1",
    },
    "bzip2": {
        "url": "https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
        "size": 810029,
        "sha256": "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269",
        "version": "1.0.8",
        "library_names": ["bz2"],
        "licenses": ["bzip2-1.0.6"],
        "license_file": "LICENSE.bzip2.txt",
    },
    "clang": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.1/clang-11.0.1.src.tar.xz",
        "size": 14849680,
        "sha256": "73f572c2eefc5a155e01bcd84815751d722a4d3925f53c144acfb93eeb274b4d",
        "version": "11.0.1",
    },
    "clang-compiler-rt": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.1/compiler-rt-11.0.1.src.tar.xz",
        "size": 2136216,
        "sha256": "087be3f1116e861cd969c9b0b0903c27028b52eaf45157276f50a9c2500687fc",
        "version": "11.0.1",
    },
    "cmake-linux-bin": {
        "url": "https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-Linux-x86_64.tar.gz",
        "size": 42931014,
        "sha256": "4d8a6d852c530f263b22479aad196416bb4406447e918bd9759c6593b7f5f3f9",
        "version": "3.19.2",
    },
    "cmake-macos-bin": {
        "url": "https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-macos-universal.tar.gz",
        "size": 63739197,
        "sha256": "50afa2cb66bea6a0314ef28034f3ff1647325e30cf5940f97906a56fd9640bd8",
        "version": "3.19.2",
    },
    "cpython-3.8": {
        "url": "https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tar.xz",
        "size": 18261096,
        "sha256": "ddcc1df16bb5b87aa42ec5d20a5b902f2d088caa269b28e01590f97a798ec50a",
        "version": "3.8.7",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp38",
    },
    "cpython-3.9": {
        "url": "https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tar.xz",
        "size": 18897104,
        "sha256": "991c3f8ac97992f3d308fefeb03a64db462574eadbff34ce8bc5bb583d9903ff",
        "version": "3.9.1",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp39",
    },
    "gcc": {
        "url": "https://ftp.gnu.org/gnu/gcc/gcc-10.2.0/gcc-10.2.0.tar.xz",
        "size": 75004144,
        "sha256": "b8dd4368bb9c7f0b98188317ee0254dd8cc99d1e3a18d0ff146c855fe16c1d8c",
        "version": "10.2.0",
    },
    "gdbm": {
        "url": "ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.18.1.tar.gz",
        "size": 941863,
        "sha256": "86e613527e5dba544e73208f42b78b7c022d4fa5a6d5498bf18c8d6f745b91dc",
        "version": "1.18.1",
        "library_names": ["gdbm"],
        "licenses": ["GPL-3.0-or-later"],
        "license_file": "LICENSE.gdbm.txt",
    },
    "gettext": {
        "url": "https://ftp.gnu.org/pub/gnu/gettext/gettext-0.21.tar.gz",
        "size": 24181849,
        "sha256": "c77d0da3102aec9c07f43671e60611ebff89a996ef159497ce8e59d075786b12",
        "version": "0.21",
        "library_names": ["intl", "textstyle"],
        "licenses": ["GPL-3.0-or-later"],
        "license_file": "LICENSE.gettext.txt",
    },
    # gmp 6.2 does not build on wheezy.
    "gmp": {
        "url": "https://ftp.gnu.org/gnu/gmp/gmp-6.1.2.tar.xz",
        "size": 1946336,
        "sha256": "87b565e89a9a684fe4ebeeddb8399dce2599f9c9049854ca8c0dfbdea0e21912",
        "version": "6.1.2",
    },
    "inputproto": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/proto/inputproto-2.3.2.tar.gz",
        "size": 244334,
        "sha256": "10eaadd531f38f7c92ab59ef0708ca195caf3164a75c4ed99f0c04f2913f6ef3",
        "version": "2.3.2",
    },
    "isl": {
        "url": "ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-0.18.tar.bz2",
        "size": 1658291,
        "sha256": "6b8b0fd7f81d0a957beb3679c81bbb34ccc7568d5682844d8924424a0dadcb1b",
        "version": "0.18",
    },
    "jom-windows-bin": {
        "url": "http://download.qt.io/official_releases/jom/jom_1_1_3.zip",
        "size": 1213852,
        "sha256": "128fdd846fe24f8594eed37d1d8929a0ea78df563537c0c1b1861a635013fff8",
        "version": "1.1.3",
    },
    "kbproto": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/proto/kbproto-1.0.7.tar.gz",
        "size": 325858,
        "sha256": "828cb275b91268b1a3ea950d5c0c5eb076c678fdf005d517411f89cc8c3bb416",
        "version": "1.0.7",
    },
    "libc++": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.1/libcxx-11.0.1.src.tar.xz",
        "size": 1871968,
        "sha256": "9fd5f669621ffea88a2b93e3d99f3a958b5defb954f71bf754709b63275f5e3d",
        "version": "11.0.1",
    },
    "libc++abi": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.1/libcxxabi-11.0.1.src.tar.xz",
        "size": 552960,
        "sha256": "4a697056a5c08621a8380dcaf3836525835aa76b3008d9e8f27abf9270bf683f",
        "version": "11.0.1",
    },
    "libedit": {
        "url": "https://www.thrysoee.dk/editline/libedit-20191231-3.1.tar.gz",
        "size": 516801,
        "sha256": "dbb82cb7e116a5f8025d35ef5b4f7d4a3cdd0a3909a146a39112095a2d229071",
        "version": "20191231-3.1",
        "library_names": ["edit"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libedit.txt",
    },
    "libffi": {
        "url": "ftp://sourceware.org/pub/libffi/libffi-3.3.tar.gz",
        "size": 1305466,
        "sha256": "72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056",
        "version": "3.3",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libpthread-stubs": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/lib/libpthread-stubs-0.1.tar.gz",
        "size": 301448,
        "sha256": "f8f7ca635fa54bcaef372fd5fd9028f394992a743d73453088fcadc1dbf3a704",
        "version": "0.1",
    },
    "libressl": {
        "url": "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-3.2.3.tar.gz",
        "size": 3839953,
        "sha256": "412dc2baa739228c7779e93eb07cd645d5c964d2f2d837a9fd56db7498463d73",
        "version": "3.2.3",
        "library_names": ["crypto", "ssl"],
        "licenses": ["OpenSSL"],
        "license_file": "LICENSE.libressl.txt",
    },
    "libX11": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/lib/libX11-1.6.8.tar.gz",
        "size": 3144482,
        "sha256": "69d1a27cba722dca897198a23fa8d3cad3ec0c715e00205ea4398ec68a4258a5",
        "version": "1.6.8",
        "library_names": ["X11", "X11-xcb"],
        "licenses": ["MIT", "X11"],
        "license_file": "LICENSE.libX11.txt",
    },
    "libXau": {
        "url": "https://www.x.org/releases/individual/lib/libXau-1.0.7.tar.gz",
        "size": 349278,
        "sha256": "cbb81b4ba0f585faac8b9914b0bdbef6e0ef886a30c70d6584e2b30efeda9ac4",
        "version": "1.0.7",
        "library_names": ["Xau"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libXau.txt",
    },
    "libxcb": {
        "url": "https://xcb.freedesktop.org/dist/libxcb-1.13.1.tar.gz",
        "size": 636748,
        "sha256": "f09a76971437780a602303170fd51b5f7474051722bc39d566a272d2c4bde1b5",
        "version": "1.13.1",
        "library_names": ["xcb"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libxcb.txt",
    },
    "lld": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.1/lld-11.0.1.src.tar.xz",
        "size": 1237040,
        "sha256": "60ba0da01a391078dcc437fee629f3bf7e30e06467a3a060b4a2a3aa661308b7",
        "version": "11.0.1",
    },
    "llvm": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-11.0.1/llvm-11.0.1.src.tar.xz",
        "size": 38914796,
        "sha256": "ccd87c254b6aebc5077e4e6977d08d4be888e7eb672c6630a26a15d58b59b528",
        "version": "11.0.1",
    },
    "mpc": {
        "url": "http://www.multiprecision.org/downloads/mpc-1.0.3.tar.gz",
        "size": 669925,
        "sha256": "617decc6ea09889fb08ede330917a00b16809b8db88c29c31bfbb49cbf88ecc3",
        "version": "1.0.3",
    },
    "mpfr": {
        "url": "https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.6.tar.xz",
        "size": 1133672,
        "sha256": "7a62ac1a04408614fccdc506e4844b10cf0ad2c2b1677097f8f35d3a1344a950",
        "version": "3.1.6",
    },
    "musl": {
        "url": "https://www.musl-libc.org/releases/musl-1.2.1.tar.gz",
        "size": 1047481,
        "sha256": "68af6e18539f646f9c41a3a2bb25be4a5cfa5a8f65f0bb647fd2bbfdf877e84b",
        "version": "1.2.1",
    },
    "ncurses": {
        "url": "https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz",
        "size": 3425862,
        "sha256": "30306e0c76e0f9f1f0de987cf1c82a5c21e1ce6568b9227f7da5b71cbea86c9d",
        "version": "6.2",
        "library_names": ["ncurses", "ncursesw", "panel", "panelw"],
        "licenses": ["X11"],
        "license_file": "LICENSE.ncurses.txt",
    },
    "ninja-linux-bin": {
        "url": "https://github.com/ninja-build/ninja/releases/download/v1.10.2/ninja-linux.zip",
        "size": 103219,
        "sha256": "763464859c7ef2ea3a0a10f4df40d2025d3bb9438fcb1228404640410c0ec22d",
        "version": "1.10.2",
    },
    "ninja-macos-bin": {
        "url": "https://github.com/ninja-build/ninja/releases/download/v1.10.2/ninja-mac.zip",
        "size": 234089,
        "sha256": "6fa359f491fac7e5185273c6421a000eea6a2f0febf0ac03ac900bd4d80ed2a5",
        "version": "1.10.2",
    },
    "openssl": {
        "url": "https://www.openssl.org/source/openssl-1.1.1i.tar.gz",
        "size": 9808346,
        "sha256": "e8be6a35fe41d10603c3cc635e93289ed00bf34b79671a3a4de64fcee00d5242",
        "version": "1.1.1i",
        "library_names": ["crypto", "ssl"],
        "licenses": ["OpenSSL"],
        "license_file": "LICENSE.openssl.txt",
    },
    "nasm-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/nasm-2.11.06.tar.gz",
        "size": 384826,
        "sha256": "8af0ae5ceed63fa8a2ded611d44cc341027a91df22aaaa071efedc81437412a5",
        "version": "2.11.06",
    },
    "pip": {
        "url": "https://files.pythonhosted.org/packages/ca/1e/d91d7aae44d00cd5001957a1473e4e4b7d1d0f072d1af7c34b5899c9ccdf/pip-20.3.3.tar.gz",
        "size": 1529320,
        "sha256": "79c1ac8a9dccbec8752761cb5a2df833224263ca661477a2a9ed03ddf4e0e3ba",
        "version": "20.3.3",
    },
    "readline": {
        "url": "ftp://ftp.gnu.org/gnu/readline/readline-8.0.tar.gz",
        "size": 2975937,
        "sha256": "e339f51971478d369f8a053a330a190781acb9864cf4c541060f12078948e461",
        "version": "8.0",
        "library_names": ["readline"],
        "licenses": ["GPL-3.0"],
        "license_file": "LICENSE.readline.txt",
    },
    "rust": {
        "url": "https://static.rust-lang.org/dist/rust-1.30.1-x86_64-unknown-linux-gnu.tar.gz",
        "size": 236997689,
        "sha256": "a01a493ed8946fc1c15f63e74fc53299b26ebf705938b4d04a388a746dfdbf9e",
        "version": "1.30.1",
    },
    "setuptools": {
        "url": "https://files.pythonhosted.org/packages/94/23/e9e3d96500c063129a19feb854efbb01e6ffe7d913f1da8176692418ab8e/setuptools-51.1.1.tar.gz",
        "size": 2051053,
        "sha256": "0b43d1e0e0ac1467185581c2ceaf86b5c1a1bc408f8f6407687b0856302d1850",
        "version": "51.1.1",
    },
    "sqlite": {
        "url": "https://www.sqlite.org/2020/sqlite-autoconf-3340000.tar.gz",
        "size": 2930085,
        "sha256": "bf6db7fae37d51754737747aaaf413b4d6b3b5fbacd52bdb2d0d6e5b2edd9aee",
        "version": "3340000",
        "actual_version": "3.34.0.0",
        "library_names": ["sqlite3"],
        "licenses": [],
        "license_file": "LICENSE.sqlite.txt",
        "license_public_domain": True,
    },
    "strawberryperl": {
        "url": "http://strawberryperl.com/download/5.28.1.1/strawberry-perl-5.28.1.1-32bit-portable.zip",
        "size": 143242779,
        "sha256": "8b15c7c9574989568254a7859e473b7d5f68a1145d2e4418036600a81b13805c",
        "version": "5.28.1.1",
    },
    "tcl": {
        "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.10-src.tar.gz",
        "size": 10144235,
        "sha256": "5196dbf6638e3df8d5c87b5815c8c2b758496eb6f0e41446596c9a4e638d87ed",
        "version": "8.6.10",
        "library_names": ["tcl8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tix": {
        "url": "https://github.com/python/cpython-source-deps/archive/tix-8.4.3.6.tar.gz",
        "size": 1836451,
        "sha256": "f7b21d115867a41ae5fd7c635a4c234d3ca25126c3661eb36028c6e25601f85e",
        "version": "8.4.3.6",
        "licenses": ["TCL"],
        "license_file": "LICENSE.tix.txt",
    },
    "tk": {
        "url": "https://prdownloads.sourceforge.net/tcl/tk8.6.10-src.tar.gz",
        "size": 4444764,
        "sha256": "63df418a859d0a463347f95ded5cd88a3dd3aaa1ceecaeee362194bc30f3e386",
        "version": "8.6.10",
        "library_names": ["tk8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tk-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/86027ce3edda1284ae4bf6c2c580288366af4052.tar.gz",
        "size": 7162470,
        "sha256": "34400f7b76a13389a475fc1a4d6e33d5ca21dda6f6ff11b04759865814bdf3d2",
        "version": "6.6.9",
        "git_commit": "86027ce3edda1284ae4bf6c2c580288366af4052",
    },
    "uuid": {
        "url": "https://sourceforge.net/projects/libuuid/files/libuuid-1.0.3.tar.gz",
        "size": 318256,
        "sha256": "46af3275291091009ad7f1b899de3d0cea0252737550e7919d17237997db5644",
        "version": "1.0.3",
        "library_names": ["uuid"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libuuid.txt",
    },
    "x11-util-macros": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/util/util-macros-1.19.2.tar.gz",
        "size": 103001,
        "sha256": "9225c45c3de60faf971979a55a5536f3562baa4b6f02246c23e98ac0c09a75b7",
        "version": "1.19.2",
    },
    "xcb-proto": {
        "url": "https://xcb.freedesktop.org/dist/xcb-proto-1.13.tar.gz",
        "size": 191771,
        "sha256": "0698e8f596e4c0dbad71d3dc754d95eb0edbb42df5464e0f782621216fa33ba7",
        "version": "1.13",
    },
    "xextproto": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/proto/xextproto-7.3.0.tar.gz",
        "size": 290814,
        "sha256": "1b1bcdf91221e78c6c33738667a57bd9aaa63d5953174ad8ed9929296741c9f5",
        "version": "7.3.0",
    },
    "xorgproto": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/proto/xorgproto-2019.1.tar.gz",
        "size": 1119813,
        "sha256": "38ad1d8316515785d53c5162b4b7022918e03c11d72a5bd9df0a176607f42bca",
        "version": "2019.1",
    },
    "xproto": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/proto/xproto-7.0.31.tar.gz",
        "size": 367979,
        "sha256": "6d755eaae27b45c5cc75529a12855fed5de5969b367ed05003944cf901ed43c7",
        "version": "7.0.31",
    },
    "xtrans": {
        "url": "ftp://mirror.csclub.uwaterloo.ca/x.org/pub/current/src/lib/xtrans-1.4.0.tar.gz",
        "size": 225941,
        "sha256": "48ed850ce772fef1b44ca23639b0a57e38884045ed2cbb18ab137ef33ec713f9",
        "version": "1.4.0",
    },
    "xz": {
        "url": "https://tukaani.org/xz/xz-5.2.5.tar.gz",
        "size": 1791345,
        "sha256": "f6f4910fd033078738bd82bfba4f49219d03b17eb0794eb91efbae419f4aba10",
        "version": "5.2.5",
        "library_names": ["lzma"],
        # liblzma is in the public domain. Other parts of code have licenses. But
        # we only use liblzma.
        "licenses": [],
        "license_file": "LICENSE.liblzma.txt",
        "license_public_domain": True,
    },
    "zlib": {
        "url": "https://zlib.net/zlib-1.2.11.tar.gz",
        "size": 607698,
        "sha256": "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1",
        "version": "1.2.11",
        "library_names": ["z"],
        "licenses": ["Zlib"],
        "license_file": "LICENSE.zlib.txt",
    },
}
