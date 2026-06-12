---
title: "addMapMarkers3d abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-addmapmarkers3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapMarkers3d.html -->


<div>
<h1>addMapMarkers3d abstract method</h1></div>

void
addMapMarkers3d(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a>&gt; markers</li>
</ol>)

      

    

<p>Adds multiple 3D map markers to this map scene.</p>
<p>Adding the same 3D marker instances multiple
times has no effect.</p>
<p><strong>Note:</strong>
Due to technical limitations, using the MapMarkers3D API to add a very large number of 3D
markers (especially 500+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="/sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>markers</code> The list of 3D markers to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapMarkers3d(List&lt;MapMarker3D&gt; markers);</code></pre>

 



</div>
`
}</HTMLBlock>
