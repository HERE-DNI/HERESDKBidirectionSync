---
title: "TileKey constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-tilekey-tilekey"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileKey.html -->


<div>
<h1>TileKey constructor</h1></div>

TileKey(<ol class="parameter-list single-line"> <li>int x, </li>
<li>int y, </li>
<li>int level</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>x</code> X coordinate of the tile. This ranges from 0 to 2^level − 1.</li>
<li><code>y</code> Y coordinate of the tile. This ranges from 0 to 2^level − 1.</li>
<li><code>level</code> Level of the tile. Supported range [0, 31].</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TileKey(this.x, this.y, this.level);</code></pre>

 



</div>
`
}</HTMLBlock>
