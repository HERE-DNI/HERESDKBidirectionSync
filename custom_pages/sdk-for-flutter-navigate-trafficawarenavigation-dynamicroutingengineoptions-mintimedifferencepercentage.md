---
title: "minTimeDifferencePercentage property"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifferencepercentage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- minTimeDifferencePercentage.html -->


<div>
<h1>minTimeDifferencePercentage property</h1></div>

        
        double?
        minTimeDifferencePercentage
<div class="features">getter/setter pair</div>


<p>The value is in the range of [0, 1] over the remaining (current position to next waypoint)
To get notified, the following check must be true:
oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival &gt;= newRouteDuration * <code>min_time_difference_percentage</code>.
A value of 0 will be treated as <code>null</code> meaning no event will be sent.
In order to receive events the difference needs to be greater than 0.
Defaults to <code>null</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? minTimeDifferencePercentage;</code></pre>

 



</div>
`
}</HTMLBlock>
