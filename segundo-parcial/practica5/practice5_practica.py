'''
Neurona 1
w10    -1.5
w11 =   1
w12     1
'''

'''
Neurona 2
w20    -0.5
w21 =   1
w22     1
'''

'''
Neurona 3
w10    -0.5
w11 =   -2
w12     1
'''

'''
XOR
0 1 | 1
1 0 | 1
1 1 | 0
0 0 | 0
'''

'''
Neurona 1 * Neurona 2
Factor de correccion = b
( 1 0 1 ) => ( b xor 1 )
funcion activacion => 0 = 1 : 0

[ -1.5 1 1 ] [ 1 ] = [ -1.5 + 1 ] = [ -0.5 ]
[ -0.5 1 1 ] [ 0 ]   [ -0.5 + 1 ]   [ 0.5 ]
             [ 1 ]
             
y = [ -0.5] = [ 0 ] => [ -0.5 -2 1] [ 1 ] => [ -0.5 + 1 ] = f(0.5) = 1
    [ 0.5 ]   [ 1 ]                 [ 0 ]
                                    [ 1 ]
'''

# -----------------------------------------------------------------------

'''
Neurona 1 * Neurona 2
Factor de correccion = b
primer 1 te lo da el problema
funcion activacion => 0 = 1 : 0
x0 = 1 

[ -1.5 1 1 ] [ 1 ] = [ -1.5 + 1 + 1 ] = [ 0.5 ]
[ -0.5 1 1 ] [ 1 ]   [ -0.5 + 1 + 1 ]   [ 1.5 ]
             [ 1 ]

y = [ 0.5 ] = [ 1 ] => [-0.5 -2 1] [ 1 ] => [ -0.5 -2 + 1 ] = f(-1.5) = 0
    [ 1.5 ]   [ 1 ]                [ 1 ]
           entrada sig             [ 1 ]
'''