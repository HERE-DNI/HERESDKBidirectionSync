---
title: "removeIf abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-polygondatasource-removeif"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- removeIf.html -->


<div>
<h1>removeIf abstract method</h1></div>

void
removeIf(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-polygondatasourcepolygondataprocessor">PolygonDataSourcePolygonDataProcessor</a> inspector</li>
</ol>)

      

    

<p>Iterates through all the polygons from the data source and passes them to the
given inspector, one by one.</p>
<p>All polygons for which the inspector returns <code>true</code> get removed from the data source.
The inspector cannot update the polygon data.</p>
<ul>
<li><code>inspector</code> Polygon data processor.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void removeIf(PolygonDataSourcePolygonDataProcessor inspector);</code></pre>

 



</div>
`
}</HTMLBlock>
