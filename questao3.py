# 3. Na programação é comum relacionar dados usando um campo que identifica
# registros (id). Elabore uma modelagem de dados em que os registros estão
# relacionados através de um campo identificador (o id), atendendo as seguintes
# afirmações:

estados = [{'id': 3, 'estado': 'Goiás'}, {'id': 4, 'estado': 'Paraná'}]

cidades = [{'id': 15, 'cidade': 'Diamantina', 'estado_id': 3},
           {'id': 16, 'cidade': 'Noronha', 'estado_id': 4}]
bairros = [{'id': 22, 'bairro': 'Betânia', 'cidade_id': 15, 'estado_id': 3}, {'id': 23, 'bairro': 'Agostinho',
 'cidade_id': 16, 'estado_id': 4}, {'id': 24, 'bairro': 'Natal', 'cidade_id': 16, 'estado_id': 4}]
