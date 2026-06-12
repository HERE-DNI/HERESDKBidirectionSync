---
title: "addLocationStatusListener method"
slug: "sdk-for-flutter-navigate-location-locationengine-addlocationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addLocationStatusListener.html -->


<div>
<h1>addLocationStatusListener method</h1></div>

void
addLocationStatusListener(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> listener</li>
</ol>)

      <div class="features">override</div>


<p>Adds a <a href="/sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> to the engine to get notified when there is a an important status change.
Supports more than one listener, instance is added only once.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addLocationStatusListener(LocationStatusListener listener) {
  if (!_locationStatusListeners.containsKey(listener)) {
    _locationStatusListeners[listener] = LocationStatusListenerBridge(listener);
  }
  _location.addLocationStatusListener(_locationStatusListeners[listener]!);
}</code></pre>

 



</div>
`
}</HTMLBlock>
