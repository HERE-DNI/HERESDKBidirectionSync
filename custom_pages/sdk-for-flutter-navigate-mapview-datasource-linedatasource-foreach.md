---
title: "forEach abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-linedatasource-foreach"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- forEach.html -->


<div>
<h1>forEach abstract method</h1></div>

void
forEach(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-linedatasourcelinedataprocessor">LineDataSourceLineDataProcessor</a> processor</li>
</ol>)

      

    

<p>Iterates through all the lines from the data source and passes them to the
given processor, one by one.</p>
<p>The processor can update the line data.
The iteration stops after all lines have been processed or the processor returns false
from the process call.</p>
<ul>
<li><code>processor</code> Line processor.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void forEach(LineDataSourceLineDataProcessor processor);</code></pre>

 



</div>
`
}</HTMLBlock>
