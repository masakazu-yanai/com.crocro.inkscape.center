#!/usr/bin/env python
# coding:utf-8

'''
Copyright (C) 2014 Masakazu yanai, yanai@crocro.com
http://crocro.com/

crocro_center.py
「Inkscape」用のエクステンションです。選択したオブジェクトの中心を、
X軸の座標0位置に移動します。

本スクリプトは、「Inkscape」用の基本的なエクステンションを利用しています。
そのため、GPLライセンス下で公開されます。

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex, simpletransform
_ = str

class CroCro_Center(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	def effect(self):
		# 選択要素がなければ終了
		if len(self.selected) <= 0: return

		# 選択要素を取得
		# グループ内のtransformを展開
		# バウンディングボックスの取得
		sel = self.selected
		bbox = simpletransform.computeBBox(sel.values())
		# inkex.debug('>> ' + ' '.join(_(v) for v in sel))

		# X座標の相対移動ドット数の計算
		x = bbox[0]
		y = bbox[2]
		w = bbox[1] - bbox[0]
		h = bbox[3] - bbox[2]
		# inkex.debug('>> ' + ' '.join(_(v) for v in bbox))
		# inkex.debug('>> x' + _(x) + ' y' + _(y) + ' w' + _(w) + ' h' + _(h))

		mvX = - x + - w / 2
		# inkex.debug('>> mvX ' + _(mvX))

		# 変形マトリクスの作成
		transformation = 'translate(' + _(mvX) + ', 0)'
		transform = simpletransform.parseTransform(transformation)

		# 変形マトリクスの適用
		for id, node in sel.iteritems():
			simpletransform.applyTransformToNode(transform, node)

# インスタンスの初期化と実行
if __name__ == '__main__':
	e = CroCro_Center()
	e.affect()

