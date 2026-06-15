---
title: "LaneType constructor"
slug: "sdk-for-flutter-navigate-navigation-lanetype-lanetype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneType.html -->


<div>
<h1>LaneType constructor</h1></div>

LaneType(<ol class="parameter-list"> <li>bool isRegular, </li>
<li>bool isHighOccupancyVehicle, </li>
<li>bool isReversible, </li>
<li>bool isExpress, </li>
<li>bool isAcceleration, </li>
<li>bool isDeceleration, </li>
<li>bool isAuxiliary, </li>
<li>bool isSlow, </li>
<li>bool isPassing, </li>
<li>bool isShoulder, </li>
<li>bool isRegulatedAccess, </li>
<li>bool isTurn, </li>
<li>bool isCenterTurn, </li>
<li>bool isTruckParking, </li>
<li>bool isParking, </li>
<li>bool isVariableDriving, </li>
<li>bool isBicycle, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>isRegular</code> Regular lane is a lane that does not have a specific use.</li>
<li><code>isHighOccupancyVehicle</code> A lane which is restricted for high occupancy vehicles.
Note: High occupancy vehicles are vehicles with a driver and one or more passengers.</li>
<li><code>isReversible</code> A lane in which traffic may travel in either direction, depending on certain conditions
such as the time of the day to improve traffic flow during rush hours.</li>
<li><code>isExpress</code> Express lane is a lane or set of lanes usually physically separated from the major roadway
with limited entry and exit points to quickly move traffic in and out of a major metropolitan
city. An express lane can be reversible, bidirectional, or one-way.</li>
<li><code>isAcceleration</code> An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle
increase its speed to where it can safely merge with ongoing traffic. These lanes can be
accessed from ramps, rest areas, or weigh stations.</li>
<li><code>isDeceleration</code> A deceleration lane is the same as an acceleration lane but used for the opposite scenario.</li>
<li><code>isAuxiliary</code> An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance
ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next
interchange.</li>
<li><code>isSlow</code> A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep
uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.</li>
<li><code>isPassing</code> A passing lane is a lane that can occur on steep mountain grades or other roads where
overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass
slow moving vehicles.</li>
<li><code>isShoulder</code> A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is
not generally used for driving, although it is possible under certain circumstances.</li>
<li><code>isRegulatedAccess</code> A regulated lane access is a lane designated as a holding zone, used to regulate traffic
using time intervals. Regulated lane access is only coded for truck holding zones that are
used to regulate truck access into tunnels and over bridges using time intervals (e.g., some
tunnel accesses in Switzerland).</li>
<li><code>isTurn</code> Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing
traffic.</li>
<li><code>isCenterTurn</code> Center turn lane is a bidirectional turn lane located in the middle of a road that allows
traffic in both directions to turn left (right for left side driving countries).</li>
<li><code>isTruckParking</code> Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for
emergency.</li>
<li><code>isParking</code> Parking lanes are portions of the road bed that may be used for parking legally. They may
allow vehicles to use them as driving lanes at times, though.</li>
<li><code>isVariableDriving</code> Variable driving lanes are lanes added to a road that open and close to accommodate traffic
volume and flow using variable indicators.</li>
<li><code>isBicycle</code> Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by
lane markings, signs, buffers or barriers.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LaneType(this.isRegular, this.isHighOccupancyVehicle, this.isReversible, this.isExpress, this.isAcceleration, this.isDeceleration, this.isAuxiliary, this.isSlow, this.isPassing, this.isShoulder, this.isRegulatedAccess, this.isTurn, this.isCenterTurn, this.isTruckParking, this.isParking, this.isVariableDriving, this.isBicycle);</code></pre>

 



</div>
`
}</HTMLBlock>
