---
title: "path property"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-path"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- path.html -->


<div>
<h1>path property</h1></div>

        
        String
        path
<div class="features">getter/setter pair</div>


<p>The path to the directory to use for the cache. By default, the map gets initialized with a
data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
unless an absolute path is provided. The cache can be stored in an internal/external storage as long
as the app has read/write permissions.
Empty string means the data path will be used for caching.
If the provided path, either as absolute path or as relative path is invalid,
then caching will be disabled.
There is no contraint regarding the existence of the path. If the path does not exist
but is valid, it will be created.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String path;</code></pre>

 



</div>
`
}</HTMLBlock>
