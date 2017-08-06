# depth of understanding

# Song Fingerprinting

————————————————

*Sound*

Sound - 

Vibration(regions of pressure) of  that propagates through a medium(compression and 
refraction(speed = 343 meters^2 in 68 degrees F in dry air))

Amplitude - sound pressure or intensity

Frequency - times repeated(measured in hertz)
	
  Travels in waves measured in decibels

Sound Perception - 

  Pitch - low/high

	Duration - short/long

	Loudness - loud/soft

	Timbre - quality of sound

Speakers - 

Take in 	energy and converts into a corresponding sound

	Inverse of speakers is in the ear - perceiving the sound

Microphone -
	Converts sound to an electrical ignal (basically the opposite of a speaker)

Digital Audio -

	Record/store and reproduce sound using audio signals that have been encoded in digital form

Common Sampling Rate is  44.1 kHz to 96 kHz (usually double of what you want)

Equation of any wave propagating to the right

P(x,T) = A*Sin*(kx - wT)

Pressure = P

Space = x

Time = T

Amplitude = A

kx = radial distance



In a microphone - air pressure moves diaphragm with magnets —> electrical field —> current = 
pressure waves —> voltage waves(which is the analog signal)



Encoding - going from analog to  digital signal

Decoding - going from digital to analog signal

CHECK!!!!!!! Used 16-bit encoding(one bit goes to the max(+) or min(-)

Analog Signal - described by a combination of sine waves of different frequencies with loss of information

Digitization - digital recording of an analog signal by the computer

————————————————

*Discrete Fourier Transform*

DFT - converts a finite sequence of equally spaced samples of a function into an equivalent 
length sequence of equally spaced samples

Better Definition - Takes a function on a continuous interval and breaks it down into a infinite 
sum of sinusoids 

tn = n/N+T > C(k) = E(N -1, n=0) Yn*e^-i*2pi*kn/N

Point is to store the song from a magnitude vs time graph and to make into a magnitude vs 
frequency graph.

Peak finding - 

Find the highest peaks of a song at any given time, so when the song is played into the 
microphone, the song with the most matches with the songs in the database will be returned,

————————————————

*Peak Finding*

In order to be a peak it has to be greater than or greater than or equal to the things next to it

1D - finds greatest number in its surroundings

2D - finds and compared to 4 neighbors if its greater than or greater than or equal to its 4 
neighbors

——————————————————————————————————————————

#Facial Recognition 

Use deep learning with neural networks

My grad

Basic indexing - doesn't create a copy but a view

Advanced indexing - creates a cop(array of ints and boolean array)

Machine Learning - ex box office sales based on linear data
	Y = f(X; Abais, Aprod, Abook, Aprom)

	x = movie data = vector

	Y = data set of true earnings 

	dot product multiples x terms by A terms and add them(find value of A and take 
the for product of A and finds the correct Y

	Forward pass F(X;A) = X f then use grad descent to lessen loss func(L = 1/N 
E(i=1,N) Yi - Y^)**2) ( to refine A vals)

		grad of L =  [dL/ dAbias, dL/dAproduction, dL/dAbook, dL/DaPromtion]

MyGrad

	X= Tensor([1,2,3])

		X.data = np.array([1,2,3])

		X.constant = False

		X.scalar_only = False

	X=Tensor([X0,X1,X2)

	F = 3X = Tensor([3*X0, 3*X1…])


	perform F.backward (don’t need functionality of tensor only the gradient



Linear Classifier:
	Given pts(x0,y0) predict what tendril they will be in which tendral

	Take dot product of W and X -> for each point in X array, multiply by 	
weights, the W where the tendrill is should be the greatest value -> change Ws to make 
it so -> Wx0 is the average point in tendrill 0



	X*W = [[W0*X0 + W0*Y0,    W1*X0 + W1*X0,    W2*X0 + W2*Y0],

            [W0*X1 + W0*Y1,    W1*X1 + W1*X1,    W2*X1 + W2*Y1],

            [W0*X2 + W0*Y2,    W1*X2 + W1*X2,    W2*X2 + W2*Y2],


            [W0*X3 + W0*Y3,    W1*X3 + W1*X3,    W2*X3 + W2*Y3],

            ...]


	Add bias


	X*W + B

	         = [[W0*X0 + W0*Y0 + b0,    W1*X0 + W1*X0 + b1,    W2*X0 + W2*Y0 + b2],

            [W0*X1 + W0*Y1 + b0,    W1*X1 + W1*X1 + b1,    W2*X1 + W2*Y1 + b2],

            [W0*X2 + W0*Y2 + b0,    W1*X2 + W1*X2 + b1,    W2*X2 + W2*Y2 + b2],

            [W0*X3 + W0*Y3 + b0,    W1*X3 + W1*X3 + b1,    W2*X3 + W2*Y3 + b2],

            ...]


	W = W - W.grad*StepSize

	b = b - b.grad

	Training Data:

	Y = [1,0,0] or [0,1,0] or [0,0,1] -> depends on which tendral

	X = [x,y] -> coords of point


——————————————————————————————————————————

#News Buddy

Natural language processing

	P(W1,W2,Wt) where w is words

	ngram model: predict next words gives words before it(P(Wi | W1,W1...Wi-1)

	Or: given 2 words predict the next: P(Wi | Wi-2, Wi-1)

Analyzing sentences

	Take a sentences —> tokenize then(separate them), filter, normalize then numerically 
encode them

Bag of Words

	word order doesn't matter even if important to the sentences (only instances matter)

Info retrieving 

	get original ID

	term vector for vector, then doc freq for each doc
