---
title: "forEach abstract method"
slug: "sdk-for-flutter-explore-mapview-datasource-pointdatasource-foreach"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- forEach.html -->


<div>
<h1>forEach abstract method</h1></div>

void
forEach(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor">PointDataSourcePointDataProcessor</a> processor</li>
</ol>)

      

    

<p>Iterates through all the points from the data source and passes them to the
given processor, one by one.</p>
<p>The processor can update the point data.</p>
<p>The iteration stops after all points have been processed or the processor returns false
from the process call.</p>
<ul>
<li><code>processor</code> Point data processor.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void forEach(PointDataSourcePointDataProcessor processor);</code></pre>

 



</div>
`
}</HTMLBlock>
