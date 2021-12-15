import sys, platform


collect_ignore = []


if platform.platform() != 'Windows' or 'gcc' in sys.version.lower():
    collect_ignore.extend([
        'distutils/command/bdist_msi.py',
        'distutils/msvc9compiler.py',
    ])
