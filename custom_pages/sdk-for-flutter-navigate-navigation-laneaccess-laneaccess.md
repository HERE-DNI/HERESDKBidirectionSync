---
title: "LaneAccess constructor"
slug: "sdk-for-flutter-navigate-navigation-laneaccess-laneaccess"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneAccess.html -->


<div>
<h1>LaneAccess constructor</h1></div>

LaneAccess(<ol class="parameter-list"> <li>bool automobiles, </li>
<li>bool buses, </li>
<li>bool taxis, </li>
<li>bool carpools, </li>
<li>bool pedestrians, </li>
<li>bool trucks, </li>
<li>bool throughTraffic, </li>
<li>bool deliveryVehicles, </li>
<li>bool emergencyVehicles, </li>
<li>bool motorcycles, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>automobiles</code> Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.</li>
<li><code>buses</code> Buses that are used for public transportation.</li>
<li><code>taxis</code> Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
along with their driver, to carry passengers to any specified destination.</li>
<li><code>carpools</code> Represents the sharing of car journeys so that more than one person travels in a car, and
prevents the need for others to have to drive to a location themselves.</li>
<li><code>pedestrians</code> Persons traveling on foot, whether walking or running.</li>
<li><code>trucks</code> Large vehicles that range from medium to heavy duty trucks.</li>
<li><code>throughTraffic</code> Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
allowed to access roads that have traffic restrictions.</li>
<li><code>deliveryVehicles</code> Delivery <a href="sdk-for-flutter-navigate-navigation-laneaccess-trucks">LaneAccess.trucks</a> that are permitted to enter the city proper
to unload goods at businesses.</li>
<li><code>emergencyVehicles</code> Any vehicle that is designated and authorized to respond to an emergency in a
life-threatening situation.</li>
<li><code>motorcycles</code> Motorized two-wheeled passenger vehicles. Generally, mopeds are considered
motorcycles.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LaneAccess(this.automobiles, this.buses, this.taxis, this.carpools, this.pedestrians, this.trucks, this.throughTraffic, this.deliveryVehicles, this.emergencyVehicles, this.motorcycles);</code></pre>

 



</div>
`
}</HTMLBlock>
