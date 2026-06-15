---
title: "PolygonDataSourcePolygonDataProcessor typedef"
slug: "sdk-for-flutter-explore-mapview-datasource-polygondatasourcepolygondataprocessor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonDataSourcePolygonDataProcessor.html -->


<div>
<h1>PolygonDataSourcePolygonDataProcessor typedef</h1></div>

PolygonDataSourcePolygonDataProcessor =
     bool Function(<a href="sdk-for-flutter-explore-mapview-datasource-polygondataaccessor-class">PolygonDataAccessor</a> polygonAccessor)


<p>Called for each polygon, allowing inspection, removal or update of coordinates and attributes.</p>
<ul>
<li><code>polygonAccessor</code> the polygon data accessor.</li>
</ul>
<p>Returns value indicating the result of the processing.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef PolygonDataSourcePolygonDataProcessor = bool Function(PolygonDataAccessor polygonAccessor);</code></pre>

 



</div>
`
}</HTMLBlock>
