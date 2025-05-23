# setup.py

from setuptools import setup, find_packages

setup(
    name='miyabi256',
    version='0.1.0', # リリースごとにバージョンを更新します
    author='Your Name or Organization Name', # あなたの名前または組織名
    author_email='eightman124@gmail.com', # あなたのメールアドレス
    description='A Base64-like encoder/decoder using 256 Japanese characters (Hiragana, Katakana, Kanji).',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/miyabi256-python', # GitHubリポジトリのURL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # 適切なライセンスを選択してください
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6', # 必要なPythonのバージョン
)