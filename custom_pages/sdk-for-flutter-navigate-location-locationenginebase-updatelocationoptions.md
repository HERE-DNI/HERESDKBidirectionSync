---
title: "updateLocationOptions abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-updatelocationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateLocationOptions.html -->


<div>
<h1>updateLocationOptions abstract method</h1></div>

<a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>
updateLocationOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> locationOptions</li>
</ol>)

      

    

<p>Reconfigures the location engine with desired <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.</p>
<p>This method is a faster way to change location options for already started
location engine, than calling <a href="sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> and <a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> in sequence. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notReady</a>,
if called for unstarted location engine.
This method variant is not currently supported on iOS platforms. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which this method variant is not supported.</p>
<ul>
<li><code>locationOptions</code> Desired location options.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus updateLocationOptions(LocationOptions locationOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
