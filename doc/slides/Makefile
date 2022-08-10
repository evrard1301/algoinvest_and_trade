all: slides report

slides:
	pdflatex slides.tex
	pdflatex slides.tex

report:
	pdflatex report.tex
	pdflatex report.tex

clean:
	rm -f *.aux *.log *.out *.snm *.toc *.nav *.vrb

mrproper: clean
	rm -f *.pdf
