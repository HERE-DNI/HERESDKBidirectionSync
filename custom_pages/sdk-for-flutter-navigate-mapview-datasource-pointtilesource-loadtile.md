---
title: "loadTile abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-pointtilesource-loadtile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadTile.html -->


<div>
<h1>loadTile abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class">TileSourceLoadTileRequestHandle</a>?
loadTile(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a> tileKey, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-datasource-pointtilesourceloadresulthandler-class">PointTileSourceLoadResultHandler</a> completionHandler</li>
</ol>)

      

    

<p>Load data of a tile.</p>
<p>Upon completion, the handler gets informed.</p>
<ul>
<li>
<p><code>tileKey</code> Key of the tile to load data for.</p>
</li>
<li>
<p><code>completionHandler</code> Load result handler.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class">TileSourceLoadTileRequestHandle?</a>. A handle to the created load request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TileSourceLoadTileRequestHandle? loadTile(TileKey tileKey, PointTileSourceLoadResultHandler completionHandler);</code></pre>

 



</div>
`
}</HTMLBlock>
