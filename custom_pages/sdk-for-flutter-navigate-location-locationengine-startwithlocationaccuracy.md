---
title: "startWithLocationAccuracy method"
slug: "sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationAccuracy.html -->


<div>
<h1>startWithLocationAccuracy method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
startWithLocationAccuracy(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> locationAccuracy</li>
</ol>)

      <div class="features">override</div>


<p>Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>.
Make sure to call either <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">LocationEngine.confirmHEREPrivacyNoticeInclusion</a> or
<a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">LocationEngine.confirmHEREPrivacyNoticeException</a> beforehand.
Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a> if <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">LocationEngine.startWithLocationAccuracy</a> or
<a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">LocationEngine.startWithLocationOptions</a> is called again without calling <a href="sdk-for-flutter-navigate-location-locationengine-stop">LocationEngine.stop</a> in between.
See <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> for other possible return values.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus startWithLocationAccuracy(LocationAccuracy locationAccuracy) =&gt;
    _location.startWithLocationAccuracy(locationAccuracy);</code></pre>

 



</div>
`
}</HTMLBlock>
