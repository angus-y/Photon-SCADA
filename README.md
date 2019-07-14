<p align="center">
  <img src="https://user-images.githubusercontent.com/32593795/61183173-3d822c80-a670-11e9-8155-c0ab0703f866.png" height="200" width="200"/>
</p>

# The Photon Project
A miniauture questionably coded proof of concept smart grid built with a web SCADA system using python 3 and flask for dynamically storing 
solar energy when voltage output drops below a certain threshold. Built for 2019's CXA hackathon competition.

# Infrastructure
A voltmeter monitors the output of a solar panel. The data is then streamed to Blynk where it is then pulled using python 3's urllib 
module from a special token url which constantly updates with the latest value being sent to it. The data is then displayed in the SCADA
interface and depending on the setting of manual/auto monitoring or solar/battery relay path the data is sent back over using the blynk
servers to the microcontroller which changes the relay contorlling current path to either a LED (representative of a load) or a battery
(representative of energy storage cell)
