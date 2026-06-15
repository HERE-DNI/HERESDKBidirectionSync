---
title: "startWithLocationAccuracy abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-startwithlocationaccuracy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationAccuracy.html -->


<div>
<h1>startWithLocationAccuracy abstract method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
startWithLocationAccuracy(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> locationAccuracy</li>
</ol>)

      

    

<p>Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>.</p>
<p>Returns
<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a>, if <a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> is called again without <a href="sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> in between.
Make sure to call either <a href="sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion">LocationEngineBase.confirmHEREPrivacyNoticeInclusion</a> or <a href="sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception">LocationEngineBase.confirmHEREPrivacyNoticeException</a> beforehand.</p>
<ul>
<li><code>locationAccuracy</code> Desired location accuracy. Requested accuracy is not guaranteed.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus startWithLocationAccuracy(LocationAccuracy locationAccuracy);</code></pre>

 



</div>
`
}</HTMLBlock>
