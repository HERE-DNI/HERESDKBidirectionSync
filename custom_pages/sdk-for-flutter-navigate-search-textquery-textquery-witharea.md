---
title: "TextQuery.withArea constructor"
slug: "sdk-for-flutter-navigate-search-textquery-textquery-witharea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TextQuery.withArea.html -->


<div>
<h1>TextQuery.withArea constructor</h1></div>

TextQuery.withArea(<ol class="parameter-list single-line"> <li>String query, </li>
<li><a href="/sdk-for-flutter-navigate-search-textqueryarea-class">TextQueryArea</a> area</li>
</ol>)
    

<p>Constructs a TextQuery from the provided text query and geographic area.</p>
<p>For Offline Search, search in a given <code>GeoBox</code>, <code>GeoCircle</code> or <code>GeoCorridor</code>
restricts the results to only POIs.</p>
<ul>
<li>
<p><code>query</code> Desired query to search.</p>
</li>
<li>
<p><code>area</code> Area which to provide the most relevant places.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TextQuery.withArea(String query, TextQueryArea area) =&gt; $prototype.withArea(query, area);</code></pre>

 



</div>
`
}</HTMLBlock>
