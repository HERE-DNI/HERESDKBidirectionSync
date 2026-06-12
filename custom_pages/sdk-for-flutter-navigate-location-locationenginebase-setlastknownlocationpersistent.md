---
title: "setLastKnownLocationPersistent abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setlastknownlocationpersistent"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setLastKnownLocationPersistent.html -->


<div>
<h1>setLastKnownLocationPersistent abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setLastKnownLocationPersistent(<ol class="parameter-list single-line"> <li>bool persistent</li>
</ol>)

      

    

<p>Enables or disables saving of last known location so that it persists between application sessions.</p>
<p>Defaults to enabled.</p>
<ul>
<li><code>persistent</code> Set to <code>true</code> to enable last known location to be saved persistently, or <code>false</code> to disable it.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds.
<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support controlling of last known location saving.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setLastKnownLocationPersistent(bool persistent);</code></pre>

 



</div>
`
}</HTMLBlock>
