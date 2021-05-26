'''
CODE' -> CODE
CODE -> VDECL CODE
CODE -> FDECL CODE
CODE -> CDECL CODE
CODE -> ''
VDECL->vtype id semi
VDECL -> vtype ASSIGN semi
ASSIGN -> id assign RHS
RHS -> EXPR
RHS -> literal 
RHS -> character 
RHS -> boolstr
EXPR -> EXPRT addsub EXPR
EXPR -> EXPRT
EXPRT -> EXPRF multdiv EXPRT
EXPRT -> EXPRF
EXPRF -> lparen EXPR rparen
EXPRF -> id
EXPRF -> num
FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
ARG -> vtype id MOREARGS
ARG -> ''
MOREARGS -> comma vtype id MOREARGS
MOREARGS -> ''
BLOCK -> STMT BLOCK
BLOCK -> ''
STMT -> VDECL
STMT -> ASSIGN semi
STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
STMT -> while lparen COND rparen lbrace BLOCK rbrace ELSE
COND -> CONDL comp COND
COND -> CONDL
CONDL -> boolstr
ELSE -> else lbrace BLOCK rbrace
ELSE -> ''
RETURN -> return RHS semi
CDECL -> class id lbrace ODECL rbrace
ODECL -> VDECL ODECL
ODECL -> FDECL ODECL
ODECL -> ''
'''
GRAMMER = [0] * 40
GRAMMER[0] = ("CODE'", 'CODE')
GRAMMER[1] = ('CODE','VDECL CODE')
GRAMMER[2] = ('CODE','FDECL CODE')
GRAMMER[3] = ('CODE','CDECL CODE')
GRAMMER[4] = ('CODE', '')
GRAMMER[5] = ('VDECL','vtype id semi')
GRAMMER[6] = ('VDECL','vtype ASSIGN semi')
GRAMMER[7] = ('ASSIGN','id assign RHS')
GRAMMER[8] = ('RHS','EXPR')
GRAMMER[9] = ('RHS','literal')
GRAMMER[10] = ('RHS','character')
GRAMMER[11] = ('RHS','boolstr')
GRAMMER[12] = ('EXPR','EXPRT addsub EXPR')
GRAMMER[13] = ('EXPR','EXPRT')
GRAMMER[14] = ('EXPRT','EXPRF multdiv EXPRT')
GRAMMER[15] = ('EXPRT','EXPRF')
GRAMMER[16] = ('EXPRF','lparen EXPR rparen')
GRAMMER[17] = ('EXPRF','id')
GRAMMER[18] = ('EXPRF','num')
GRAMMER[19] = ('FDECL','vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace')
GRAMMER[20] = ('ARG','vtype id MOREARGS')
GRAMMER[21] = ('ARG','')
GRAMMER[22] = ('MOREARGS','comma vtype id MOREARGS')
GRAMMER[23] = ('MOREARGS','')
GRAMMER[24] = ('BLOCK','STMT BLOCK')
GRAMMER[25] = ('BLOCK','')
GRAMMER[26] = ('STMT','VDECL')
GRAMMER[27] = ('STMT','ASSIGN semi')
GRAMMER[28] = ('STMT','if lparen COND rparen lbrace BLOCK rbrace ELSE')
GRAMMER[29] = ('STMT','while lparen COND rparen lbrace BLOCK rbrace ELSE')
GRAMMER[30] = ('COND','CONDL comp COND')
GRAMMER[31] = ('COND','CONDL')
GRAMMER[32] = ('CONDL','boolstr')
GRAMMER[33] = ('ELSE','else lbrace BLOCK rbrace')
GRAMMER[34] = ('ELSE','')
GRAMMER[35] = ('RETURN','return RHS semi')
GRAMMER[36] = ('CDECL','class id lbrace ODECL rbrace')
GRAMMER[37] = ('ODECL','VDECL ODECL')
GRAMMER[38] = ('ODECL','FDECL ODECL')
GRAMMER[39] = ('ODECL','')

def grammer_fn():
    return GRAMMER


