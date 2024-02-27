# CS361_Microservice
Instructions in running microservice
1. First, the current port number is 4567. You will have to change the port number value to the microservice to match the port number in the UI.
2. Run the microservice.
3. Write the name of an MLB team and it must all be capitalized.
4. The microservice will recieve the input. If the input was valid it will return a tcp message for all the World Series years that team has won. For invalid input the microservice will return an error message.

Instructions how to request data:

1. Within the client_MLB.py, that is suppose to resemble the UI (the image below)

![Screenshot 2024-02-26 at 10 21 46 PM](https://github.com/russ8412/CS361_Microservice/assets/148286128/b8e85224-3c31-4f4f-ba22-81efc5cb5625)


2. In order to request data the function "client.connect((theHostName, portNum))". This establishes the TCP socket connection.
3. The next function "sentInfo = input("Enter MLB Team name (CAPITALIZED): ")" this is how the UI grabs user input and saves that to "sentInfo" variable.
4. Lastly, the function "client.send(sentInfo.encode())", this encodes the user input and sends it to the microservice. 

Instructions how to recieve data:

1. Within the client_MLB.py, that is suppose to resemble the UI (the image below)
   
   ![Screenshot 2024-02-26 at 10 32 34 PM](https://github.com/russ8412/CS361_Microservice/assets/148286128/0000793e-7a1a-41c5-9d3f-471f3f24edf9)

3. The function "charsArrive = client.recv(1024)" , that recieves the response from the microservice and saves it to the variable "charsArrive". It is set to recieve only 1024 bytes per transmission.
4. Lastly, the function "print(charsArrive.decode())" , that will decode the response held in the variable and print it to the terminal. 
