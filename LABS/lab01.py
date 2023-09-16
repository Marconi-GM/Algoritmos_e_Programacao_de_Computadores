sheila = str(input().strip())
reginaldo = str(input().strip())

if sheila == reginaldo:
	print('empate')

elif sheila == 'tesoura':
	if reginaldo == 'papel' or reginaldo == 'lagarto':
		print('Interestelar')

	else:
		print('Jornada nas Estrelas')

elif sheila == 'papel':
	if reginaldo == 'pedra' or reginaldo == 'spock':
		print('Interestelar')

	else:
		print('Jornada nas Estrelas')

elif sheila == 'pedra':
	if reginaldo == 'lagarto' or reginaldo == 'tesoura':
		print('Interestelar')

	else:
		print('Jornada nas Estrelas')

elif sheila == 'lagarto':
	if reginaldo == 'spock' or reginaldo == 'papel':
		print('Interestelar')

	else:
		print('Jornada nas Estrelas')

elif sheila == 'spock':
	if reginaldo == 'tesoura' or reginaldo == 'pedra':
		print('Interestelar')

	else:
		print('Jornada nas Estrelas')