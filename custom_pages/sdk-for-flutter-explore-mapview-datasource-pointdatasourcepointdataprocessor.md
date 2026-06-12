---
title: "PointDataSourcePointDataProcessor typedef"
slug: "sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PointDataSourcePointDataProcessor.html -->


<div>
<h1>PointDataSourcePointDataProcessor typedef</h1></div>

PointDataSourcePointDataProcessor =
     bool Function(<a href="/sdk-for-flutter-explore-mapview-datasource-pointdataaccessor-class">PointDataAccessor</a> pointAccessor)


<p>Called for each point, allowing inspection, removal or update of coordinates and attributes.</p>
<ul>
<li><code>pointAccessor</code> the point data accessor.</li>
</ul>
<p>Returns value indicating the result of the processing.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef PointDataSourcePointDataProcessor = bool Function(PointDataAccessor pointAccessor);</code></pre>

 



</div>
`
}</HTMLBlock>
