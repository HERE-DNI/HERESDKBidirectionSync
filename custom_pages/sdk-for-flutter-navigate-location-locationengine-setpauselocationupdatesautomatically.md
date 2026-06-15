---
title: "setPauseLocationUpdatesAutomatically method"
slug: "sdk-for-flutter-navigate-location-locationengine-setpauselocationupdatesautomatically"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPauseLocationUpdatesAutomatically.html -->


<div>
<h1>setPauseLocationUpdatesAutomatically method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setPauseLocationUpdatesAutomatically(<ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      <div class="features">override</div>


<p>On iOS devices this controls automatic pausing of location updates e.g.
for improving device's battery life at times when
location data is unlikely to change.
By default automatic pausing of location updates is allowed.
Set <code>allowed</code> to true to allow automatic pausing of location updates, or false to disable them.
When calling this method then <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> is returned.</p>
<p>On Android devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setPauseLocationUpdatesAutomatically(bool allowed) {
  if (Platform.isIOS) {
    return _location.setPauseLocationUpdatesAutomatically(allowed);
  }
  return LocationEngineStatus.notSupported;
}</code></pre>

 



</div>
`
}</HTMLBlock>
