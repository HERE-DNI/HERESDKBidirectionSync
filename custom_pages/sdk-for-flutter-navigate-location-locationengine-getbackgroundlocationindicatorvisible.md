---
title: "getBackgroundLocationIndicatorVisible method"
slug: "sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationindicatorvisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getBackgroundLocationIndicatorVisible.html -->


<div>
<h1>getBackgroundLocationIndicatorVisible method</h1></div>

bool
getBackgroundLocationIndicatorVisible()

      <div class="features">override</div>


<p>On iOS devices this checks if application's background location indicator is visible.
Returns true if background location indicator is visible, false otherwise.</p>
<p>On Android devices this is not supported and false is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool getBackgroundLocationIndicatorVisible() {
  if (Platform.isIOS) {
    return _location.getBackgroundLocationIndicatorVisible();
  }
  return false;
}</code></pre>

 



</div>
`
}</HTMLBlock>
