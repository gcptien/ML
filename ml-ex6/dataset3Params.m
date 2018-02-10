function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
C = [0.01 0.03 0.1 0.3 1 3 10 30]; 
sigma = [0.01 0.03 0.1 0.3 1 3 10 30];
err_min = inf;

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
%fprintf('The final C is %.2f and the final sigma is %.2f', C, sigma)






% =========================================================================

end
