---
title: "freeFlowSpeedTable property"
slug: "sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- freeFlowSpeedTable.html -->


<div>
<h1>freeFlowSpeedTable property</h1></div>

        
        Map&lt;int, double&gt;
freeFlowSpeedTable
<div class="features">getter/setter pair</div>


<p>Free flow speed table describes energy consumption when traveling at constant speed.
It defines a function curve specifying consumption rate at a given free flow speed
on a flat stretch of road.
Map keys represent speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
At minimum, one key/value pair must be set. In this case the consumption value is
used for all possible speed keys.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;int, double&gt; freeFlowSpeedTable;</code></pre>

 



</div>
`
}</HTMLBlock>
