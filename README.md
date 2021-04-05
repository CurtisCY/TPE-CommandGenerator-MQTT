# TPE-CommandGenerator-MQTT
MOXA ThingsPro Edge Remote API Invocation request command generator

User can interact with IoT gateway by using MQTT to read/write data from gateway remotely with pre-defined format of message.
This utility helps user generate the request command easily with an UI interface with pre-defined arguments.

In order to proceed the demonstration, please make sure you have an eligible device with ThingsPro edge software
and make the device connect to the remote/local MQTT broker. In this tutorial, we won't go through the setup of general
device setting, Modbus TCP/RTU setting and MQTT message setting.

Here comes the testing scenario. We have 1 IoT gateway polling the Field sensoring device by using Modbus TCP and sending data to 
public Hive MQ Broker. My laptop will have MQTT.fx software as client try to retrieve data or control the IoT gateway through the Broker

Key component of this demonstration:
1. Field sensoring device - ioLogik E1212 (Modbus TCP device)
2. UC-3111-T-EU-LX (Moxa ARM-based industrial computer with ThingsPro Edge software inside)
3. Hive MQ Public Broker
4. MQTT.fx MQTT client software
5. ThingsPro Edge Command Generator software

Architecture:  
Remote I/O device--(Wired LAN)--UC-3111-T-EU-LX--(Internet)--HiveMQ Broker--Laptop(With MQTT.fx and ThingsPro Edge Command Generator)

The gateway will subscribe to the topic 'Input topic to Subscribe' and react based on the receiving message. Once receive the message, it
will publish the execution result to the topic 'Out topic to Subscribe'. Therefore, users need to follow the API document to fill in the 
legal message format to let gateway understand the request command.

In my testing scenairo, 'Input topic to subscribe' is '/PLCDemo/requests' and 'Out topic to subscribe' is '/PLCDemo/responses'. We can use
MQTT.fx software to publish the control command to '/PLCDemo/requests' to control gateway and monitor the response by subscribing /PLCDemo/responses

![image](https://user-images.githubusercontent.com/63384830/113556518-3151b600-962f-11eb-8582-22a9706191b8.png)

Let us just use this utility to create a basic request command to get device IP information. 
Once you open the ThingsPro Edge Control command generator, there are several setup you will need to modify
1. Choose the command to invoke action - Please select the required action you would like to retrieve.
2. Command expired time - When will this request command expired to execute.
3. Task id - Task id is used to distiguish the request command sent to the gateway.

![image](https://user-images.githubusercontent.com/63384830/113557459-9fe34380-9630-11eb-9433-6f8c99b985be.png)

After setting up the command expired time and task id, you can click 'Generate' button to get the request command in text box
![image](https://user-images.githubusercontent.com/63384830/113558099-a58d5900-9631-11eb-94d1-6e17ea3d0129.png)

Copy the command and paste it on the MQTT.fx publish page and click 'publish'
![image](https://user-images.githubusercontent.com/63384830/113558265-eab18b00-9631-11eb-89d1-bebc8c879188.png)

After that, you can see the device response on the subscribe page.
![image](https://user-images.githubusercontent.com/63384830/113558347-1765a280-9632-11eb-83ed-45fcf6cce20c.png)

In this software version, we support several commands in the drop down box.

For the Get device IP, Get device general info, Get cellular status, Get DLM status, Get app status, System reboot command,
user only need to setup the command expired time and task id. 

For Get Modbus value and Write modbus value, user need to setup Modbus device name, tag name, tag type and desired value. All
those information has been shown on the ThingsPro Edge Modbus setup page.

For Others, user need to fill in the API endpoint and GET/PUT method with the pre-defined key and value. You might need to contact
with us for further instruction or check our online API document (https://thingspro-edge.moxa.online/v2.1.0/thingspro-agent/index.html)

![image](https://user-images.githubusercontent.com/63384830/113558486-572c8a00-9632-11eb-81d8-bbc6d5275604.png)

Let me show some example here:

Example 1 - Get modbus device data

To Get Modbus device data, you will need to fill in the connected Modbus device name and the required tag name
Select the modbus device types - Modbus TCP or Modbus RTU slave devices
![image](https://user-images.githubusercontent.com/63384830/113559731-7af0cf80-9634-11eb-87c8-7a3e2891e3ba.png)

Copy the message and paste it on the MQTT.fx publish page
![image](https://user-images.githubusercontent.com/63384830/113559895-bab7b700-9634-11eb-89f0-4031833de15c.png)

Monitor the response from the MQTT.fx subscribe page
![image](https://user-images.githubusercontent.com/63384830/113559778-8fcd6300-9634-11eb-9ade-9fe9180c41f0.png)

Example 2 - Write modbus device data

To write modbus device data, except the Modbus device name and required tag name, you will need to fill in the
data type of the tag and the desired value of the tag
![image](https://user-images.githubusercontent.com/63384830/113560399-8690c600-9635-11eb-87f5-f81598315367.png)

Copy the message and paste it on the MQTT.fx publish page
![image](https://user-images.githubusercontent.com/63384830/113560481-a922df00-9635-11eb-82bd-32e9d7422685.png)

Monitor the response from the MQTT.fx subscribe page
![image](https://user-images.githubusercontent.com/63384830/113560541-b93abe80-9635-11eb-8402-bbf43266f4ff.png)

Example 3 - Check online API document and fill in the pre-defined API endpoints and select the GET or PUT method to use.
key and value arguements can be found from the online API documents
![image](https://user-images.githubusercontent.com/63384830/113560821-36feca00-9636-11eb-8816-99db40189ca7.png)

*POST Method will be added soon in next version

Reference: Online API documents - Write modbus tag
![image](https://user-images.githubusercontent.com/63384830/113560964-74fbee00-9636-11eb-8e2e-29a82515b2e0.png)






