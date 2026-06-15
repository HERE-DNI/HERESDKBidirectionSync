---
title: "TileUrlProviderCallback typedef"
slug: "sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileUrlProviderCallback.html -->


<div>
<h1>TileUrlProviderCallback typedef</h1></div>

TileUrlProviderCallback =
     String Function(int x, int y, int level)


<p>Provides the URL as String for the given tile coordinates and storage level.</p>
<p>The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1.
The third parameter indicates the level of the tile.</p>
<ul>
<li>
<p><code>x</code> X coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
</li>
<li>
<p><code>y</code> Y coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
</li>
<li>
<p><code>level</code> Level of the tile.</p>
</li>
</ul>
<p>Returns the URL.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef TileUrlProviderCallback = String Function(int x, int y, int level);</code></pre>

 



</div>
`
}</HTMLBlock>
