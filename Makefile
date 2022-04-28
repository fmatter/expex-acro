.PHONY: clean

default:
	rm -f expex-acro.*
	rm -f expex-acro-*
	python3 combine_code.py
	tex expex-acro.ins
	sed -i 's/\^\^e2\^\^80\^\^98/‘/g' expex-acro.sty
	sed -i 's/\^\^e2^^80\^\^99/’/g' expex-acro.sty
	sed -i 's/\^\^e2\^\^80\^\^9c/“/g' expex-acro.sty
	sed -i 's/\^\^e2\^\^80\^\^9d/”/g' expex-acro.sty
	pdflatex expex-acro.dtx
	pdflatex expex-acro.dtx
	cp expex-acro.sty tests
	cp expex-acro.dtx expex-acro
	cp expex-acro.pdf expex-acro
	cp expex-acro.ins expex-acro
	cp README.md expex-acro
	rm -f expex-acro.*
	rm -f expex-acro-*
	zip -r expex-acro.zip expex-acro/

clean:
	rm -f expex-acro.*
	rm -f expex-acro-*

