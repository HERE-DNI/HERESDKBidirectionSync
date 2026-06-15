---
title: "addMapPolygon abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-addmappolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapPolygon.html -->


<div>
<h1>addMapPolygon abstract method</h1></div>

void
addMapPolygon(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-mappolygon-class">MapPolygon</a> mapPolygon</li>
</ol>)

      

    

<p>Adds a map polygon to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapPolygon API to add a very large number of polygons
(especially 1000+ also depending on their complexity) is not recommended.
Adding this many polygons has a negative impact on the performance leading to stuttering of
the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>mapPolygon</code> The map polygon to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapPolygon(MapPolygon mapPolygon);</code></pre>

 



</div>
`
}</HTMLBlock>
