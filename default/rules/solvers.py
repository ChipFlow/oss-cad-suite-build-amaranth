from src.base import SourceLocation, Target

# avy
SourceLocation(
	name = 'avy',
	vcs = 'git',
	location = 'https://bitbucket.org/arieg/extavy',
	revision = 'origin/master',
	license_url = 'https://bitbucket.org/arieg/avy/raw/a9685b8ba660e46fc3325797ef059cbe95adaf10/LICENSE',
)

Target(
	name = 'avy',
	sources = [ 'avy' ],
	patches = [ 'avy.diff' ],
)

# bitwuzla

SourceLocation(
	name = 'symfpu',
	vcs = 'git',
	location = 'https://github.com/martin-cs/symfpu',
	revision = '8fbe139bf0071cbe0758d2f6690a546c69ff0053',
	license_file = 'LICENSE',
	license_build_only = True,
)

Target(
	name = 'symfpu',
	sources = [ 'symfpu' ],
	patches = [ 'symfpu_20201114.patch' ],
	license_build_only = True,
	build_native = True, # header only library
)

SourceLocation(
	name = 'bitwuzla',
	vcs = 'git',
	location = 'https://github.com/bitwuzla/bitwuzla',
	revision = 'origin/main',
	license_file = 'COPYING',
)

Target(
	name = 'bitwuzla',
	sources = [ 'bitwuzla' ],
	dependencies = [ 'lingeling', 'cadical', 'btor2tools', 'symfpu' ],
	patches = [ 'Toolchain-mingw64.cmake' ],
)

# boolector

SourceLocation(
	name = 'lingeling',
	vcs = 'git',
	location = 'https://github.com/arminbiere/lingeling',
	revision = 'origin/master',
	license_file = 'COPYING',
	license_build_only = True,
)

Target(
	name = 'lingeling',
	sources = [ 'lingeling' ],
	patches = [ 'Lingeling_20190110.patch' ],
	license_build_only = True,
)

SourceLocation(
	name = 'cadical',
	vcs = 'git',
	location = 'https://github.com/arminbiere/cadical',
	revision = 'origin/master',
	license_file = 'LICENSE',
	license_build_only = True,
)

Target(
	name = 'cadical',
	sources = [ 'cadical' ],
	patches = [ 'CaDiCaL_20190730.patch' ],
	license_build_only = True,
)

SourceLocation(
	name = 'btor2tools',
	vcs = 'git',
	location = 'https://github.com/Boolector/btor2tools',
	revision = 'origin/master',
	license_file = 'LICENSE.txt',
	license_build_only = True,
)

Target(
	name = 'btor2tools',
	sources = [ 'btor2tools' ],
	license_build_only = True,
)

SourceLocation(
	name = 'boolector',
	vcs = 'git',
	location = 'https://github.com/Boolector/boolector',
	revision = 'origin/master',
	license_file = 'COPYING',
)

Target(
	name = 'boolector',
	sources = [ 'boolector' ],
	dependencies = [ 'lingeling', 'cadical', 'btor2tools' ],
	patches = [ 'Toolchain-mingw64.cmake' ],
)

# pono

SourceLocation(
	name = 'smt-switch',
	vcs = 'git',
	location = 'https://github.com/makaimann/smt-switch',
	revision = 'e64c261faa826beb51f22ff6d5e74f581362ab47',
	license_file = 'LICENSE',
	license_build_only = True,
)

SourceLocation(
	name = 'pono',
	vcs = 'git',
	location = 'https://github.com/upscale-project/pono',
	revision = '8b2a94649f5ea1161260a611de4b49e6f5d92b98',
	license_file = 'LICENSE',
)

SourceLocation(
	name = 'cvc4',
	vcs = 'git',
	location = 'https://github.com/CVC4/CVC4.git',
	revision = '3dda54ba7e6952060766775c56969ab920430a8a',
	license_file = 'COPYING',
	license_build_only = True,
)

SourceLocation(
	name = 'cvc5',
	vcs = 'git',
	location = 'https://github.com/cvc5/cvc5',
	revision = '77d0bec48a745e3c4acd65085f9c59bdfceed6c0',
	license_file = 'COPYING',
	license_build_only = True,
)

Target(
	name = 'bison',
	sources = [ 'smt-switch' ],
	build_native = True,
)

Target(
	name = 'cvc5',
	sources = [ 'cvc5' ],
	patches = [ 'get-antlr-3.4' ],
	license_build_only = True,
)

Target(
	name = 'cvc4',
	sources = [ 'cvc4' ],
	license_build_only = True,
)

Target(
	name = 'smt-switch',
	sources = [ 'smt-switch' ],
	dependencies = [ 'cvc4', 'boolector', 'bison' ],
	patches = [ 'smt-switch-win32.diff' ],
	license_build_only = True,
)

Target(
	name = 'pono',
	sources = [ 'pono' ],
	dependencies = [ 'smt-switch', 'cvc4', 'boolector' ],
)

# suprove

SourceLocation(
	name = 'suprove',
	vcs = 'git',
	location = 'https://github.com/sterin/super-prove-build',
	revision = 'origin/master',
	license_file = 'pywrapper/LICENSE',
)

Target(
	name = 'suprove',
	sources = [ 'suprove' ],
	dependencies = [ 'python2' ],
	resources = [ 'python2' ],
	patches = [ 'suprove.diff' ],
	arch = [ 'linux-x64', 'linux-arm', 'linux-arm64', 'linux-riscv64' ],
)

# yices

SourceLocation(
	name = 'yices',
	vcs = 'git',
	location = 'https://github.com/SRI-CSL/yices2',
	revision = 'origin/master',
	license_file = 'LICENSE.txt',
)

Target(
	name = 'yices',
	sources = [ 'yices' ],
)

# z3

SourceLocation(
	name = 'z3',
	vcs = 'git',
	location = 'https://github.com/Z3Prover/z3',
	revision = 'origin/master',
	license_file = 'LICENSE.txt',
)

Target(
	name = 'z3',
	sources = [ 'z3' ],
)

# aiger

SourceLocation(
	name = 'aiger',
	vcs = 'git',
	location = 'https://github.com/arminbiere/aiger',
	revision = 'origin/master',
	license_file = 'LICENSE',
)

SourceLocation(
	name = 'picosat',
	vcs = 'git',
	location = 'https://github.com/mmicko/picosat',
	revision = 'origin/main',
	license_file = 'LICENSE',
	license_build_only = True,
)

Target(
	name = 'picosat',
	sources = [ 'picosat' ],
	license_build_only = True,
)

Target(
	name = 'aiger',
	sources = [ 'lingeling', 'aiger' ],
	dependencies = [ 'picosat' ],
	arch = [ 'linux-x64', 'linux-arm', 'linux-arm64', 'linux-riscv64', 'darwin-x64', 'darwin-arm64' ],
)
