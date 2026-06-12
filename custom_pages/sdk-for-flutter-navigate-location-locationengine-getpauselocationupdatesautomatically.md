---
title: "getPauseLocationUpdatesAutomatically method"
slug: "sdk-for-flutter-navigate-location-locationengine-getpauselocationupdatesautomatically"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getPauseLocationUpdatesAutomatically.html -->


<div>
<h1>getPauseLocationUpdatesAutomatically method</h1></div>

bool
getPauseLocationUpdatesAutomatically()

      <div class="features">override</div>


<p>On iOS devices this checks if automatic pausing of location updates is enabled.
Returns true if automatic pausing of location updates is enabled, false otherwise.</p>
<p>On Android devices this is not supported and false is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool getPauseLocationUpdatesAutomatically() {
  if (Platform.isIOS) {
    return _location.getPauseLocationUpdatesAutomatically();
  }
  return false;
}</code></pre>

 



</div>
`
}</HTMLBlock>
