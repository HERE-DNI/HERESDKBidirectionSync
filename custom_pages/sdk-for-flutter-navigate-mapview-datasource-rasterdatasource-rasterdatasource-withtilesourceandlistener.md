---
title: "RasterDataSource.withTileSourceAndListener constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSource.withTileSourceAndListener.html -->


<div>
<h1>RasterDataSource.withTileSourceAndListener constructor</h1></div>

RasterDataSource.withTileSourceAndListener(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a> context, </li>
<li>String name, </li>
<li><a href="sdk-for-flutter-navigate-mapview-datasource-rastertilesource-class">RasterTileSource</a> tileSource, </li>
<li><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a> listener, </li>
</ol>)
    

<p>Creates a RasterDataSource instance with the provided raster tile source and registers
a listener.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>context</code> The map context to associate the data source with.</p>
</li>
<li>
<p><code>name</code> The unique name of the data source.</p>
</li>
<li>
<p><code>tileSource</code> The raster tile source.</p>
</li>
<li>
<p><code>listener</code> The initial listener to be registered for receiving state notifications.
Due to the asynchronous nature of the data source initialization, the listeners
registered later might miss some notifications. This listener is guaranteed to
receive all notifications.
The state notifications can occur on an arbitrary thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterDataSource.withTileSourceAndListener(MapContext context, String name, RasterTileSource tileSource, RasterDataSourceListener listener) =&gt; $prototype.withTileSourceAndListener(context, name, tileSource, listener);</code></pre>

 



</div>
`
}</HTMLBlock>
