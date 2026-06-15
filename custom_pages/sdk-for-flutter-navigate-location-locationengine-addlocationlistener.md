---
title: "addLocationListener method"
slug: "sdk-for-flutter-navigate-location-locationengine-addlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addLocationListener.html -->


<div>
<h1>addLocationListener method</h1></div>

void
addLocationListener(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> listener</li>
</ol>)

      <div class="features">override</div>


<p>Adds a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> to the engine to get notified when there is a new location update available.
Supports more than one listener, instance is added only once.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addLocationListener(LocationListener listener) {
  if (!_locationUpdateListeners.containsKey(listener)) {
    _locationUpdateListeners[listener] = LocationUpdateListenerBridge(listener);
  }
  _location.addLocationListener(_locationUpdateListeners[listener]!);
}</code></pre>

 



</div>
`
}</HTMLBlock>
