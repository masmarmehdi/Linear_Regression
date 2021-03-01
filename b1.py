x = [6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4]
y = [8.78, 8.45, 7.98, 8.05, 8.01, 8.00, 7.97, 7.99]
x_bar = 6.7
y_bar = 8.15
nominator = 0
denominator = 0
for i in range(len(x)):
    nominator += (x[i] - x_bar) * (y[i] - y_bar)

for j in range(len(x)):
    denominator += pow((x[j] - x_bar),2)

b1 = nominator/denominator
print("%.3f" %b1)