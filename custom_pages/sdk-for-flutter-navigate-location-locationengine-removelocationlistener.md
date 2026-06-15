---
title: "removeLocationListener method"
slug: "sdk-for-flutter-navigate-location-locationengine-removelocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removeLocationListener.html -->


<div>
<h1>removeLocationListener method</h1></div>

void
removeLocationListener(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> listener</li>
</ol>)

      <div class="features">override</div>


<p>Removes a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> from the engine.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void removeLocationListener(LocationListener listener) {
  LocationUpdateListenerBridge? bridge = _locationUpdateListeners.remove(listener);
  if (bridge == null) {
    return;
  }
  _location.removeLocationListener(bridge);
}</code></pre>

 



</div>
`
}</HTMLBlock>
