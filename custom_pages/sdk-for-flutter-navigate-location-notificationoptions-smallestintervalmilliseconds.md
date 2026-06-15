---
title: "smallestIntervalMilliseconds property"
slug: "sdk-for-flutter-navigate-location-notificationoptions-smallestintervalmilliseconds"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- smallestIntervalMilliseconds.html -->


<div>
<h1>smallestIntervalMilliseconds property</h1></div>

        
        int
        smallestIntervalMilliseconds
<div class="features">getter/setter pair</div>


<p>Smallest allowed interval for position updates in milliseconds.  It is
guaranteed that positions are not provided more often than this value.
Smallest interval could be used for throttling position updates, e.g.
when each position update triggers CPU intensive calculations in the
client application. This value is used as a minimum update interval
when requesting GNSS location updates from the operating system.
When hdEnabled is set to <code>true</code> in SatellitePositioningOptions, the
smallest_interval_milliseconds value has a limited range. The SDK will
adjust the value to allow location updates with a frequency of 1Hz to
10Hz (1000 ms to 100 ms, respectively).
Default interval is 900 milliseconds.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int smallestIntervalMilliseconds;</code></pre>

 



</div>
`
}</HTMLBlock>
