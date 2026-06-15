---
title: "addMapMarker3d abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmapmarker3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapMarker3d.html -->


<div>
<h1>addMapMarker3d abstract method</h1></div>

void
addMapMarker3d(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a> marker</li>
</ol>)

      

    

<p>Adds a 3D map marker to this map scene.</p>
<p>Does nothing if the marker instance was already added to the scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarker3D API to add a very large number of 3D
markers (especially 500+ also depending on the complexity of the 3D object) is not
recommended. Adding this many 3D markers has a negative impact on the performance leading to
stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>marker</code> The marker to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapMarker3d(MapMarker3D marker);</code></pre>

 



</div>
`
}</HTMLBlock>
