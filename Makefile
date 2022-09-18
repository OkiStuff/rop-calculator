PIP:=py -m pip
PYINSTALLER:=pyinstaller
SCRIPTFILE:=main.py

all:
	$(PIP) install -U pyinstaller
	${PYINSTALLER} -c -F $(SCRIPTFILE) 

clean:
	rm -rf ./build/
	rm *.spec

fullclean:
	rm -rf ./dist/
	make clean