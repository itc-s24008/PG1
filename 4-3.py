def show_args(*args):
    '''与えられた複数の位置引数をタプルにまとめて受け取りそのタプルを表示して返す'''
    print('Positional arguments:', args)
    return args

show_args(1, 2, 3, 'da!')

def show_kwargs(**kwargs):
    '''与えられた複数のキーワード引数を辞書にまとめて受け取りその辞書を表示して返す'''
    print('Keyword arguments:', kwargs)
    return kwargs

show_kwargs{'pasta': 'ペンネ', 'drin': '赤ワイン', 'main_dish': '肉料理', 'n_customers': 3}

show_args(1, 2, 3, 'da!')

