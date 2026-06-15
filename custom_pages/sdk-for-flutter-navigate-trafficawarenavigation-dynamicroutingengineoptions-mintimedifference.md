---
title: "minTimeDifference property"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- minTimeDifference.html -->


<div>
<h1>minTimeDifference property</h1></div>

        
        Duration?
        minTimeDifference
<div class="features">getter/setter pair</div>


<p>The minimum time difference, before notifying the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a>.
To get notified, the following check must be true:
oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival &gt; <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference">DynamicRoutingEngineOptions.minTimeDifference</a>.
A value of 0 will be treated as <code>null</code> meaning no event will be sent.
In order to receive events the difference needs to be greater than 0.
Defaults to <code>null</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Duration? minTimeDifference;</code></pre>

 



</div>
`
}</HTMLBlock>
