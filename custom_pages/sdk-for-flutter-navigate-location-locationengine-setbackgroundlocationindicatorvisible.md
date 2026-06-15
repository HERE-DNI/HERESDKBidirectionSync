---
title: "setBackgroundLocationIndicatorVisible method"
slug: "sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationindicatorvisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationIndicatorVisible.html -->


<div>
<h1>setBackgroundLocationIndicatorVisible method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setBackgroundLocationIndicatorVisible(<ol class="parameter-list single-line"> <li>bool visible</li>
</ol>)

      <div class="features">override</div>


<p>On iOS devices this controls visibility of application's background location indicator.
By default background location indicator
is visible, if application has background location capabilities.
Set <code>visible</code> to true to show background location indicator, or false to hide it.
Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application
does not have background location capabilities enabled.</p>
<p>On Android devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setBackgroundLocationIndicatorVisible(bool visible) {
  if (Platform.isIOS) {
    return _location.setBackgroundLocationIndicatorVisible(visible);
  }
  return LocationEngineStatus.notSupported;
}</code></pre>

 



</div>
`
}</HTMLBlock>
