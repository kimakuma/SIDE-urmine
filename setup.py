from setuptools import setup, find_packages
 
setup(
    name                = 'urmine',
    version             = '0.0.1',
    description         = 'Terminal Game: MineSweeper',
    author              = 'kimakuma',
    author_email        = 'kimakuma808@gmail.com',
    url                 = 'https://github.com/kimakuma/SIDE-urmine',
    download_url        = 'https://github.com/kimakuma/SIDE-urmine/archive/main.zip',
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적어줍니다. ex. install_requires= ['numpy', 'django']
    install_requires    =  [],
    # 등록하고자 하는 패키지를 적는 곳입니다. 제외할 것은 exclude에 적습니다.
    packages            = find_packages(exclude = []),
    # 패키지의 키워드를 적습니다.
    keywords            = ['urmine'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
