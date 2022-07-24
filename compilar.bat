@REM pyinstaller --onefile --name Robo_API_SMS_%SELECAO% main.py
@REM pyinstaller --onefile --name Cont_API_SMS_%SELECAO% direct.py
@REM pyinstaller --onefile --name gerenc_agenda gerenc_agenda.py
pyinstaller --add-binary="fire.ico;." --onefile --name ex_agenda ex_agenda.py
@REM pyinstaller --add-binary="fire.ico;." --onefile --name ex_contigencia ex_contigencia.py