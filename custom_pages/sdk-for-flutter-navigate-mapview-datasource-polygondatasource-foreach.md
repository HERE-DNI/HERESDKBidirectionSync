---
title: "forEach abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-polygondatasource-foreach"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- forEach.html -->


<div>
<h1>forEach abstract method</h1></div>

void
forEach(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-polygondatasourcepolygondataprocessor">PolygonDataSourcePolygonDataProcessor</a> processor</li>
</ol>)

      

    

<p>Iterates through all the polygons from the data source and passes them to the
given processor, one by one.</p>
<p>The processor can update the polygon data.</p>
<p>The iteration stops after all polygons have been processed or the processor returns false
from the process call.</p>
<ul>
<li><code>processor</code> Polygon processor.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void forEach(PolygonDataSourcePolygonDataProcessor processor);</code></pre>

 



</div>
`
}</HTMLBlock>
