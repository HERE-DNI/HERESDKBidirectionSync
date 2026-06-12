---
title: "startWithLocationOptions abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationOptions.html -->


<div>
<h1>startWithLocationOptions abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
startWithLocationOptions(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> locationOptions</li>
</ol>)

      

    

<p>Starts the location engine with desired <a href="/sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.</p>
<p>Returns
<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a>, if <a href="/sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> is called again without <a href="/sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> in between.
Make sure to call either <a href="/sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion">LocationEngineBase.confirmHEREPrivacyNoticeInclusion</a> or <a href="/sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception">LocationEngineBase.confirmHEREPrivacyNoticeException</a> beforehand.
This method variant is not currently supported on iOS platforms. Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which this method variant is not supported.</p>
<ul>
<li><code>locationOptions</code> Desired location options.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus startWithLocationOptions(LocationOptions locationOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
