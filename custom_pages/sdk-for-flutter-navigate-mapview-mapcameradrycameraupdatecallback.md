---
title: "MapCameraDryCameraUpdateCallback typedef"
slug: "sdk-for-flutter-navigate-mapview-mapcameradrycameraupdatecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraDryCameraUpdateCallback.html -->


<div>
<h1>MapCameraDryCameraUpdateCallback typedef</h1></div>

MapCameraDryCameraUpdateCallback =
     void Function(<a href="/sdk-for-flutter-navigate-mapview-mapcamerastate-class">MapCameraState</a>? cameraState)


<p>Used to report back results of dry update application to camera.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>cameraState</code> Map camera state after dry application of update</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapCameraDryCameraUpdateCallback = void Function(MapCameraState? cameraState);</code></pre>

 



</div>
`
}</HTMLBlock>
