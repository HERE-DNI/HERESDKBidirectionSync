---
title: "updateLocationAccuracy abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-updatelocationaccuracy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateLocationAccuracy.html -->


<div>
<h1>updateLocationAccuracy abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
updateLocationAccuracy(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> locationAccuracy</li>
</ol>)

      

    

<p>Reconfigures the location engine with desired <a href="/sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>.</p>
<p>This method is a faster way to change location accuracy for already started
location engine, than calling <a href="/sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> and <a href="/sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> in sequence. Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notReady</a>,
if called for unstarted location engine.</p>
<ul>
<li><code>locationAccuracy</code> Desired location accuracy. Requested accuracy is not guaranteed.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="/sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus updateLocationAccuracy(LocationAccuracy locationAccuracy);</code></pre>

 



</div>
`
}</HTMLBlock>
