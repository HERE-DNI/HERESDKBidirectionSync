---
title: "hdEnabled property"
slug: "sdk-for-flutter-navigate-location-satellitepositioningoptions-hdenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- hdEnabled.html -->


<div>
<h1>hdEnabled property</h1></div>

        
        bool
        hdEnabled
<div class="features">getter/setter pair</div>


<p>Controls HD GNSS positioning. If false, HD GNSS positioning is disabled.
VDR (Vehicle Dead Reckoning) is used if HD GNSS is enabled and sensors are used for positioning.
This feature requires Android 12 or later and dual frequency GNSS receiver and raw GNSS measurements.
This feature is disabled by default: <a href="https://www.here.com/platform/positioning">Contact us</a> to enable it.
If it is not enabled or the OS/device requirements are not met, fallback to other positioning technologies may occur and desired accuracy level may not be reached.
Defaults to <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool hdEnabled;</code></pre>

 



</div>
`
}</HTMLBlock>
