---
title: "setPauseLocationUpdatesAutomatically abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setpauselocationupdatesautomatically"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPauseLocationUpdatesAutomatically.html -->


<div>
<h1>setPauseLocationUpdatesAutomatically abstract method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setPauseLocationUpdatesAutomatically(<ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      

    

<p>Controls automatic pausing of location updates e.g.</p>
<p>for improving device's battery life at times when
location data is unlikely to change. By default automatic pausing of location updates is allowed.</p>
<ul>
<li><code>allowed</code> Set to <code>true</code> to allow automatic pausing of location updates, or <code>false</code> to disable them.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms
which do not support automatic pausing of location updates.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setPauseLocationUpdatesAutomatically(bool allowed);</code></pre>

 



</div>
`
}</HTMLBlock>
