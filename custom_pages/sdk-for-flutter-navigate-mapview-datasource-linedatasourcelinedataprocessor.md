---
title: "LineDataSourceLineDataProcessor typedef"
slug: "sdk-for-flutter-navigate-mapview-datasource-linedatasourcelinedataprocessor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LineDataSourceLineDataProcessor.html -->


<div>
<h1>LineDataSourceLineDataProcessor typedef</h1></div>

LineDataSourceLineDataProcessor =
     bool Function(<a href="/sdk-for-flutter-navigate-mapview-datasource-linedataaccessor-class">LineDataAccessor</a> lineAccessor)


<p>Called for each line, allowing inspection, removal or update of coordinates and attributes.</p>
<ul>
<li><code>lineAccessor</code> the line data accessor.</li>
</ul>
<p>Returns value indicating the result of the processing.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef LineDataSourceLineDataProcessor = bool Function(LineDataAccessor lineAccessor);</code></pre>

 



</div>
`
}</HTMLBlock>
