---
title: "addMapPolygons abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-addmappolygons"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapPolygons.html -->


<div>
<h1>addMapPolygons abstract method</h1></div>

void
addMapPolygons(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-mapview-mappolygon-class">MapPolygon</a>&gt; mapPolygons</li>
</ol>)

      

    

<p>Adds multiple map polygons to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapPolygon API to add a very large number of polygons
(especially 1000+ also depending on their complexity) is not recommended.
Adding this many polygons has a negative impact on the performance leading to stuttering of
the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="/sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>mapPolygons</code> The map polygons to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapPolygons(List&lt;MapPolygon&gt; mapPolygons);</code></pre>

 



</div>
`
}</HTMLBlock>
