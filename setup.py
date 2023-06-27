from setuptools import setup, find_packages
 
setup(
    name                = 'urmine',
    version             = '0.0.1',
    description         = 'Terminal Game: MineSweeper',
    author              = 'kimakuma',
    author_email        = 'kimakuma808@gmail.com',
    url                 = 'https://github.com/kimakuma/SIDE-urmine',
    # 배포하는 패키지의 다운로드 url을 적어줍니다.
    download_url        = 'https://github.com/doorBW/pypi_deploy_test/archive/master.zip',
    # 해당 패키지를 사용하기 위해 필요한 패키지를 적어줍니다. ex. install_requires= ['numpy', 'django']
    # 여기에 적어준 패키지는 현재 패키지를 install할때 함께 install됩니다.
    install_requires    =  [],
    # 등록하고자 하는 패키지를 적는 곳입니다.
    # 우리는 find_packages 라이브러리를 이용하기 때문에 아래와 같이 적어줍니다.
    # 만약 제외하고자 하는 파일이 있다면 exclude에 적어줍니다.
    packages            = find_packages(exclude = []),
    # 패키지의 키워드를 적습니다.
    keywords            = ['pypi deploy'],
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
