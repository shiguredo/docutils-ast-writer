##############################
Docutils AST Writer
##############################

About Shiguredo's open source software
==============================================

We will not respond to PRs or issues that have not been discussed on Discord. Also, Discord is only available in Japanese.

Please read https://github.com/shiguredo/oss/blob/master/README.en.md before use.

時雨堂のオープンソースソフトウェアについて
==============================================

利用前に https://github.com/shiguredo/oss をお読みください。

Docutils AST Writer について
============================

このリポジトリは `@jimo1001 <https://github.com/johejo/>`_ の https://github.com/jimo1001/docutils-ast-writer フォークです。

時雨堂がメンテナンスをしています。

インストール
======================

**PyPI には登録を行っていません**

.. code-block:: console

   $ pip install -e git+https://github.com/shiguredo/docutils-ast-writer@shiguredo#egg=docutils-ast-writer


requirements.txt を利用している場合は以下を追記してください。

::

  -e git+https://github.com/shiguredo/docutils-ast-writer@shiguredo#egg=docutils-ast-writer


使い方
======================

.. code-block:: console

   $ rst2ast [options] [<source> [<destination>]]


ライセンス
======================

::

  The MIT License (MIT)

  Copyright (c) 2023-2023 Shiguredo Inc.
  Copyright (c) 2016 jimo1001

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
