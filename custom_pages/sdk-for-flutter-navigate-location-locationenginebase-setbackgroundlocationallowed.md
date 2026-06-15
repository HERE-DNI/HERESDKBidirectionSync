---
title: "setBackgroundLocationAllowed abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationAllowed.html -->


<div>
<h1>setBackgroundLocationAllowed abstract method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setBackgroundLocationAllowed(<ol class="parameter-list single-line"> <li>bool allowed</li>
</ol>)

      

    

<p>Enables or disables background location updates for an application.</p>
<p>Defaults to <code>false</code>.</p>
<ul>
<li><code>allowed</code> Set to <code>true</code> to allow background location updates, or <code>false</code> to disable them.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application
does not have background location capabilities enabled.
<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support controlling of background location modes.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setBackgroundLocationAllowed(bool allowed);</code></pre>

 



</div>
`
}</HTMLBlock>
