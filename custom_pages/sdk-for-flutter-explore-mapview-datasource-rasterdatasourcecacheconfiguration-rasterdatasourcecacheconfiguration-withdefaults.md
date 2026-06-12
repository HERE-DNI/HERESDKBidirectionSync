---
title: "RasterDataSourceCacheConfiguration.withDefaults constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration-withdefaults"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceCacheConfiguration.withDefaults.html -->


<div>
<h1>RasterDataSourceCacheConfiguration.withDefaults constructor</h1></div>

RasterDataSourceCacheConfiguration.withDefaults(<ol class="parameter-list single-line"> <li>String path</li>
</ol>)
    

<p>Constructs a Cache object from the provided path and a default cache size of 32 MiB.</p>
<ul>
<li><code>path</code> The path to the directory to use for the cache. By default, the map gets initialized with a
data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
unless an absolute path is provided. The cache can be stored in an internal/external storage as long
as the app has read/write permissions.
Empty string means the data path will be used for caching.
If the provided path, either as absolute path or as relative path is invalid,
then caching will be disabled.
There is no contraint regarding the existence of the path. If the path does not exist
but is valid, it will be created.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceCacheConfiguration.withDefaults(this.path)
    : diskSize = 33554432;</code></pre>

 



</div>
`
}</HTMLBlock>
