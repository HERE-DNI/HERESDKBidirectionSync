---
title: "RasterDataSource.withConfigurationAndListener constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasource-rasterdatasource-withconfigurationandlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSource.withConfigurationAndListener.html -->


<div>
<h1>RasterDataSource.withConfigurationAndListener constructor</h1></div>

RasterDataSource.withConfigurationAndListener(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapcontext-class">MapContext</a> context, </li>
<li><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-class">RasterDataSourceConfiguration</a> configuration, </li>
<li><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a> listener</li>
</ol>)
    

<p>Creates a RasterDataSource instance with the provided data source configuration and
registers a listener.</p>
<ul>
<li>
<p><code>context</code> The map context to associate the data source with.</p>
</li>
<li>
<p><code>configuration</code> The data source configuration object to use.</p>
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
<pre class="language-dart"><code class="language-dart">factory RasterDataSource.withConfigurationAndListener(MapContext context, RasterDataSourceConfiguration configuration, RasterDataSourceListener listener) =&gt; $prototype.withConfigurationAndListener(context, configuration, listener);</code></pre>

 



</div>
`
}</HTMLBlock>
