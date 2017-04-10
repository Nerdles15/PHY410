f(x)=7.29887+-0.909723*x
set title 'Gutenberg-Richter Law'
set xlabel 'Magnitude M'
set ylabel 'log_10(N) per bin'
set xrange [0:10]
plot f(x) title '7.29887 - 0.909723 M', 'histogram.dat' with points, 'histogram.dat' with impulses lw 2
