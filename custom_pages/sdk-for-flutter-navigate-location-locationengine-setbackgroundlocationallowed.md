---
title: "setBackgroundLocationAllowed method"
slug: "sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationAllowed.html -->


<div>
<h1>setBackgroundLocationAllowed method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setBackgroundLocationAllowed(<ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      <div class="features">override</div>


<p>On iOS devices this enables or disables application's background location updates.
By default background location updates
are enabled if application has background location capabilities.
Set <code>allowed</code> to true to allow background location updates, or false to disable them.
Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application
does not have background location capabilities enabled.</p>
<p>On Android devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setBackgroundLocationAllowed(bool allowed) {
  if (Platform.isIOS) {
    return _location.setBackgroundLocationAllowed(allowed);
  }
  return LocationEngineStatus.notSupported;
}</code></pre>

 



</div>
`
}</HTMLBlock>
