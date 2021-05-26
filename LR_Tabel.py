non_terminals = [
    'vtype','id','semi','assign','literal','character','boolstr','addsub',
    'multdiv','lparen','rparen','num','lbrace','rbrace','comma',
    'if','while','comp','else','return','class','$'
]
terminals = [
    "CODE'",'CODE','VDECL','ASSIGN','RHS','EXPR','EXPRT','EXPRF''FDECL','ARG','MOREARGS','BLOCK','STMT',
    'COND','CONDL','ELSE','RETURN','CDECL','ODECL'    
]
state_num = 88
temp_dict = {}
for key in non_terminals + terminals:
    temp_dict[key] = None

LR_tabel = [temp_dict.copy() for _ in range(state_num)]
LR_tabel[0]['vtype'] = 's5';LR_tabel[0]['class'] = 's6';LR_tabel[0]['$'] = 'r4';LR_tabel[0]['CODE'] = '1';LR_tabel[0]['VDECL'] = '2';LR_tabel[0]['FDECL'] = '3';LR_tabel[0]['CDECL'] = '4'
LR_tabel[1]['$'] = 'acc'
LR_tabel[2]['vtype'] = 's5';LR_tabel[2]['class'] = 's6';LR_tabel[2]['$'] = 'r4';LR_tabel[2]['CODE'] = '7';LR_tabel[2]['VDECL'] = '2';LR_tabel[2]['FDECL'] = '3';LR_tabel[2]['CDECL'] = '4'
LR_tabel[3]['vtype'] = 's5';LR_tabel[3]['class'] = 's6';LR_tabel[3]['$'] = 'r4';LR_tabel[3]['CODE'] = '8';LR_tabel[3]['VDECL'] = '2';LR_tabel[3]['FDECL'] = '3';LR_tabel[3]['CDECL'] = '4'
LR_tabel[4]['vtype'] = 's5';LR_tabel[4]['class'] = 's6';LR_tabel[4]['$'] = 'r4';LR_tabel[4]['CODE'] = '9';LR_tabel[4]['VDECL'] = '2';LR_tabel[4]['FDECL'] = '3';LR_tabel[4]['CDECL'] = '4'
LR_tabel[5]['id'] = 's10';LR_tabel[5]['ASSIGN'] = '11'
LR_tabel[6]['id'] = 's12'
LR_tabel[7]['$'] = 'r1';LR_tabel[8]['$'] = 'r2';LR_tabel[9]['$'] = 'r3'
LR_tabel[10]['semi'] = 's13';LR_tabel[10]['assign'] = 's15';LR_tabel[10]['lparen'] = 's14'
LR_tabel[11]['semi'] = 's16'
LR_tabel[12]['lbrace'] = 's17'
LR_tabel[13]['vtype'] = 'r5';LR_tabel[13]['id'] = 'r5';LR_tabel[13]['rbrace'] = 'r5';LR_tabel[13]['if'] = 'r5';LR_tabel[13]['while'] = 'r5';LR_tabel[13]['return'] = 'r5';LR_tabel[13]['return'] = 'r5';LR_tabel[13]['class'] = 'r5'
LR_tabel[14]['vtype'] = 's19';LR_tabel[14]['rparen'] = 'r21';LR_tabel[14]['ARG'] = '18'
LR_tabel[15]['id'] = 's28';LR_tabel[15]['literal'] = 's22';LR_tabel[15]['character'] = 's23';LR_tabel[15]['boolstr'] = 's24';LR_tabel[15]['lparen'] = 's27';LR_tabel[15]['num'] = 's29';LR_tabel[15]['RHS'] = '20';LR_tabel[15]['EXPR'] = '21';LR_tabel[15]['EXPRT'] = '25';LR_tabel[15]['EXPRF'] = '26'
LR_tabel[16]['vtype'] = 'r6';LR_tabel[16]['id'] = 'r6';LR_tabel[16]['rbrace'] = 'r6';LR_tabel[16]['if'] = 'r6';LR_tabel[16]['while'] = 'r6';LR_tabel[16]['return'] = 'r6';LR_tabel[16]['class'] = 'r6';LR_tabel[16]['$'] = 'r6'
LR_tabel[17]['vtype'] = 's5';LR_tabel[17]['rbrace'] = 'r39';LR_tabel[17]['VDECL'] = '31';LR_tabel[17]['FDECL'] = '32';LR_tabel[17]['ODECL'] = '30'
LR_tabel[18]['rparen'] = 's33';LR_tabel[19]['id'] = 's34'
LR_tabel[20]['semi'] = 'r7';LR_tabel[21]['semi'] = 'r8';LR_tabel[22]['semi'] = 'r9';LR_tabel[23]['semi'] = 'r10';LR_tabel[24]['semi'] = 'r11'
LR_tabel[25]['semi'] = 'r13';LR_tabel[25]['addsub'] = 's35';LR_tabel[25]['rparen'] = 'r13'
LR_tabel[26]['semi'] = 'r15';LR_tabel[26]['addsub'] = 'r15';LR_tabel[26]['multdiv'] = 's36';LR_tabel[26]['rparen'] = 'r15'
LR_tabel[27]['id'] = 's28';LR_tabel[27]['lparen'] = 's27';LR_tabel[27]['num'] = 's29';LR_tabel[27]['EXPR'] = '37';LR_tabel[27]['EXPRT'] = '25';LR_tabel[27]['EXPRF'] = '26'
LR_tabel[28]['semi'] = 'r17';LR_tabel[28]['addsub'] = 'r17';LR_tabel[28]['multdiv'] = 'r17';LR_tabel[28]['rparen'] = 'r17'
LR_tabel[29]['semi'] = 'r18';LR_tabel[29]['addsub'] = 'r18';LR_tabel[29]['multdiv'] = 'r18';LR_tabel[29]['rparen'] = 'r18'
LR_tabel[30]['rbrace'] = 's38'
LR_tabel[31]['vtype'] = 's5';LR_tabel[31]['rbrace'] = 'r39';LR_tabel[31]['VDECL'] = '31';LR_tabel[31]['FDECL'] = '32';LR_tabel[31]['ODECL'] = '39'
LR_tabel[32]['vtype'] = 's5';LR_tabel[32]['rbrace'] = 'r39';LR_tabel[32]['VDECL'] = '31';LR_tabel[32]['FDECL'] = '32';LR_tabel[32]['ODECL'] = '40'
LR_tabel[33]['lbrace'] = 's41'
LR_tabel[34]['rparen'] = 'r23';LR_tabel[34]['comma'] = 's43';LR_tabel[34]['MOREARGS'] = '42'
LR_tabel[35]['id'] = 's28';LR_tabel[35]['lparen'] = 's27';LR_tabel[35]['num'] = 's29';LR_tabel[35]['EXPR'] = '44';LR_tabel[35]['EXPRT'] = '25';LR_tabel[35]['EXPRF'] = '26'
LR_tabel[36]['id'] = 's28';LR_tabel[36]['lparen'] = 's27';LR_tabel[36]['num'] = 's29';LR_tabel[36]['EXPRT'] = '45';LR_tabel[36]['EXPRF'] = '26'
LR_tabel[37]['rparen'] = 's46'
LR_tabel[38]['vtype'] = 'r36';LR_tabel[38]['class'] = 'r36';LR_tabel[38]['$'] = 'r36'
LR_tabel[39]['rbrace'] = 'r37'
LR_tabel[40]['rbrace'] = 'r38'
LR_tabel[41]['vtype'] = 's53';LR_tabel[41]['id'] = 's54';LR_tabel[41]['rbrace'] = 'r25';LR_tabel[41]['if'] = 's51';LR_tabel[41]['while'] = 's52';LR_tabel[41]['return'] = 'r25';LR_tabel[41]['VDECL'] = '49';LR_tabel[41]['ASSIGN'] = '50';LR_tabel[41]['BLOCK'] = '47';LR_tabel[41]['STMT'] = '48'
LR_tabel[42]['rparen'] = 'r20'
LR_tabel[43]['vtype'] = 's55'
LR_tabel[44]['semi'] = 'r12';LR_tabel[44]['rparen'] = 'r12'
LR_tabel[45]['semi'] = 'r14';LR_tabel[45]['addsub'] = 'r14';LR_tabel[45]['rparen'] = 'r14'
LR_tabel[46]['semi'] = 'r16';LR_tabel[46]['addsub'] = 'r16';LR_tabel[46]['multdiv'] = 'r16';LR_tabel[46]['rparen'] = 'r16';
LR_tabel[47]['return'] = 's57';LR_tabel[47]['RETURN'] = '56';
LR_tabel[48]['vtype'] = 's53';LR_tabel[48]['id'] = 's54';LR_tabel[48]['rbrace'] = 'r25';LR_tabel[48]['if'] = 's51';LR_tabel[48]['while'] = 's52';LR_tabel[48]['return'] = 'r25';LR_tabel[48]['VDECL'] = '49';LR_tabel[48]['ASSIGN'] = '50';LR_tabel[48]['BLOCK'] = '58';LR_tabel[48]['STMT'] = '48';
LR_tabel[49]['vtype'] = 'r26';LR_tabel[49]['id'] = 'r26';LR_tabel[49]['rbrace'] = 'r26';LR_tabel[49]['if'] = 'r26';LR_tabel[49]['while'] = 'r26';LR_tabel[49]['return'] = 'r26'
LR_tabel[50]['semi'] = 's59'
LR_tabel[51]['lparen'] = 's60'
LR_tabel[52]['lparen'] = 's61'
LR_tabel[53]['id'] = 's62';LR_tabel[53]['ASSIGN'] = '11'
LR_tabel[54]['assign'] = 's15'
LR_tabel[55]['id'] = 's63'
LR_tabel[56]['rbrace'] = 's64'
LR_tabel[57]['id'] = 's28';LR_tabel[57]['literal'] = 's22';LR_tabel[57]['character'] = 's23';LR_tabel[57]['boolstr'] = 's24';LR_tabel[57]['lparen'] = 's27';LR_tabel[57]['num'] = 's29';LR_tabel[57]['RHS'] = '65';LR_tabel[57]['EXPR'] = '21';LR_tabel[57]['EXPRT'] = '25';LR_tabel[57]['EXPRF'] = '26'
LR_tabel[58]['rbrace'] = 'r24';LR_tabel[58]['return'] = 'r24'
LR_tabel[59]['vtype'] = 'r27';LR_tabel[59]['id'] = 'r27';LR_tabel[59]['rbrace'] = 'r27';LR_tabel[59]['if'] = 'r27';LR_tabel[59]['while'] = 'r27';LR_tabel[59]['return'] = 'r27'
LR_tabel[60]['boolstr'] = 's68';LR_tabel[60]['COND'] = '66';LR_tabel[60]['CONDL'] = '67'
LR_tabel[61]['boolstr'] = 's68';LR_tabel[61]['COND'] = '69';LR_tabel[61]['CONDL'] = '67'
LR_tabel[62]['semi'] = 's13';LR_tabel[62]['assign'] = 's15';LR_tabel[62]['semi'] = 's13'
LR_tabel[63]['rparen'] = 'r23';LR_tabel[63]['comma'] = 's43';LR_tabel[63]['MOREARGS'] = '70'
LR_tabel[64]['vtype'] = 'r19';LR_tabel[64]['rbrace'] = 'r19';LR_tabel[64]['class'] = 'r19';LR_tabel[64]['$'] = 'r19'
LR_tabel[65]['semi'] = 's71'
LR_tabel[66]['rparen'] = 's72'
LR_tabel[67]['rparen'] = 'r31';LR_tabel[67]['comp'] = 's73'
LR_tabel[68]['rparen'] = 'r32';LR_tabel[68]['comp'] = 'r32'
LR_tabel[69]['rparen'] = 's74'
LR_tabel[70]['rparen'] = 'r22'
LR_tabel[71]['rbrace'] = 'r35'
LR_tabel[72]['lbrace'] = 's75'
LR_tabel[73]['boolstr'] = 's68';LR_tabel[73]['COND'] = '76';LR_tabel[73]['CONDL'] = '67'
LR_tabel[74]['lbrace'] = 's77'
LR_tabel[75]['vtype'] = 's53';LR_tabel[75]['id'] = 's54';LR_tabel[75]['rbrace'] = 'r25';LR_tabel[75]['if'] = 's51';LR_tabel[75]['while'] = 's52';LR_tabel[75]['return'] = 'r25';LR_tabel[75]['VDECL'] = '49';LR_tabel[75]['ASSIGN'] = '50';LR_tabel[75]['BLOCK'] = '78';LR_tabel[75]['STMT'] = '48'
LR_tabel[76]['rparen'] = 'r30'
LR_tabel[77]['vtype'] = 's53';LR_tabel[77]['id'] = 's54';LR_tabel[77]['rbrace'] = 'r25';LR_tabel[77]['if'] = 's51';LR_tabel[77]['while'] = 's52';LR_tabel[77]['return'] = 'r25';LR_tabel[77]['VDECL'] = '49';LR_tabel[77]['ASSIGN'] = '50';LR_tabel[77]['BLOCK'] = '79';LR_tabel[77]['STMT'] = '48'
LR_tabel[78]['rbrace'] = 's80';LR_tabel[79]['rbrace'] = 's81'
LR_tabel[80]['vtype'] = 'r34';LR_tabel[80]['id'] = 'r34';LR_tabel[80]['rbrace'] = 'r34';LR_tabel[80]['if'] = 'r34';LR_tabel[80]['while'] = 'r34';LR_tabel[80]['else'] = 's83';LR_tabel[80]['return'] = 'r34';LR_tabel[80]['ELSE'] = '82'
LR_tabel[81]['vtype'] = 'r34';LR_tabel[81]['id'] = 'r34';LR_tabel[81]['rbrace'] = 'r34';LR_tabel[81]['if'] = 'r34';LR_tabel[81]['while'] = 'r34';LR_tabel[81]['else'] = 's83';LR_tabel[81]['return'] = 'r34';LR_tabel[81]['ELSE'] = '84'
LR_tabel[82]['vtype'] = 'r28';LR_tabel[82]['id'] = 'r28';LR_tabel[82]['rbrace'] = 'r28';LR_tabel[82]['if'] = 'r28';LR_tabel[82]['while'] = 'r28';LR_tabel[82]['return'] = 'r28'
LR_tabel[83]['lbrace'] = 's85'
LR_tabel[84]['vtype'] = 'r29';LR_tabel[84]['id'] = 'r29';LR_tabel[84]['rbrace'] = 'r29';LR_tabel[84]['if'] = 'r29';LR_tabel[84]['while'] = 'r29';LR_tabel[84]['return'] = 'r29'
LR_tabel[85]['vtype'] = 's53';LR_tabel[85]['id'] = 's54';LR_tabel[85]['rbrace'] = 'r25';LR_tabel[85]['if'] = 'r51';LR_tabel[85]['while'] = 'r52';LR_tabel[85]['return'] = 'r25';LR_tabel[85]['VDECL'] = '49';LR_tabel[85]['ASSIGN'] = '50';LR_tabel[85]['BLOCK'] = '86';LR_tabel[85]['STMT'] = '48'
LR_tabel[86]['rbrace'] = 's87'
LR_tabel[87]['vtype'] = 'r33';LR_tabel[87]['id'] = 'r33';LR_tabel[87]['rbrace'] = 'r33';LR_tabel[87]['if'] = 'r33';LR_tabel[87]['while'] = 'r33';LR_tabel[87]['return'] = 'r33'

def LR_Tabel_fn():
    return LR_tabel