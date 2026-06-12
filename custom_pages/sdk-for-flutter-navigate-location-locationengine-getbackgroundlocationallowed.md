---
title: "getBackgroundLocationAllowed method"
slug: "sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getBackgroundLocationAllowed.html -->


<div>
<h1>getBackgroundLocationAllowed method</h1></div>

bool
getBackgroundLocationAllowed()

      <div class="features">override</div>


<p>On iOS devices this checks if application's background location updates are enabled.
Returns true if background location updates are allowed, false otherwise.</p>
<p>On Android devices this is not supported and false is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool getBackgroundLocationAllowed() {
  if (Platform.isIOS) {
    return _location.getBackgroundLocationAllowed();
  }
  return false;
}</code></pre>

 



</div>
`
}</HTMLBlock>
