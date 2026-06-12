---
title: "setLastKnownLocationPersistent method"
slug: "sdk-for-flutter-navigate-location-locationengine-setlastknownlocationpersistent"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setLastKnownLocationPersistent.html -->


<div>
<h1>setLastKnownLocationPersistent method</h1></div>

<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setLastKnownLocationPersistent(<ol class="parameter-list single-line"> <li>bool persistent</li>
</ol>)

      <div class="features">override</div>


<p>On Android devices this enables or disables saving of last known location so
that it persists across application sessions.
By default persistent saving across sessions is enabled.
Set <code>persistent</code> to true to enable last known location to persist across application sessions, or false to disable it.
When calling this method then <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> is returned.</p>
<p>On iOS devices this is not supported and the value is stored, by default, across sessions.
When calling this method then <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setLastKnownLocationPersistent(bool persistent)  {
  if (Platform.isAndroid) {
    return _location.setLastKnownLocationPersistent(persistent);
  }
  return LocationEngineStatus.notSupported;
}</code></pre>

 



</div>
`
}</HTMLBlock>
