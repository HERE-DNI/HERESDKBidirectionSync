---
title: "removeLocationStatusListener method"
slug: "sdk-for-flutter-navigate-location-locationengine-removelocationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removeLocationStatusListener.html -->


<div>
<h1>removeLocationStatusListener method</h1></div>

void
removeLocationStatusListener(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> listener</li>
</ol>)

      <div class="features">override</div>


<p>Removes a <a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> from the engine.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void removeLocationStatusListener(LocationStatusListener listener) {
  LocationStatusListenerBridge? bridge = _locationStatusListeners.remove(listener);
  if (bridge == null) {
    return;
  }
  _location.removeLocationStatusListener(bridge);
}</code></pre>

 



</div>
`
}</HTMLBlock>
