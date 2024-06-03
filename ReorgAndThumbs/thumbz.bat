IF %1.==. GOTO No1
IF %2.==. GOTO No2
... do stuff...
GOTO End1

:No1
  ECHO No param 1
GOTO End1
:No2
  ECHO No param 2
GOTO End1

:End1