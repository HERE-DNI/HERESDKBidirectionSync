---
title: "RasterDataSourceCacheConfiguration constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceCacheConfiguration.html -->


<div>
<h1>RasterDataSourceCacheConfiguration constructor</h1></div>

RasterDataSourceCacheConfiguration(<ol class="parameter-list single-line"> <li>String path, </li>
<li>int diskSize</li>
</ol>)
    

<p>Constructs a Cache object from the provided path and cache size.</p>
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
<li><code>diskSize</code> The maximum size to use on disk for the cache, in bytes. Default is 32 MiB.
This cache is independent from the map cache as defined via <code>SDKOptions</code>.
Its size is only limited by the total device storage capacity.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RasterDataSourceCacheConfiguration(this.path, this.diskSize);</code></pre>

 



</div>
`
}</HTMLBlock>
