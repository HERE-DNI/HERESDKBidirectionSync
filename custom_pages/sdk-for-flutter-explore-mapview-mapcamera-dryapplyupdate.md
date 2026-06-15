---
title: "dryApplyUpdate abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-dryapplyupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dryApplyUpdate.html -->


<div>
<h1>dryApplyUpdate abstract method</h1></div>

void
dryApplyUpdate(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a> cameraUpdate, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapcameradrycameraupdatecallback">MapCameraDryCameraUpdateCallback</a> callback</li>
</ol>)

      

    

<p>Computes result of applying camera update without changing state of the map camera.</p>
<p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>cameraUpdate</code> The update that gets dryly applied to camera.</p>
</li>
<li>
<p><code>callback</code> Called upon completion with computed map state.
The callback is called from an arbitrary thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void dryApplyUpdate(MapCameraUpdate cameraUpdate, MapCameraDryCameraUpdateCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
