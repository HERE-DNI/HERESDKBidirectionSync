---
title: "IndoorLevelChangeData constructor"
slug: "sdk-for-flutter-navigate-routing-indoorlevelchangedata-indoorlevelchangedata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IndoorLevelChangeData.html -->


<div>
<h1>IndoorLevelChangeData constructor</h1></div>

IndoorLevelChangeData(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a> connector, </li>
<li>int deltaZ</li>
</ol>)
    

<p>Creates an Indoor level change data object and assign values for level change data.</p>
<ul>
<li><code>connector</code> Type of the connector to change the level.</li>
<li><code>deltaZ</code> The number of levels to change, positive for up, negative for down. For example,
a value of -1 means that a user needs to go one level down. The value is never 0.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">IndoorLevelChangeData(this.connector, this.deltaZ);</code></pre>

 



</div>
`
}</HTMLBlock>
