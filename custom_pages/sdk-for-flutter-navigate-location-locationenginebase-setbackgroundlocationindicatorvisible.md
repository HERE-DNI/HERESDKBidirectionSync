---
title: "setBackgroundLocationIndicatorVisible abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationindicatorvisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationIndicatorVisible.html -->


<div>
<h1>setBackgroundLocationIndicatorVisible abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
setBackgroundLocationIndicatorVisible(<ol class="parameter-list single-line"> <li>bool visible</li>
</ol>)

      

    

<p>Controls visibility of application's background location indicator.</p>
<p>By default background location indicator
is visible, if application has background location capabilities.</p>
<ul>
<li><code>visible</code> Set to <code>true</code> to show background location indicator, or <code>false</code> to hide it.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application
does not have background location capabilities enabled.
<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support controlling of background location
indicator visibility.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus setBackgroundLocationIndicatorVisible(bool visible);</code></pre>

 



</div>
`
}</HTMLBlock>
