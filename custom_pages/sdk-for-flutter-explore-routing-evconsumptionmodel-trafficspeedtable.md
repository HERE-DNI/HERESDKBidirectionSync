---
title: "trafficSpeedTable property"
slug: "sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficSpeedTable.html -->


<div>
<h1>trafficSpeedTable property</h1></div>

        
        Map&lt;int, double&gt;
trafficSpeedTable
<div class="features">getter/setter pair</div>


<p>Traffic speed table describes energy consumption when traveling under heavy traffic
conditions, i.e. when the vehicle is expected to often change the travel speed.
It defines a function curve specifying consumption rate at a given speed under traffic
conditions on a flat stretch of road.
Map keys represent traffic speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
If only one key/value pair is set, the consumption value is
used for all possible traffic speed keys.
If <a href="/sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable">EVConsumptionModel.trafficSpeedTable</a> is empty then only
<a href="/sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable">EVConsumptionModel.freeFlowSpeedTable</a> is used for calculating speed-related
energy consumption.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;int, double&gt; trafficSpeedTable;</code></pre>

 



</div>
`
}</HTMLBlock>
