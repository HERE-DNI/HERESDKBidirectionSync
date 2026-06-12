---
title: "startWithLocationOptions method"
slug: "sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationOptions.html -->


<div>
<h1>startWithLocationOptions method</h1></div>

<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
startWithLocationOptions(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> locationOptions</li>
</ol>)

      <div class="features">override</div>


<p>On Android devices starts the location engine with desired <a href="/sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.
Make sure to call either <a href="/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">LocationEngine.confirmHEREPrivacyNoticeInclusion</a> or
<a href="/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">LocationEngine.confirmHEREPrivacyNoticeException</a> beforehand.
Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a> if <a href="/sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">LocationEngine.startWithLocationAccuracy</a> or
<a href="/sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">LocationEngine.startWithLocationOptions</a> is called again without calling <a href="/sdk-for-flutter-navigate-location-locationengine-stop">LocationEngine.stop</a> in between.
See <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> for other possible return values.</p>
<p>On iOS devices this is not supported and <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus startWithLocationOptions(LocationOptions locationOptions) =&gt;
    _location.startWithLocationOptions(locationOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
