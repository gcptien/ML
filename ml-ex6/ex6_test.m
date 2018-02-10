clear ; close all; clc

load('ex6data3.mat');

C = [0.01 0.03 0.1 0.3 1 3 10 30]; 
sigma = [0.01 0.03 0.1 0.3 1 3 10 30];


err_min = inf;
% Try different SVM Parameters here
%[C, sigma] = dataset3Params(X, y, Xval, yval);

% Train the SVM
for i = 1:length(C)
	for j = 1:length(sigma)
		model= svmTrain(X, y, C(i), @(x1, x2) gaussianKernel(x1, x2, sigma(j))); 
		predictions = svmPredict(model, Xval);
		err = mean(double(predictions~=yval));
		if (err <= err_min)
			C_final = C(i);
			sigma_final = sigma(j)
			err_min = err;
			fprintf('New C = %.2f and new sigma = %.2f. The new min error is %f', C_final,sigma_final,err_min)
		end
	end;
end;

C = C_final;
sigma = sigma_final;
fprintf('The final C is %.2f and the final sigma is %.2f', C, sigma)